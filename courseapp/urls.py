from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('lesson', views.lesson, name='lesson'),
    path('badge', views.badge, name='badge'),
    path('certificate', views.certificate, name='certificate'),
    path('quizes', views.quizes, name='quizes'),
]

api_urlpatterns = [
    path('lesson', views.LessonList.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', views.LessonDetail.as_view(), name='lesson_detail'),
    path('badge', views.BadgeList.as_view(), name='badge_list'),
    path('badge/<int:pk>', views.BadgeDetail.as_view(), name='badge_detail'),
    path('quiz', views.QuizList.as_view(), name='quiz_list'),
    path('quiz/<int:pk>', views.QuizDetail.as_view(), name='quiz_detail'),

]
