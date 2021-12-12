from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your accounts has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form':form}
    return render(request, 'accounts/signup.html', context)
