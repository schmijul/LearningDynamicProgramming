#!/usr/bin/python
"""
Task:
    Write a funciton 'fib(n)' that takes in a number as an argument.
    The function should return the -th number of the Fibonnaci Sequenz

    The first and second number of the sequence is 1.
    
    To generate the net number of the sequence one must sum the prevoius two
"""




def simple_fib(n):
   
    if (n <= 2):return 1 

    else: return fib(n-1) + fib(n-2)



if __name__ == "__main__":


