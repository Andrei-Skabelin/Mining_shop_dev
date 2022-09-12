from django.urls import path

from cart import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_item_add, name='cart_item_add'),
    path('remove/<int:product_id>/', views.cart_item_remove, name='cart_item_remove'),
    # path('order/', views.OrderView.as_view(), name='order'),
]
