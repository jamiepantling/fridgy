from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# import login
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Food, Household, Profile

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Food functions

def foods_index(request):
    foods = Food.objects.all
    return render(request, 'foods/index.html', {"foods": foods})

# Household functions

def household_index(request):
    household = Household.objects.all()
    return render(request, 'households/index.html', {'household': household})
def household_detail(request, household_id):
    household = Household.objects.get(id=household_id)
    users_in_house = Profile.objects.filter(household=household_id)
    return render(request, 'households/detail.html', { 'household': household, 'users_in_house': users_in_house })

# Household class-based views

class HouseholdCreate(CreateView):
    model = Household
    fields = ['name']
    success_url = '/' # Changed when new route finished
class HouseholdUpdate(UpdateView):
    model = Household
    fields = ['name']
    success_url = '/' # Changed later to household details
class HouseholdDelete(DeleteView):
    model = Household
    success_url = '/' # Change success?


# Authorization functions
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Something went wrong - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
