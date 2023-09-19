from django.shortcuts import render, redirect

# Import CBV's
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView

# Import Models
from .models import Workout, Exercise

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def workouts_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html', { 'workouts': workouts})

def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    # add form here
    return render(request, 'workouts/detail.html', {'workout': workout})

class WorkoutCreate(CreateView):
    model = Workout
    fields = ['name', 'date', 'duration', 'description']
    success_url = '/workouts/{workout_id}'

class WorkoutUpdate(UpdateView):
    model = Workout 
    fields = ['name', 'date', 'duration', 'description']

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts'

class ExerciseList(ListView):
    model = Exercise
    template_name = 'exercises/index.html'

class ExerciseDetail(DetailView):
    model = Exercise
    template_name = 'exercises/detail.html'

class ExerciseCreate(CreateView):
    model = Exercise
    fields = '__all__'