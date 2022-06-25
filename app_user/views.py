from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile/create')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class AnotherLogin(LoginView):
    template_name = 'login.html'


class AnotherLogout(LogoutView):
    template_name = 'logout.html'
