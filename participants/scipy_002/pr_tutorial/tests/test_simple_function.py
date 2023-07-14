from pr_tutorial.simple_functions import factorial, is_prime

def test_factorial_3():
    """Simplest test for one crete case"""

    assert factorial(3) == 6

def test_is_prime():
    """Simple test for naive is_prime() function."""
    primes_below_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
                        41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 
                        89, 97]
    
    for num in range(1, 100):
        if num == 1:
            try:
                is_prime(num)
            except ValueError as e:
                continue
            except Exception as e: # wrong exception raised
                assert False
            assert False
        else:
            primeOrNot = is_prime(num)

            if num in primes_below_100:
                assert primeOrNot is True
            else:
                assert primeOrNot is False       