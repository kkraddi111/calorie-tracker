from django.core.management.base import BaseCommand
from tracker.models import Food

class Command(BaseCommand):
    help = 'Adds common South Indian foods to the database'

    def handle(self, *args, **kwargs):
        south_indian_foods = [
            # Rotis and Breads
            {
                'name': 'Jowar Roti',
                'calories_per_unit': 120,
                'unit': 'pieces'
            },
            {
                'name': 'Bajra Roti',
                'calories_per_unit': 130,
                'unit': 'pieces'
            },
            {
                'name': 'Multi-grain Roti',
                'calories_per_unit': 110,
                'unit': 'pieces'
            },
            # Vegetable Dishes
            {
                'name': 'Beans Palya',
                'calories_per_unit': 85,
                'unit': 'cups'
            },
            {
                'name': 'Carrot Palya',
                'calories_per_unit': 70,
                'unit': 'cups'
            },
            {
                'name': 'Cabbage Palya',
                'calories_per_unit': 65,
                'unit': 'cups'
            },
            {
                'name': 'Mixed Vegetable Palya',
                'calories_per_unit': 90,
                'unit': 'cups'
            },
            {
                'name': 'Beetroot Palya',
                'calories_per_unit': 75,
                'unit': 'cups'
            },
            {
                'name': 'Green Beans Curry',
                'calories_per_unit': 95,
                'unit': 'cups'
            },
            {
                'name': 'Brinjal Curry',
                'calories_per_unit': 85,
                'unit': 'cups'
            },
            # Karnataka Foods
            {
                'name': 'Mysore Masala Dosa',
                'calories_per_unit': 270,
                'unit': 'pieces'
            },
            {
                'name': 'Bisi Bele Bath',
                'calories_per_unit': 245,
                'unit': 'cups'
            },
            {
                'name': 'Ragi Mudde',
                'calories_per_unit': 150,
                'unit': 'pieces'
            },
            {
                'name': 'Neer Dosa',
                'calories_per_unit': 110,
                'unit': 'pieces'
            },
            {
                'name': 'Akki Roti',
                'calories_per_unit': 180,
                'unit': 'pieces'
            },
            {
                'name': 'Ragi Roti',
                'calories_per_unit': 160,
                'unit': 'pieces'
            },
            {
                'name': 'Kesari Bath',
                'calories_per_unit': 290,
                'unit': 'cups'
            },
            {
                'name': 'Khara Bath (Upma)',
                'calories_per_unit': 230,
                'unit': 'cups'
            },
            {
                'name': 'Mangalore Buns',
                'calories_per_unit': 195,
                'unit': 'pieces'
            },
            {
                'name': 'Saagu',
                'calories_per_unit': 120,
                'unit': 'cups'
            },
            # Snacks
            {
                'name': 'Onion Bajji',
                'calories_per_unit': 120,
                'unit': 'pieces'
            },
            {
                'name': 'Chilli Bajji',
                'calories_per_unit': 85,
                'unit': 'pieces'
            },
            {
                'name': 'Potato Bajji',
                'calories_per_unit': 145,
                'unit': 'pieces'
            },
            {
                'name': 'Bonda',
                'calories_per_unit': 130,
                'unit': 'pieces'
            },
            {
                'name': 'Masala Vada',
                'calories_per_unit': 115,
                'unit': 'pieces'
            },
            {
                'name': 'Mixture (Snack)',
                'calories_per_unit': 160,
                'unit': 'cups'
            },
            {
                'name': 'Murukku',
                'calories_per_unit': 95,
                'unit': 'pieces'
            },
            # Beverages
            {
                'name': 'Filter Coffee',
                'calories_per_unit': 120,
                'unit': 'cups'
            },
            {
                'name': 'Masala Tea',
                'calories_per_unit': 60,
                'unit': 'cups'
            },
            {
                'name': 'Plain Tea',
                'calories_per_unit': 40,
                'unit': 'cups'
            },
            {
                'name': 'Coffee with Milk',
                'calories_per_unit': 100,
                'unit': 'cups'
            },
            {
                'name': 'Plain Milk',
                'calories_per_unit': 150,
                'unit': 'cups'
            },
            {
                'name': 'Buttermilk',
                'calories_per_unit': 40,
                'unit': 'cups'
            },
            {
                'name': 'Sweet Lassi',
                'calories_per_unit': 180,
                'unit': 'cups'
            },
            # Other South Indian Foods
            {
                'name': 'Idli',
                'calories_per_unit': 39,
                'unit': 'pieces'
            },
            {
                'name': 'Dosa',
                'calories_per_unit': 133,
                'unit': 'pieces'
            },
            {
                'name': 'Sambar',
                'calories_per_unit': 65,
                'unit': 'cups'
            },
            {
                'name': 'Coconut Chutney',
                'calories_per_unit': 40,
                'unit': 'tablespoons'
            },
            {
                'name': 'Upma',
                'calories_per_unit': 85,
                'unit': 'cups'
            },
            {
                'name': 'Uttapam',
                'calories_per_unit': 160,
                'unit': 'pieces'
            },
            {
                'name': 'Rice (Cooked)',
                'calories_per_unit': 130,
                'unit': 'cups'
            },
            {
                'name': 'Rasam',
                'calories_per_unit': 35,
                'unit': 'cups'
            },
            {
                'name': 'Vada',
                'calories_per_unit': 97,
                'unit': 'pieces'
            },
            {
                'name': 'Pongal',
                'calories_per_unit': 150,
                'unit': 'cups'
            },
            {
                'name': 'Curd Rice',
                'calories_per_unit': 166,
                'unit': 'cups'
            },
            {
                'name': 'Lemon Rice',
                'calories_per_unit': 185,
                'unit': 'cups'
            },
            {
                'name': 'Coconut Rice',
                'calories_per_unit': 200,
                'unit': 'cups'
            },
            {
                'name': 'Tomato Rice',
                'calories_per_unit': 180,
                'unit': 'cups'
            },
            {
                'name': 'Tamarind Rice',
                'calories_per_unit': 190,
                'unit': 'cups'
            },
            {
                'name': 'Appam',
                'calories_per_unit': 105,
                'unit': 'pieces'
            },
            {
                'name': 'Paruppu (Dal)',
                'calories_per_unit': 120,
                'unit': 'cups'
            }
        ]

        for food_data in south_indian_foods:
            food, created = Food.objects.get_or_create(
                name=food_data['name'],
                defaults={
                    'calories_per_unit': food_data['calories_per_unit'],
                    'unit': food_data['unit']
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added {food.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'{food.name} already exists')
                )
