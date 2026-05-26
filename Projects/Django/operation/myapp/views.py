from django.shortcuts import render

# Create your views here.

def home(request):
    result = None

    if request.method == "POST":
        num1 = int(request.POST.get("num1"))
        num2 = int(request.POST.get("num2"))
        op = request.POST.get("op")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Cannot divide by 0"
        elif op == "%":
            result = num1 % num2

    return render(request, "home.html", {"result": result})