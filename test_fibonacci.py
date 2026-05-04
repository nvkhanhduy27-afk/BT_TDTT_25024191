# test fibonacci function
from fibonacci import fib 
def test_first_two():
    assert fib(0) == 0
    assert fib(1) == 1
def test_small_numbers():
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
def test_large_number():
    assert fib(10) == 55

if __name__ == "__main__":
    test_first_two()
    print("First two tests passed!")
    test_small_numbers()
    print("Small numbers tests passed!")
    test_large_number()
    print("Large numbers test passed!")