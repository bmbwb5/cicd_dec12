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
    for i,o in ((("a", "b"), False), ((1, 2), True)):
        try:
            a.add(*i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_sub():
    assert a.sub(5, 6) == -1

def test_sub2():
    assert a.sub(5, 6) != 11

def test_sub3():
    for i,o in ((("a", "b"), False), ((1, 2), True)):
        try:
            a.sub(*i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_mult():
    assert a.mult(5, 6) == 30

def test_mult2():
    assert a.mult(-5, 6) == -30

def test_mult3():
    for i,o in ((("a", "b"), False), ((1, 2), True)):
        try:
            a.mult(*i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_div():
    assert a.div(10, 5) == 2

def test_div2():
    for i,o in (((10, 0), False), ((1, 2), True)):
        try:
            a.div(*i)
            ret = True
        except ZeroDivisionError:
            ret = False
        assert ret == o

def test_div3():
    for i,o in ((("a", "b"), False), ((1, 2), True)):
        try:
            a.div(*i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_log():
    assert a.log(1) == 0

def test_log2():
    for i,o in (((0), False), ((1), True)):
        try:
            a.log(i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_log3():
    for i,o in ((("a"), False), ((1), True)):
        try:
            a.log(i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_square():
    assert a.square(1, 3) == 1

def test_square2():
    assert a.square(2) == 4

def test_square3():
    for i,o in ((("a"), False), ((1), True)):
        try:
            a.square(i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_sin():
    assert math.isclose(a.sin(0), 0)

def test_sin2():
    assert math.isclose(a.sin(math.radians(90)), 1)

def test_sin3():
    for i,o in ((("a"), False), ((1), True)):
        try:
            a.sin(i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_cos():
    assert math.isclose(a.cos(0), 1)

def test_cos2():
    assert math.isclose(a.cos(math.radians(180)), -1)

def test_cos3():
    for i,o in ((("a"), False), ((1), True)):
        try:
            a.cos(i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_square_root():
    assert a.square_root(4) == 2

def test_square_root2():
    for i,o in (((-4), False), ((4), True)):
        try:
            a.square_root(i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_square_root3():
     for i,o in ((("a"), False), ((9), True)):
        try:
            a.square_root(i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_percentage():
    assert a.percentage(1, 100) == 1

def test_percentage2():
    for i,o in (((1, -10), False), ((1, 2), True)):
        try:
            a.percentage(*i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o

def test_percentage3():
    for i,o in ((("a", "b"), False), ((1, 2), True)):
        try:
            a.percentage(*i)
            ret = True
        except ValueError:
            ret = False
        assert ret == o
