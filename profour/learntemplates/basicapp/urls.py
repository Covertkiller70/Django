from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('mytest/',views.mytest,name='mytest'),
    path('other/',views.other,name='other'),
]
