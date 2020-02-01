# -*- coding: utf-8 -*-
"""
Problem:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def gauss_formula(number):
    """Computes sum of all integers up to a given number

    Parameters
    ----------
    number : int
        Upper bound for summation

    Returns
    -------
    int
        Sum determined by the gauss formula

    """
    return number * (number + 1) // 2

def sum_multiples_3_and_5(max_number):
    """Compute sum of all multiples of 3 and 5 smaller than a given number

    In order to be more efficient the following steps are taken:
     - take integer part of quotient of max_number and 3, this is the quantity of number that can be divided by 3
     - determine the sum of those as 3 times the gauss sum for the quotient just mentioned
     - do the same with 5
     - add both sums
     - take into consideration all numbers that can be divided by 3 and 5, i.e. fifteen; compute sum of all numbers that
        can be divided by 15
     - substract the sum for 15 from the previous sum

    Parameters
    ----------
    max_number : int
        Upper bound (excluding) to which numbers are inspected

    Returns
    -------
    int
        Sum of all numbers

    """
    divided_by_3 = (max_number - 1) // 3
    divided_by_5 = (max_number - 1) // 5
    divided_by_15 = (max_number - 1) // 15

    return gauss_formula(divided_by_3) * 3 + gauss_formula(divided_by_5) * 5 - gauss_formula(divided_by_15) * 15

