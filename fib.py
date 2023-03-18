#!/usr/bin/python

import numpy as np






from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def simple_fib(n): 
    """
    This function is a simple Fibonacci implementation using recursion.
    It will wrk very quick for a low n, however if n is very high the number of calculations is so high that the programm will become ve    ry slow


    This implementation is O(n) in both space and time complexity
    """
    if (n <= 1): return n 
    return simple_fib(n - 1) + simple_fib(n - 2)






@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def dynamic_fib(n):
    a = [0] * (n + 1)
    a[0] = 0
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i-1] + a[i-2]
    return a[n]


def main():
    # Call function
    print(simple_fib(n=N))
    # Save recursion tree to a file
    vs.make_animation("fibonacci.gif", delay=2)


if __name__ == "__main__":
    N = 4
    main()
