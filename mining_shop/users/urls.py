# from django.urls import path, include
# from django.views.generic import TemplateView
from rest_framework import routers

from users.api import UserViewSet
# from users.views import RegistersView, EmailVerify, MyLoginView

# urlpatterns = [
#
#     path('login/', MyLoginView.as_view(), name='login'),
#     path('', include('django.contrib.auth.urls')),
#     path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),
#     path('verify_email/<uidb64>/<token>', EmailVerify.as_view(), name='verify_email'),
#     path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
#     path('registration/', RegistersView.as_view(), name='registration'),
# ]
router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
