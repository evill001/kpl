from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView

def main(request):
    return render(request, 'traur2/main.html')

def reg(request):
    return render(request, 'traur2/reg.html')

def suvenir(request):
    return render(request, 'traur2/suvenir.html')

def kontact(request):
    return render(request, 'traur2/kontact.html')

def vhod(request):
    return render(request, 'traur2/vhod.html')

def product_detail(request):
    return render(request, 'traur2/product_detail.html')

def cart(request):
    return render(request, 'traur2/cart.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('traur2/main.html')
        else:
            # Обработка неверных данных входа
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})