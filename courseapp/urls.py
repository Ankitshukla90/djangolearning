from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('lesson', views.lesson, name='lesson'),
    path('badge', views.badge, name='badge'),
    path('certificate', views.certificate, name='certificate'),
    path('quizes', views.quizes, name='quizes'),
    path('courses', views.courses, name='courses'),
    path('coursedetails', views.coursedetails, name='coursedetails'),
]

api_urlpatterns = [
    
   
]