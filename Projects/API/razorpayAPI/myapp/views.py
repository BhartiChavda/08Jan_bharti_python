from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_SECRET_KEY))

def index(request):
    return render(request, 'index.html')

def order_payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100  # Amount in paise

        # Create Razorpay Order
        razorpay_order = client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1" # auto capture
        })

        context = {
            'order_id': razorpay_order['id'],
            'amount': amount,
            'display_amount': amount // 100,
            'api_key': settings.RAZORPAY_API_KEY,
        }
        return render(request, 'payment.html', context)
    return render(request, 'index.html')

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')
        
        # Verify Payment Signature
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
        
        try:
            client.utility.verify_payment_signature(params_dict)
            # Payment Successful
            return render(request, 'success.html', {'status': 'Payment Successful'})
        except razorpay.errors.SignatureVerificationError:
            return render(request, 'success.html', {'status': 'Payment Failed - Invalid Signature'})

    return render(request, 'success.html')
