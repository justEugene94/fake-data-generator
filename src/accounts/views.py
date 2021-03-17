from django.contrib.auth.views import LoginView

from accounts.forms import MyAuthenticationForm


class MyLoginView(LoginView):
    """ Login view"""

    form_class = MyAuthenticationForm
    template_name = 'accounts/login.html'