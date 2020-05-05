from django.urls import path
from passapp import views

app_name = 'passapp'

urlpatterns = [
    path('registration/',views.register,name='registration'),
    path('',views.index,name='index'),
    path('user_login/',views.user_login,name='user_login'),
]