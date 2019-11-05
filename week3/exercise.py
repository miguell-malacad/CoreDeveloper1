#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----


def fizzbuzz(n: int) -> str:
    """
            Given an int >= 0, returns the following:
            "fizz" if n is divisible by 3
            "buzz" if n is divisible by 5
            "fizzbuzz" if n is divisible by both 3 and 5
            str(n) if n does not meet any other test cases
    """
    output = str(n)
    if (n % 3 == 0) and (n % 5 == 0):
        output = "fizzbuzz"
    elif n % 3 == 0:
        output = "fizz"
    elif n % 5 == 0:
        output = "buzz"
    return output
# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----


# -----END PAYROLL CODE-----
