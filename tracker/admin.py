from django.contrib import admin
from .models import Food, MealEntry, MealItem

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories_per_unit', 'unit')
    search_fields = ('name',)
    list_filter = ('unit',)

@admin.register(MealEntry)
class MealEntryAdmin(admin.ModelAdmin):
    list_display = ('meal_type', 'date', 'total_calories')
    list_filter = ('meal_type', 'date')

@admin.register(MealItem)
class MealItemAdmin(admin.ModelAdmin):
    list_display = ('meal', 'food', 'quantity', 'total_calories')
    list_filter = ('meal__meal_type', 'food')
    search_fields = ('food__name',)
