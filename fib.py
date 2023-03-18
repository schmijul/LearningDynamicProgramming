#!/usr/bin/python




"""
Task:
        Write a funciton 'fib(n)' that takes in a number as an argument.
        The function should return the -th number of the Fibonnaci Sequenz
        The first and second number of the sequence is 1.
                    
        To generate the net number of the sequence one must sum the prevoius two
"""









from visualiser.visualiser import Visualiser as vs


@vs(node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def simple_fib(n): 
    """
    This function is a simple Fibonacci implementation using recursion.
    It will wrk very quick for a low n, however if n is very high the number of calculations is so high that the programm will become ve    ry slow
    """
    if n <= 1: return n 
    return simple_fib(n - 1) + simple_fib(n - 2) 


def main():
    # Call function
    print(simple_fib(n=N))
    # Save recursion tree to a file
    vs.make_animation("fibonacci.gif", delay=2)


if __name__ == "__main__":
    N = 4
    main()
