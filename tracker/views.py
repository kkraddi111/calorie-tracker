from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db import transaction
from .models import Food, MealEntry, MealItem
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Sum, F, Prefetch
import json
from django.core.serializers.json import DjangoJSONEncoder

class MealListView(ListView):
    model = MealEntry
    template_name = 'tracker/meal_list.html'
    context_object_name = 'meals'

    def get_queryset(self):
        return MealEntry.objects.prefetch_related(
            Prefetch('mealitem_set', queryset=MealItem.objects.select_related('food'))
        ).order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        today_meals = MealEntry.objects.filter(date=today).prefetch_related(
            Prefetch('mealitem_set', queryset=MealItem.objects.select_related('food'))
        )
        context['total_calories'] = sum(meal.total_calories for meal in today_meals)
        return context

class FoodCreateView(CreateView):
    model = Food
    template_name = 'tracker/food_form.html'
    fields = ['name', 'calories_per_unit', 'unit']
    success_url = reverse_lazy('meal_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foods = Food.objects.all().order_by('name')
        
        # Categorize foods
        categories = {
            'rotis_and_breads': ['Jowar Roti', 'Bajra Roti', 'Multi-grain Roti', 'Akki Roti', 'Ragi Roti'],
            'vegetable_dishes': ['Beans Palya', 'Carrot Palya', 'Cabbage Palya', 'Mixed Vegetable Palya', 
                               'Beetroot Palya', 'Green Beans Curry', 'Brinjal Curry', 'Saagu'],
            'karnataka_specialties': ['Mysore Masala Dosa', 'Bisi Bele Bath', 'Ragi Mudde', 'Neer Dosa', 
                                    'Kesari Bath', 'Khara Bath', 'Mangalore Buns'],
            'rice_dishes': ['Rice (Cooked)', 'Curd Rice', 'Lemon Rice', 'Coconut Rice', 'Tomato Rice', 'Tamarind Rice'],
            'breakfast_items': ['Idli', 'Dosa', 'Uttapam', 'Vada', 'Rava Idli', 'Medu Vada', 'Pongal', 'Upma'],
            'snacks_and_beverages': ['Onion Bajji', 'Chilli Bajji', 'Potato Bajji', 'Bonda', 'Masala Vada', 
                                   'Mixture', 'Murukku', 'Filter Coffee', 'Tea', 'Milk', 'Lassi', 'Buttermilk'],
            'accompaniments': ['Sambar', 'Coconut Chutney', 'Rasam', 'Paruppu (Dal)']
        }
        
        categorized_foods = {
            'Rotis & Breads': [],
            'Vegetable Dishes': [],
            'Karnataka Specialties': [],
            'Rice Dishes': [],
            'Breakfast Items': [],
            'Snacks & Beverages': [],
            'Accompaniments': [],
            'Others': []
        }

        for food in foods:
            categorized = False
            for cat_key, cat_foods in categories.items():
                if any(cat_food.lower() in food.name.lower() for cat_food in cat_foods):
                    if cat_key == 'rotis_and_breads':
                        categorized_foods['Rotis & Breads'].append(food)
                    elif cat_key == 'vegetable_dishes':
                        categorized_foods['Vegetable Dishes'].append(food)
                    elif cat_key == 'karnataka_specialties':
                        categorized_foods['Karnataka Specialties'].append(food)
                    elif cat_key == 'rice_dishes':
                        categorized_foods['Rice Dishes'].append(food)
                    elif cat_key == 'breakfast_items':
                        categorized_foods['Breakfast Items'].append(food)
                    elif cat_key == 'snacks_and_beverages':
                        categorized_foods['Snacks & Beverages'].append(food)
                    elif cat_key == 'accompaniments':
                        categorized_foods['Accompaniments'].append(food)
                    categorized = True
                    break
            if not categorized:
                categorized_foods['Others'].append(food)

        context['categorized_foods'] = {k: v for k, v in categorized_foods.items() if v}
        return context

class MealEntryCreateView(CreateView):
    model = MealEntry
    template_name = 'tracker/meal_form.html'
    fields = ['meal_type', 'date']
    success_url = reverse_lazy('meal_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foods = Food.objects.all().order_by('name')
        
        # Create list of tuples for the food choices
        food_choices = [
            (food.id, f"{food.name} ({food.calories_per_unit} calories/{food.get_unit_display()})")
            for food in foods
        ]
        context['food_choices'] = json.dumps(food_choices, cls=DjangoJSONEncoder)

        # Group foods by category for reference
        categories = {
            'breakfast_items': [
                'Idli', 'Dosa', 'Pongal', 'Upma', 'Vada',
                'Rava Idli', 'Mysore Masala Dosa', 'Uttapam'
            ],
            'rice_dishes': [
                'Rice', 'Curd Rice', 'Lemon Rice', 'Tomato Rice',
                'Coconut Rice', 'Bisi Bele Bath', 'Tamarind Rice'
            ],
            'rotis_and_breads': [
                'Roti', 'Jowar Roti', 'Ragi Roti', 'Akki Roti',
                'Bajra Roti', 'Multi-grain Roti'
            ],
            'snacks_and_beverages': [
                'Bajji', 'Bonda', 'Vada', 'Mixture', 'Murukku',
                'Coffee', 'Tea', 'Milk', 'Lassi', 'Buttermilk'
            ],
            'curries_and_palyas': [
                'Beans Palya', 'Carrot Palya', 'Cabbage Palya',
                'Mixed Vegetable', 'Beetroot', 'Brinjal',
                'Green Beans', 'Curry'
            ],
            'accompaniments': [
                'Sambar', 'Rasam', 'Chutney', 'Saagu',
                'Coconut Chutney', 'Paruppu'
            ],
            'specialties': [
                'Ragi Mudde', 'Kesari Bath', 'Khara Bath',
                'Mangalore Buns', 'Neer Dosa'
            ]
        }
        
        # Add JSON-encoded categories to the context
        context['food_categories'] = json.dumps(categories, cls=DjangoJSONEncoder)
        return context

    def form_valid(self, form):
        with transaction.atomic():
            # Save the meal entry
            self.object = form.save()
            
            # Process multiple food items
            post_data = self.request.POST
            food_items = []
            index = 1
            
            while True:
                food_key = f'food_{index}'
                quantity_key = f'quantity_{index}'
                
                if food_key not in post_data:
                    break
                    
                food_id = post_data.get(food_key)
                quantity = post_data.get(quantity_key)
                
                if food_id and quantity:
                    try:
                        food = Food.objects.get(id=food_id)
                        MealItem.objects.create(
                            meal=self.object,
                            food=food,
                            quantity=float(quantity)
                        )
                    except (Food.DoesNotExist, ValueError):
                        pass
                
                index += 1
            
            return redirect(self.success_url)

class MealEntryUpdateView(UpdateView):
    model = MealEntry
    template_name = 'tracker/meal_form.html'
    fields = ['meal_type', 'date']
    success_url = reverse_lazy('meal_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foods = Food.objects.all().order_by('name')
        food_choices = [
            (food.id, f"{food.name} ({food.calories_per_unit} calories/{food.get_unit_display()})")
            for food in foods
        ]
        context['food_choices'] = json.dumps(food_choices, cls=DjangoJSONEncoder)

        # Define categories for food items
        categories = {
            'breakfast_items': [
                'Idli', 'Dosa', 'Pongal', 'Upma', 'Vada',
                'Rava Idli', 'Mysore Masala Dosa', 'Uttapam'
            ],
            'rice_dishes': [
                'Rice', 'Curd Rice', 'Lemon Rice', 'Tomato Rice',
                'Coconut Rice', 'Bisi Bele Bath', 'Tamarind Rice'
            ],
            'rotis_and_breads': [
                'Roti', 'Jowar Roti', 'Ragi Roti', 'Akki Roti',
                'Bajra Roti', 'Multi-grain Roti'
            ],
            'snacks_and_beverages': [
                'Onion Bajji', 'Chilli Bajji', 'Potato Bajji', 'Bonda',
                'Masala Vada', 'Mixture', 'Murukku', 'Filter Coffee',
                'Tea', 'Milk', 'Lassi', 'Buttermilk'
            ],
            'curries_and_palyas': [
                'Beans Palya', 'Carrot Palya', 'Cabbage Palya',
                'Mixed Vegetable', 'Beetroot', 'Brinjal',
                'Green Beans', 'Curry'
            ],
            'accompaniments': [
                'Sambar', 'Rasam', 'Chutney', 'Saagu',
                'Coconut Chutney', 'Paruppu'
            ],
            'specialties': [
                'Ragi Mudde', 'Kesari Bath', 'Khara Bath',
                'Mangalore Buns', 'Neer Dosa'
            ]
        }
        
        context['food_categories'] = json.dumps(categories, cls=DjangoJSONEncoder)
        context['existing_items'] = self.object.mealitem_set.select_related('food')
        context['is_update'] = True
        return context

    def form_valid(self, form):
        with transaction.atomic():
            # Delete existing meal items
            self.object.mealitem_set.all().delete()
            
            # Save the updated meal entry
            response = super().form_valid(form)
            
            # Process multiple food items
            post_data = self.request.POST
            index = 1
            
            while True:
                food_key = f'food_{index}'
                quantity_key = f'quantity_{index}'
                
                if food_key not in post_data:
                    break
                    
                food_id = post_data.get(food_key)
                quantity = post_data.get(quantity_key)
                
                if food_id and quantity:
                    try:
                        food = Food.objects.get(id=food_id)
                        MealItem.objects.create(
                            meal=self.object,
                            food=food,
                            quantity=float(quantity)
                        )
                    except (Food.DoesNotExist, ValueError):
                        pass
                
                index += 1
            
            messages.success(self.request, 'Meal updated successfully!')
            return response

class MealEntryDeleteView(DeleteView):
    model = MealEntry
    success_url = reverse_lazy('meal_list')
    template_name = 'tracker/meal_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Meal deleted successfully!')
        return super().delete(request, *args, **kwargs)
