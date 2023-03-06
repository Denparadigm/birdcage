"""
Lambda calculus is a formal system developed in the 1930s by Alonzo Church to investigate the foundations of
mathematics and computability. It is a system for representing and manipulating functions, and it has become an
important tool in the study of theoretical computer science and programming language theory.

The lambda calculus is based on the idea of using anonymous functions, which are functions that do not have a name.
Instead of naming a function and defining it explicitly, a lambda expression defines a function by specifying its
inputs and outputs. A lambda expression has the form "λx.e", where "x" is a variable and "e" is an expression that
uses "x".

Lambda calculus provides a way to formally define and reason about computations and the behavior of functions. It is
used in the design of programming languages and in the development of algorithms for various computational problems.
The lambda calculus is also the basis of functional programming, a programming paradigm that emphasizes the use of
functions as the primary means of computation.
"""

# Lots of birds #

"""
Idiot Bird (Id function):
The Idiot Bird, or Identity function, is a lambda function that takes an argument and returns it unchanged.
In lambda calculus notation: \a.a
"""
I = lambda a: a

"""
Kestrel (K function):
The Kestrel, or K function, is a lambda function that takes two arguments and returns the first argument unchanged. 
In lambda calculus notation: \ab.a
"""
K = lambda a: lambda b: a
T = lambda a: lambda b: a

"""
Kite (KI function):
The Kite, or KI function, is a lambda function that takes two arguments and returns the second argument unchanged. 
In lambda calculus notation: \ab.b
"""
KI = lambda a: lambda b: b
F = lambda a: lambda b: b

"""
Mockingbird (M function):
The Mockingbird, or M function, is a lambda function that takes an argument and applies itself to that argument, 
returning the result. This creates an infinite loop and is used to demonstrate recursion in lambda calculus. 
In lambda calculus notation: M := \f.ff
"""
M = lambda a: a(a)

"""
Cardinal (C function):
The Cardinal, or C function, is a lambda function that takes a function with two arguments and returns a new function 
that has the same functionality, but with the order of the arguments reversed. 
In lambda calculus notation: \f.\a.\b.f b a
"""
C = lambda f: lambda a: lambda b: f(b)(a)

"""
Bluebird (B function):
The Bluebird, or B function, is a lambda function that takes two functions f and g as input and returns a new function 
that applies the function g to its argument x, and then applies the function f to the result. In lambda calculus notation: 
\fgx.f (g x)
"""
B = lambda f: lambda g: lambda x: f(g(x))

# Logic

"""
NOT function:
The NOT function takes a boolean value (either True or False) and returns the opposite boolean value.
"""
not_func = lambda a: a(False)(True)

"""
AND function:
The AND function takes two boolean values as input and returns True if both inputs are True, and False otherwise.
"""
and_func = lambda a: lambda b: a(b)(a)

# Arithmetic

"""
Convert an integer to and from a Church numeral:
These functions takes a non-negative integer or church numeral as input and returns the corresponding numeral.
"""

def church_numeral(n):
    if n == 0:
        return lambda f: lambda x: x
    else:
        return lambda f: lambda x: f(church_numeral(n-1)(f)(x))

def numeral(n):
    """
    Convert a Church numeral to an integer.
    """
    return n(lambda x: x + 1)(0)

"""
Multiplication function:
The multiplication function takes two Church numerals as input and returns their product as another Church numeral.
"""
mult = lambda n: lambda k: lambda f: n(k(f))

"""
Power function:
Takes two Church numerals n and m as input and returns n raised to the power of m as another Church numeral.
"""
# power - pow n m = n^m
power = lambda n: lambda m: m(mult(n))(church_numeral(1))