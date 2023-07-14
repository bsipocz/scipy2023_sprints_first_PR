from pr_tutorial.simple_functions import factorial
from pr_tutorial.buggy_function import angle_to_sexigesimal


def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_angle_to_sexigesimal():
    """Simplest test for one case"""

    assert angle_to_sexigesimal(90) == '6:0:0.000'
