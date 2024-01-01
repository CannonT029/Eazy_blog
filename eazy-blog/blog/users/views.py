from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            messages.success(request, '{}  added.'.format(user.username))

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    
    #error 
    if not form.is_valid() and request.method == 'POST':
        return render(request, 'users/register.html', {'form': form})


    return render(request, 'users/register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LogInForm(request, data=request.POST)

        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = LogInForm()

    return render(request, 'users/login.html', {'form': form})

