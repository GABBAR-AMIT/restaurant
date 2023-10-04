from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('order/<int:pk>', order, name='order'),
    path('menu/<int:pk>', menu, name='menu'),
    path('or/<int:pk>', orders_for_table, name='orderdetail'),
    path('kit', kit, name='kitchen'),
    path('user', userdetails, name='user'),
]