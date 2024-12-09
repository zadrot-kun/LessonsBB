from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView

class Login(LoginView):
    template_name = 'auth/login.html'


class PasswordChange(PasswordChangeView):
    template_name = 'auth/password_change_form.html'


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'auth/password_change_done.html'
