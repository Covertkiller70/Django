from django.urls import path
from proapp import views

urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'help/',views.help,name='help')
]