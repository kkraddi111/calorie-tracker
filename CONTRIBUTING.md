# Contributing to South Indian Calorie Tracker

🙏 Thank you for considering contributing to the South Indian Calorie Tracker! Your help is valuable in making this tool better for everyone.

## 📝 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps to reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed and what behavior you expected to see
* Include screenshots if possible

### 💡 Suggesting Enhancements

If you have ideas for new features or improvements:

* Use a clear and descriptive title
* Provide a detailed description of the suggested enhancement
* Explain why this enhancement would be useful
* Include mockups or examples if applicable

### 🔧 Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Write a good commit message

## 🎨 Style Guidelines

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Python Style Guide

* Follow PEP 8
* Use meaningful variable names
* Add docstrings to functions and classes
* Comment complex logic

### Django Best Practices

* Keep views focused and simple
* Use class-based views when appropriate
* Leverage Django's built-in features
* Keep models well-organized and documented

## 📊 Adding New Food Items

When adding new food items to the database:

1. Research accurate calorie information
2. Include proper serving sizes
3. Use consistent units
4. Add to appropriate categories
5. Document the source of calorie information

### Food Item Template:
```python
{
    'name': 'Food Name',
    'calories_per_unit': 000,
    'unit': 'pieces/cups/grams'
}
```

## 🌟 Recognition

Contributors will be added to the README.md file. Major contributors may be invited to become maintainers.

## ❓ Questions?

Feel free to create an issue with the "question" label if you need help.

---
Thank you for making South Indian Calorie Tracker better! 🙏
