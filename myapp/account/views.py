from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.conf import settings

signin = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'account/signin.html',
    success_url = settings.LOGIN_URL,

)

login = LoginView.as_view(
    template_name = 'account/login.html',
)

logout = LogoutView.as_view(
    next_page = settings.LOGIN_REDIRECT_URL,
)

@login_required
def profile(request):
    return render(request, 'blog/postlist.html')


