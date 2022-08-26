from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.Registers.as_view(), name='registration'),
]
