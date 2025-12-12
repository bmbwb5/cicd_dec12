import math
import random

def add (a, b):
    if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
        return "Invalid parameter passed! Not a number"
    return a+b

def sub (a, b):
    if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
        return "Invalid parameter passed! Not a number"
    return a-b

def mult (a, b):
    if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
        return "Invalid parameter passed! Not a number"
    return a*b

def div (a, b):
    if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
        return "Invalid parameter passed! Not a number"
    try:
        x = a/b
        return x
    except ZeroDivisionError:
        return "Invalid: Divide by zero!"

# Advanced Operations
def log (a):
    if not isinstance(a, (int, float)):
        return "Invalid parameter passed! Not a number"
    if a == 0:
        return "Undefined!"
    return math.log(a)

def square (a, b=2):
    if (not isinstance(a, (int, float))) or (not isinstance(b, (int, float))):
        return "Invalid parameter passed! Not a number"
    return a**b

def sin (a):
    if not isinstance(a, (int, float)):
        return "Invalid parameter passed! Not a number"
    return math.sin(a)

def cos (a):
    if not isinstance(a, (int, float)):
        return "Invalid parameter passed! Not a number"
    return math.cos(a)

def square_root (a):
    if not isinstance(a, (int, float)):
        return "Invalid parameter passed! Not a number"
    if a < 0:
        return "Domain Error!"
    return math.sqrt(a)

def percentage(num, percent):
    if (not isinstance(num, (int, float))) or (not isinstance(percent, (int, float))):
        return "Invalid parameter passed! Not a number"
    if percent < 0:
        return "Invalid: percentage is negative!"
    return num*(percent/100)
