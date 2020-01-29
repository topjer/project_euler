# -*- coding: utf-8 -*-
"""
Problem:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
def sum_multiples_3_and_5(max_number):
    return sum([number for number in range(1, max_number) if number % 3 == 0 or number % 5 == 0])
