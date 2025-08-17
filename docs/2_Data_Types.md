# Python Data Types Overview

## Simple Types

- `int` - integers: 5, 0, -32
- `float` - floating-point numbers: 3.14, -0.5
- `complex` - complex numbers: 3+4j
- `bool` - True or False
- `NoneType` - absence of a value: None
- `str` - string of characters: "hello"

## Sequence Types

- `list` - mutable sequence: [1, 2, 3]
- `tuple` - immutable sequence: (1, 2, 3)
- `range` - sequence of numbers: range(5) -> 0, 1, 2, 3, 4

## Collection Types

- `set` - unordered collection of unique elements: {1, 2, 3}
- `frozenset` - immutable set: frozenset({1, 2, 3})
- `dict` - key-value pairs: {"key": "value"}

## Binary Types

- `bytes` - immutable sequence of bytes
- `bytearray` - mutable sequence of bytes
- `memoryview` - view of a memory buffer

## Dynamic Typing

- Variables can change type at any time:

```python
x = 10      # int
x = "ten"  # now str
```

- Python is dynamically typed; type declarations are optional.

## Type Hints

- Optional annotations to indicate expected types:

```python
age: int = 25
name: str = "Oleh"
```

- Useful for documentation, IDE autocompletion, and static analysis.

## Static Type Checking with mypy

- `mypy` is a static type checker for Python.
- It analyzes type hints **before runtime** and shows warnings if types mismatch.
- `mypy` does **not prevent code execution**:

```python
age: int = 25
age = "Hello"  # Python runs, mypy warns
```

- Helps catch type errors early in development.

---
