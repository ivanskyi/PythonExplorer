# Python Naming Conventions

## 1. Variables - `snake_case`
```python
user_name = "Oleh"
total_sum = 100
is_student = True
```

## 2. Constants - `UPPER_CASE`
```python
PI = 3.14159
MAX_USERS = 100
DEFAULT_TIMEOUT = 30
```

## 3. Functions / Methods - `snake_case`
```python
def calculate_sum(a, b):
    return a + b

def get_user_name():
    return "Oleh"

def print_report():
    print("Report generated")
```

## 4. Classes / Interfaces - `PascalCase`
```python
class Car:
    pass

class ElectricCar(Car):
    pass

class UserProfile:
    pass
```

## 5. Packages / Modules - `lowercase` or `snake_case`
```
my_project/
data_utils.py
file_reader.py
```

## 6. Private Variables - `_single_leading_underscore` or `__double_leading_underscore`
```python
class Car:
    def __init__(self):
        self._speed = 0
        self.__engine_type = "V8"
        self._fuel_level = 100
```

## 7. Static Methods / Variables
- Constants: `UPPER_CASE`
- Static Methods: `snake_case`
```python
class MathUtils:
    PI = 3.14159
    MAX_ITERATIONS = 1000

    @staticmethod
    def calculate_area(radius):
        return MathUtils.PI * radius * radius
```
