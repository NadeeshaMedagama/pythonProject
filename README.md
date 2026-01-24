# Python Learning Project

A comprehensive Python learning project demonstrating fundamental programming concepts including object-oriented programming, control structures, loops, and module imports.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Modules Description](#modules-description)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project is a collection of Python scripts designed to demonstrate various programming concepts and best practices. It includes examples of:
- Object-Oriented Programming (OOP)
- Control flow statements
- Loops and iterations
- User input handling
- Module imports and organization
- Time and random library usage

## ✨ Features

- **Car Class Implementation**: Demonstrates OOP principles with a Car class including attributes and methods
- **Control Structures**: Examples of if-else statements and conditional logic
- **Loop Demonstrations**: For loops, while loops, and nested loops
- **User Interaction**: Input validation and user-friendly prompts
- **Pattern Generation**: Symbol-based pattern printing
- **Countdown Timer**: Practical time module usage
- **Modular Design**: Clean separation of concerns across multiple files

## 📁 Project Structure

```
pythonProject/
├── Basic.py          # Basic Python demonstrations and imports
├── Basic02.py        # Advanced examples with control structures and loops
├── car.py            # Car class definition with OOP concepts
├── test.py           # Utility functions for testing
└── README.md         # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Git (for cloning the repository)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/NadeeshaMedagama/pythonProject.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pythonProject
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## 💻 Usage

### Running Basic Examples

```bash
python Basic.py
```

This will execute basic Python demonstrations including:
- Hello World output
- Range function usage with custom steps

### Running Advanced Examples

```bash
python Basic02.py
```

This interactive script will prompt you for:
- Temperature input (to determine weather conditions)
- Name input (with validation)
- Age input (to categorize age groups)
- Pattern dimensions and symbols

### Using the Car Class

```python
from car import Car

# Create a car instance
my_car = Car("Sedan", "Toyota Camry", 2024, "Blue")

# Use car methods
my_car.drive()  # Output: This Sedan is driving
my_car.stop()   # Output: This Toyota Camry is stopping
```

### Using Test Module Functions

```python
import test

test.hi()      # Output: Hello man!
test.hello()   # Prompts for name and greets
```

## 📚 Modules Description

### Basic.py
Entry point demonstrating:
- Module imports
- Basic print statements
- Range function with step parameter

### Basic02.py
Comprehensive examples including:
- Temperature-based conditionals
- Name input validation using while loops
- Age categorization logic
- String iteration
- Countdown timer implementation
- Pattern generation with nested loops

### car.py
Object-oriented programming demonstration:
- Car class with attributes (type, model, year, color)
- Class variable (wheels)
- Instance methods (drive, stop)
- Constructor implementation

### test.py
Utility module containing:
- `hi()`: Simple greeting function
- `hello()`: Interactive name-based greeting

## 📦 Requirements

Standard Python libraries used:
- `time` - For countdown and delay functions
- `random` - For random number generation
- `os` - For operating system interactions

No external packages required. All dependencies are part of Python's standard library.

## 🎓 Learning Outcomes

By studying this project, you will learn:

1. **Python Basics**
   - Variables and data types
   - Input/output operations
   - String manipulation

2. **Control Flow**
   - If-elif-else statements
   - Complex conditional logic
   - Boolean operators

3. **Loops**
   - For loops with range
   - While loops with conditions
   - Nested loop structures
   - Loop control with break/continue

4. **Functions**
   - Function definition and calling
   - Parameters and return values
   - Module organization

5. **Object-Oriented Programming**
   - Class definition
   - Constructors (__init__)
   - Instance variables
   - Class variables
   - Methods

6. **Modules**
   - Importing modules
   - Creating custom modules
   - Using `as` keyword for aliases

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 👥 Authors

- **Nadeesha Medagama** - Initial work

## 🙏 Acknowledgments

- Python community for excellent documentation
- Contributors who help improve this learning resource

---

**Note**: This project is designed for educational purposes to help beginners understand Python programming concepts. Feel free to experiment and modify the code to enhance your learning experience!
