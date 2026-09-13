*This project was created as part of the 42 curriculum by lhaydar*

# FuncMage

## Description
An introduction to functional programming in Python, split into five exercises:

| Exercise | File | Topic |
|----------|------|-------|
| ex0 | `lambda_spells.py` | Lambdas with `sorted`, `filter`, `map`, `min`, `max` |
| ex1 | `higher_magic.py` | Higher-order functions (combine, amplify, condition, sequence spells) |
| ex2 | `scope_mysteries.py` | Closures and lexical scoping with `nonlocal` |
| ex3 | `functools_artifacts.py` | `reduce`, `partial`, `lru_cache`, `singledispatch` |
| ex4 | `decorator_mastery.py` | Decorators, decorator factories, `wraps`, `@staticmethod` |

## Instructions
Requires Python 3.10+. No external libraries.

```sh
python3 ex0/lambda_spells.py
python3 ex1/higher_magic.py
python3 ex2/scope_mysteries.py
python3 ex3/functools_artifacts.py
python3 ex4/decorator_mastery.py
```

Code checks:

```sh
flake8 .
mypy --strict .
```

## Resources
- [Medium article about lambda functions](https://medium.com/data-science/understanding-the-use-of-lambda-expressions-map-and-filter-in-python-5e03e4b18d09)
- [Syntax from GeeksforGeeks: lambda ](https://www.geeksforgeeks.org/python/python-lambda-anonymous-functions-filter-map-reduce/)
- [Higher Order Functions: GeeksforGeeks](https://www.geeksforgeeks.org/python/higher-order-functions-in-python/)
- [Scopes and Closures in Python: Medium article](https://medium.com/@dannymcwaves/a-python-tutorial-to-understanding-scopes-and-closures-c6a3d3ba0937)
- [Functools in python](https://www.geeksforgeeks.org/python/functools-module-in-python/)

### AI usage
AI (Claude) was used to fix mypy type-hint errors and to draft this README.
