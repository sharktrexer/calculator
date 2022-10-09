# -*- coding: utf-8 -*-
"""
I, Ibrahim Sydock, pledge  that  I  have  neither  given  nor  received  help  from  anyone  other  than  the 
instructor/TA for all program components included here!
"""

import math

#operation methods
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

#Dictionary of value to operation function
OPERATIONS = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    '^' : math.pow,
}

