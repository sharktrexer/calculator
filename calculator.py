# -*- coding: utf-8 -*-
"""
I, Ibrahim Sydock, pledge  that  I  have  neither  given  nor  received  help  from  anyone  other  than  the 
instructor/TA for all program components included here!
"""

#For sin, log, etc. functions
import math

'''operation methods'''
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def cot(num):
    return math.cos(num) / math.sin(num)


"""Dictionaries of value to operation function"""
# 2 input operations
DOS_OPERATIONS = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    '^' : math.pow
}

# 1 input operations
UNO_OPERATIONS = {
    'sin' : math.sin,
    'tan' : math.tan,
    'cos' : math.cos,
    'cot' : cot,
    'log' : math.log10,
    'ln' : math.log
    }

expression = input("What would you like to evaluate!?\n")
print(expression)