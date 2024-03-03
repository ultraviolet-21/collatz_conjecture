#collatz_conjecture.py

import contextlib
import io

def run_conjecture(n: int):
    while n != 1:
        if (n%2 == 0):
            n = n//2
        else:
            n = 3*n+1
        print(n)

def test_conjecture(n: int):
    with contextlib.redirect_stdout(io.StringIO()) as output:
        run_conjecture(n)

    if output.getvalue().endswith('1\n'):
        return True
    
    return False

def run_tests():
    for x in range(2, 100):
        truth = test_conjecture(x)
        if truth == False:
            return False


if __name__ == '__main__':
    n = int(input())
    print(test_conjecture(n))
