from django.urls import path
from hello_world import views

app_name = 'hello_world'

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('schools/',views.SchoolListView.as_view(),name='list'),
    path('schools/create/',views.SchoolCreateView.as_view(),name='create'),
    path('schools/<pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('schools/update/<pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('schools/delete/<pk>/',views.SchoolDeleteView.as_view(),name='delete'),
]