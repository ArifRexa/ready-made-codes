from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import authenticate, login, logout

# User = get_user_model
CustomUser = get_user_model()

# Create your views here.

def logout_view(request):
    logout (request)
    return redirect ('login')




# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to a success page or login page
#             return redirect('login')  # Assuming you have a URL pattern named 'login'
#     else:
#         form = RegistrationForm()
#     return render(request, 'signup.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Check if username or email is already taken
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken.')
            elif CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'This email is already associated with an account.')
            else:
                form.save()
                # Redirect to a success page or login page
                return redirect('login')  # Assuming you have a URL pattern named 'login'
        else:
            # If form is not valid, show form-level error messages
            error_message = form.errors.get('__all__')
            if error_message:
                messages.error(request, error_message)
            if 'username' in form.errors:
                messages.error(request, 'This username is already taken.')
            if 'email' in form.errors:
                messages.error(request, 'This email is already associated with an account.')
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form': form})





# def login_view(request):
#     form = LoginForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.add_message(request, messages.ERROR, 'Invalid User')

#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'Invalid email or password')  # Add custom form-level error
                # You can also use messages framework to display the error message
                messages.add_message(request, messages.ERROR, 'Invalid email or password')
                
    context = {
        'form': form
    }
    return render(request, 'login.html', context)



