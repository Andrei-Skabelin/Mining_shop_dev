from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm


class Registers(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    temlate_name = 'registration.html'
