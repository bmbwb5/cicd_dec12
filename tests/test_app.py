import sys
from pathlib import Path
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


import app as a

def test_add():
    assert a.add(5, 6) == 11

def test_add2():
    assert a.add(5, 6) != 10

def test_add3():
    assert a.add("a", "b") == "Invalid parameter passed! Not a number"

def test_sub():
    assert a.sub(5, 6) == -1

def test_sub2():
    assert a.sub(5, 6) != 11

def test_sub3():
    assert a.sub("a", "b") == "Invalid parameter passed! Not a number"

def test_mult():
    assert a.mult(5, 6) == 30

def test_mult2():
    assert a.mult(-5, 6) == -30

def test_mult3():
    assert a.mult("a", "b") == "Invalid parameter passed! Not a number"

def test_div():
    assert a.div(10, 5) == 2

def test_div2():
    assert a.div(10, 0) == "Invalid: Divide by zero!"

def test_div3():
    assert a.div("a", "b") == "Invalid parameter passed! Not a number"

def test_log():
    assert a.log(1) == 0

def test_log2():
    assert a.log(0) == "Undefined!"

def test_log3():
    assert a.log("a") == "Invalid parameter passed! Not a number"

def test_square():
    assert a.square(1, 3) == 1

def test_square2():
    assert a.square(2) == 4

def test_square3():
    assert a.square("a") == "Invalid parameter passed! Not a number"

def test_sin():
    assert math.isclose(a.sin(0), 0)

def test_sin2():
    assert math.isclose(a.sin(math.radians(90)), 1)

def test_sin3():
    assert a.sin("a") == "Invalid parameter passed! Not a number"

def test_cos():
    assert math.isclose(a.cos(0), 1)

def test_cos2():
    assert math.isclose(a.cos(math.radians(90)), 0)

def test_cos3():
    assert a.cos("a") == "Invalid parameter passed! Not a number"

def test_square_root():
    assert a.square_root(4) == 2

def test_square_root2():
    assert a.square_root(-4) == "Domain Error!"

def test_square_root3():
    assert a.square_root("a") == "Invalid parameter passed! Not a number"

def test_percentage():
    assert a.percentage(1, 100) == 1

def test_percentage2():
    assert a.percentage(1, -10) == "Invalid: percentage is negative!"

def test_percentage3():
    assert a.percentage("a", "b") == "Invalid parameter passed! Not a number"
