from django.db import models
from django.utils import timezone

class Food(models.Model):
    COMMON_UNITS = [
        ('grams', 'Grams'),
        ('pieces', 'Pieces'),
        ('cups', 'Cups'),
        ('ml', 'Milliliters'),
        ('servings', 'Servings'),
        ('tablespoons', 'Tablespoons'),
        ('teaspoons', 'Teaspoons'),
    ]

    name = models.CharField(max_length=200, help_text="Enter the name of the food item")
    calories_per_unit = models.FloatField(help_text="Enter the calories per unit of measurement")
    unit = models.CharField(max_length=50, choices=COMMON_UNITS, default='grams', help_text="Select the unit of measurement")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories_per_unit} calories per {self.get_unit_display()})"

class MealEntry(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    meal_type = models.CharField(
        max_length=20, 
        choices=MEAL_TYPES,
        help_text="Select when this meal was consumed"
    )
    date = models.DateField(
        default=timezone.now,
        help_text="Select the date when this meal was consumed"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.get_meal_type_display()} on {self.date}"

    @property
    def total_calories(self):
        return sum(item.total_calories for item in self.mealitem_set.all())

class MealItem(models.Model):
    meal = models.ForeignKey(MealEntry, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField(help_text="Enter the quantity in the selected unit")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} {self.food.unit} of {self.food.name}"

    @property
    def total_calories(self):
        return self.quantity * self.food.calories_per_unit
