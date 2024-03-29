"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""
def fibonacci(i):
    if i == 1:
        return 1
    elif i == 2:
        return 2
    elif i >= 3:
        return fibonacci(i-1) + fibonacci(i-2)


def sum_of_fibonacci(lim):
    i = 1
    ret = 0
    while (f:=fibonacci(i)) < lim:
        if f%2 == 0:
            ret += f
        i += 1
    print(ret)


if __name__ == "__main__":
    sum_of_fibonacci(4000000)
