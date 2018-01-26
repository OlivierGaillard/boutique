from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


# Create your views here.

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'


class ThanksView(TemplateView):
    template_name = 'accounts/thanks.html'