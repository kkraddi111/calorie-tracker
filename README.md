🍛 South Indian Calorie Tracker

A beautifully designed Django application to track calories for South Indian cuisine. Keep track of your daily meals, snacks, and beverages while exploring the rich variety of South Indian food.

![Application Screenshot](screenshots/app-preview.png)

✨ Features

- 🎯 Track Daily Calories: Monitor your daily calorie intake with ease
- 🍚 Comprehensive Food Database: Includes a wide variety of South Indian dishes
  - Traditional meals (Idli, Dosa, etc.)
  - Regional specialties (Mysore Masala Dosa, Bisi Bele Bath)
  - Snacks (Bajji, Bonda, Mixture)
  - Beverages (Filter Coffee, Masala Tea)
- 📊 Categorized Food Items:
  - Breakfast Items
  - Rice Dishes
  - Rotis & Breads
  - Vegetable Dishes
  - Snacks & Beverages
  - Karnataka Specialties
  - Accompaniments
- 🎨 Modern UI/UX:
  - Intuitive meal entry system
  - Beautiful color scheme
  - Mobile-responsive design
- ⚡ Smart Features:
  - Real-time calorie calculations
  - Multiple food items per meal
  - Edit and update meals
  - Daily calorie summaries

🚀 Getting Started

Prerequisites
- Python 3.8+
- Django 5.0+
- pip

Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/south-indian-calorie-tracker.git
cd south-indian-calorie-tracker
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Add food database
```bash
python manage.py add_south_indian_foods
```

6. Start development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to start using the application.

📱 Usage

1. Add Food Items
   - Browse the existing food database
   - Add new food items with calorie information

2. Create Meals
   - Select multiple food items
   - Specify quantities
   - Choose meal type (Breakfast/Lunch/Dinner/Snack)

3. Track Progress
   - View daily calorie intake
   - Review meal history
   - Edit or delete meal entries

🎨 Color Scheme

The application uses a carefully chosen color palette:
- Primary: `#4A102A` (Deep Burgundy)
- Secondary: `#FE5D26` (Vibrant Orange)
- Gradients and hover effects for enhanced visual appeal

🌟 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

🙏 Acknowledgments

- All calorie information is sourced from reliable nutritional databases
- Icons provided by Bootstrap Icons
- Inspired by traditional South Indian cuisine

📸 Screenshots

 Home Page
![Home Page](screenshots/home.png)

 Add Meal
![Add Meal](screenshots/add-meal.png)

 Food Database
![Food Database](screenshots/food-database.png)

---
Made with ❤️ for South Indian cuisine enthusiasts
