from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Food url patterns
    path("foods/", views.foods_index, name="index"),
    
    # Household url patterns
    path('household/', views.household_index, name='houeshold_index'), # Just to check if housheold had been created, no need to route users here
    path('household/<int:household_id>/', views.household_detail, name='household_detail'),
    path('household/create/', views.HouseholdCreate.as_view(), name='household_create'),
    path('household/<int:pk>/update/', views.HouseholdUpdate.as_view(), name='household_update'),
    path('household/<int:pk>/delete/', views.HouseholdDelete.as_view(), name='household_delete'),

    # accounts url patterns
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:user_id>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:user_id>/update/', views.profile_update, name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete')
]