from django.urls import path
from django.conf.urls import include
from proapp import views

urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'users/',views.users,name='users'),
    path(r'help/',views.help,name='help')
]