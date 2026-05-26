import random
import string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .models import User, Category, Note
from .forms import SignupForm, NoteUploadForm, NoteWriteForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def home(request):
    return render(request, 'userapp/home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            
            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'userapp/signup.html', {'form': form})
                
            user = form.save(commit=False)
            user.set_password(password)
            user.otp = generate_otp()
            user.save()
            # Send Beautiful HTML OTP
            from django.template.loader import render_to_string
            from django.utils.html import strip_tags
            
            html_message = render_to_string('emails/otp_email.html', {'otp': user.otp})
            plain_message = strip_tags(html_message)
            
            send_mail(
                'Verify your account - NotesHub',
                plain_message,
                'NotesHub <bhuribharu@gmail.com>',
                [user.email],
                fail_silently=False,
                html_message=html_message
            )
            request.session['verify_email'] = user.email
            messages.success(request, 'OTP sent to your email. Please verify to continue.')
            return redirect('verify_otp')
    else:
        form = SignupForm()
    return render(request, 'userapp/signup.html', {'form': form})

def verify_otp(request):
    email = request.session.get('verify_email')
    if not email:
        return redirect('signup')
    
    if request.method == 'POST':
        otp = request.POST.get('otp')
        try:
            user = User.objects.get(email=email, otp=otp)
            user.is_verified = True
            user.otp = None
            user.save()
            # We don't login automatically to ensure they know their credentials
            del request.session['verify_email']
            messages.success(request, 'Email verified successfully! Please sign in with your credentials.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Invalid OTP or email.')
    
    return render(request, 'userapp/verify_otp.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_verified:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Your account is not verified. Please check your email for the verification link sent during signup.')
    else:
        form = AuthenticationForm()
    return render(request, 'userapp/login.html', {'form': form})

from django.db.models import Q

@login_required
def dashboard(request):
    notes = Note.objects.filter(user=request.user)
    current_filter = request.GET.get('filter', 'all')
    search_query = request.GET.get('q')
    
    if search_query:
        notes = notes.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) | 
            Q(content__icontains=search_query)
        )

    if current_filter == 'recent':
        from django.utils import timezone
        today = timezone.now().date()
        # Show notes created strictly today
        notes = notes.filter(created_at__date=today).order_by('-created_at')
    elif current_filter == 'shared':
        # Show ONLY active shared notes
        notes = notes.filter(is_shared=True, is_archived=False).order_by('-created_at')
    elif current_filter == 'archive':
        # Show ONLY archived notes
        notes = notes.filter(is_archived=True).order_by('-created_at')
    else:
        # Default 'all' - show EVERYTHING (including archived)
        notes = notes.order_by('-created_at')
        
    return render(request, 'userapp/dashboard.html', {
        'notes': notes,
        'current_filter': current_filter
    })

@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteUploadForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note uploaded successfully!')
            return redirect('dashboard')
    else:
        form = NoteUploadForm()
    return render(request, 'userapp/upload_note.html', {'form': form, 'type': 'upload'})

@login_required
def write_note(request):
    if request.method == 'POST':
        form = NoteWriteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note saved successfully!')
            return redirect('dashboard')
    else:
        form = NoteWriteForm()
    return render(request, 'userapp/upload_note.html', {'form': form, 'type': 'write'})

@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    # Determine which form to use
    if note.file:
        form_class = NoteUploadForm
        note_type = 'upload'
    else:
        form_class = NoteWriteForm
        note_type = 'write'
        
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('dashboard')
    else:
        form = form_class(instance=note)
        
    return render(request, 'userapp/upload_note.html', {
        'form': form, 
        'type': note_type,
        'is_edit': True
    })

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    messages.success(request, 'Note deleted permanently!')
    return redirect('dashboard')

@login_required
def toggle_archive(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.is_archived = not note.is_archived
    note.save()
    status = "archived" if note.is_archived else "restored"
    messages.success(request, f'Note {status} successfully!')
    return redirect('dashboard')

@login_required
def toggle_share(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.is_shared = not note.is_shared
    note.save()
    status = "shared" if note.is_shared else "unshared"
    messages.success(request, f'Note {status} successfully!')
    return redirect('dashboard')

@login_required
def user_view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    return render(request, 'userapp/view_note.html', {'note': note})

def view_shared_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, is_shared=True)
    return render(request, 'userapp/shared_view.html', {'note': note})

@login_required
def settings(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('settings')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'userapp/settings.html', {'form': form})

@login_required
def security_settings(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password updated successfully!')
            return redirect('security_settings')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userapp/security.html', {'form': form})

@login_required
def integrations_settings(request):
    return render(request, 'userapp/integrations.html')

def user_logout(request):
    logout(request)
    return redirect('login')
