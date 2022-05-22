from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("foods/", views.foods_index, name="index"),
    # accounts url patterns
    path('accounts/signup/', views.signup, name='signup'),
]