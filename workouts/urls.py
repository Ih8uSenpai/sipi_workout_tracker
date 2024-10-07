from django.urls import path
from . import views
from .views import WorkoutList

urlpatterns = [
    path('workouts/', views.workout_list, name='workout_list'),
    path('api/workouts/', WorkoutList.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('workouts/<int:pk>/log/', views.log_workout, name='log_workout'),
]
