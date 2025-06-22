from django.urls import path
from .views import (
    MealListView, FoodCreateView, MealEntryCreateView,
    MealEntryUpdateView, MealEntryDeleteView
)

urlpatterns = [
    path('', MealListView.as_view(), name='meal_list'),
    path('food/add/', FoodCreateView.as_view(), name='food_add'),
    path('meal/add/', MealEntryCreateView.as_view(), name='meal_add'),
    path('meal/<int:pk>/edit/', MealEntryUpdateView.as_view(), name='meal_edit'),
    path('meal/<int:pk>/delete/', MealEntryDeleteView.as_view(), name='meal_delete'),
]
