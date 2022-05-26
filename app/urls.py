from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Food url patterns
    path("foods/", views.foods_index, name="index"),
    path("foods/create/", views.FoodCreate.as_view(), name="foods_create"),
    path('foods/<int:food_id>/', views.foods_detail, name='foods_detail'),
    path('foods/<int:food_id>/edit/', views.foods_edit, name='foods_edit'),
   # path('foods/<int:food_id>/update/', views.foods_update, name='foods_update'),
    # path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
    
    # Household url patterns
    path('household/', views.household_index, name='household_index'), # Just to check if housheold had been created, no need to route users here
    path('household/create/', views.HouseholdCreate.as_view(), name='household_create'),
    path('household/<int:household_id>/', views.household_detail, name='household_detail'),
    path('household/<int:household_id>/edit/', views.household_edit, name='household_edit'),
    path('household/<int:household_id>/update/', views.household_update, name='household_update'),
    path('household/<int:household_id>/remove/', views.household_remove_user, name='household_remove_user'),
    path('household/<int:pk>/delete/', views.HouseholdDelete.as_view(), name='household_delete'),

    # accounts url patterns
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/success/', views.login_success, name='login_success'),
    path('password-change/', views.change_password, name='user_change_password'),
    path('accounts/login/success/', views.login_success, name='login_success'),
    path('accounts/password-change/done/', views.change_password_done, name='change_password_done'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:user_id>/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<int:user_id>/update/', views.profile_update, name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),

    # Group url patterns
    path('group/create/', views.group_create, name='group_create'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),

    # Tailwind CSS reload 
    # path("__reload__/", include("django_browser_reload.urls")),
]