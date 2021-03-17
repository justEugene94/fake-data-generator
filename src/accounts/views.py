from django.contrib.auth.views import LoginView, LogoutView

from accounts.forms import MyAuthenticationForm


class MyLoginView(LoginView):
    """ Login view"""

    form_class = MyAuthenticationForm
    template_name = 'accounts/login.html'


class MyLogoutView(LogoutView):
    """ Logout view """

    template_name = 'accounts/logout.html'