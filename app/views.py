from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# import login
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Food, Household, Profile
from .forms import UpdateUserForm, UpdateProfileForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Food functions

def foods_index(request):
    foods = Food.objects.all
    return render(request, 'foods/index.html', {"foods": foods})

# Food Class-based views

class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ["food_name", "category", "expiry", "shareable", "count"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
            return redirect('profile_detail')
        else:
            error_message = 'Something went wrong - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
def profile_detail(request, user_id):
    profile = Profile.objects.get(user=user_id)
    user = User.objects.get(id=user_id)
    return render(request, 'profile/detail.html', {'profile': profile, 'user': user})
def profile_edit(request, user_id):
    profile = Profile.objects.get(user=user_id)
    user = User.objects.get(id=user_id)
    update_user_form = UpdateUserForm()
    update_profile_form = UpdateProfileForm
    return render(request, 'profile/edit.html', {'user': user, 'profile': profile, 'update_user_form': update_user_form, 'update_profile_form': update_profile_form})
def profile_update(request, user_id):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_image = request.POST['user_image']
        myuser = User.objects.get(pk=user_id)
        myuser.username = username
        myuser.email = email
        myuser.first_name = first_name
        myuser.last_name = last_name
        profile = Profile.objects.get(user=user_id)
        profile.user_image = user_image
        myuser.save()
        profile.save()
    return redirect('profile_detail', user_id=user_id)
# Class Views
class ProfileDelete(DeleteView):
    model = User
    success_url = '/'




