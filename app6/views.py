from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, SavingsAccountForm
from .models import Customer

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('products', cust_id=customer.CustId)
    else:
        form = CustomerRegistrationForm()
    return render(request, 'app6/register.html', {'form': form})

def products(request, cust_id):
    return render(request, 'app6/products.html', {'cust_id': cust_id})

def open_savings_account(request):
    if request.method == 'POST':
        form = SavingsAccountForm(request.POST)
        if form.is_valid():
            # Process savings account opening
            return redirect('success')
    else:
        form = SavingsAccountForm()
    return render(request, 'app6/open_savings_account.html', {'form': form})

def success(request):
    return render(request, 'app6/success.html')
