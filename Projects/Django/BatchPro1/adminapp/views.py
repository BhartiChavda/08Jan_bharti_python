from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from userapp.models import User, Note, Category
from django.db.models import Count
from django.contrib import messages

@staff_member_required
def admin_dashboard(request):
    total_users = User.objects.filter(is_staff=False).count()
    total_notes = Note.objects.count()
    total_categories = Category.objects.count()
    recent_notes = Note.objects.all().order_by('-created_at')[:5]
    recent_users = User.objects.filter(is_staff=False).order_by('-date_joined')[:5]
    
    return render(request, 'adminapp/dashboard.html', {
        'total_users': total_users,
        'total_notes': total_notes,
        'total_categories': total_categories,
        'recent_notes': recent_notes,
        'recent_users': recent_users,
    })

@staff_member_required
def manage_users(request):
    query = request.GET.get('search', '')
    users = User.objects.filter(is_staff=False).order_by('-date_joined')
    if query:
        users = users.filter(username__icontains=query) | users.filter(email__icontains=query)
    
    return render(request, 'adminapp/users.html', {
        'users': users,
        'query': query
    })

@staff_member_required
def manage_notes(request):
    query = request.GET.get('search', '')
    notes = Note.objects.all().order_by('-created_at')
    if query:
        notes = notes.filter(title__icontains=query) | notes.filter(user__username__icontains=query)
    
    return render(request, 'adminapp/notes.html', {
        'notes': notes,
        'query': query
    })

@staff_member_required
def manage_categories(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('manage_categories')
    return render(request, 'adminapp/categories.html', {'categories': categories})

@staff_member_required
def view_note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'adminapp/view_note.html', {'note': note})

@staff_member_required
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    messages.success(request, "Note deleted successfully.")
    return redirect('manage_notes')

@staff_member_required
def toggle_user_status(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = not user.is_active
    user.save()
    status = "activated" if user.is_active else "blocked"
    messages.success(request, f"User {user.username} has been {status} successfully.")
    return redirect('manage_users')

@staff_member_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    username = user.username
    user.delete()
    messages.success(request, f"User {username} and all their notes have been deleted.")
    return redirect('manage_users')

@staff_member_required
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.is_verified = 'is_verified' in request.POST
        user.save()
        messages.success(request, f"User {user.username} updated successfully.")
        return redirect('manage_users')
    return render(request, 'adminapp/edit_user.html', {'user': user})
