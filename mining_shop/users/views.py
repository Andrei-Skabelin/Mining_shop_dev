from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.shortcuts import render, redirect
from users.forms import UserCreationForm
from users.utils import send_email_for_verify

from users.forms import AuthenticationForm

User = get_user_model()


class MyLoginView(LoginView):
    form_class = AuthenticationForm


class RegistersView(View):

    template_name = 'users/registration.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()         # Форма создания пользователя взята из Django
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST) # Принимает и отправляет полученные данные отправленные от пост

        if form.is_valid():                                              # Если данные пришли валидные то
            form.save()                                                  # их сохраняем
            email = form.cleaned_data.get('email')                       # потом получаем email
            password = form.cleaned_data.get('password1')                # получаем пароль
            user = authenticate(email=email, password=password)          # получает с базы данных пользователя принимая емаил и пароль
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form                                                 # если данные не валидные они передаются в шаблон для обработки и вывода ошибок
        }
        return render(request, self.template_name, context)


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user
