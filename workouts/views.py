from django.shortcuts import render, get_object_or_404
from .models import Workout, WorkoutSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# РЎРїРёСЃРѕРє С‚СЂРµРЅРёСЂРѕРІРѕРє
def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

# Р”РµС‚Р°Р»Рё С‚СЂРµРЅРёСЂРѕРІРєРё
def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})

# Р›РѕРі С‚СЂРµРЅРёСЂРѕРІРєРё (РІРІРѕРґ СЂРµР·СѓР»СЊС‚Р°С‚РѕРІ)
def log_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        # Р›РѕРіРёРєР° СЃРѕС…СЂР°РЅРµРЅРёСЏ РґР°РЅРЅС‹С… С‚СЂРµРЅРёСЂРѕРІРєРё
        pass
    return render(request, 'workouts/log_workout.html', {'workout': workout})

class WorkoutList(APIView):
    def get(self, request):
        return Response({"message": "Hello, this is the workout API!"}, status=status.HTTP_200_OK)