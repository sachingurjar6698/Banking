from django.urls import path
from credits import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('customers_list/', views.transfer, name='transfer'),
    path('customer/<int:user_id>/', views.money, name='money'),
    path('customer/<int:user_id>/transaction', views.transaction, name='transaction'),
    path('all_transaction/', views.all_transaction, name='all_transaction'),
]