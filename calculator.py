# -*- coding: utf-8 -*-
"""
I, Ibrahim Sydock, pledge  that  I  have  neither  given  nor  received  help  from  anyone  other  than  the 
instructor/TA for all program components included here!
"""

#For exiting cleanly
import sys

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

def neg(num):
    return num * -1


"""Dictionary of value to operation/func method"""
operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    '^' : math.pow,
    'u' : neg,
    's' : math.sin,
    't' : math.tan,
    'c' : math.cos,
    'o' : cot,
    'l' : math.log10,
    'e' : math.log
}

"""
Dictionary of an operation and it's precedence and associativity
Left is -1, Right is 1
"""
attributes = {
    '^' : (3, 1),
    '/' : (2, -1),
    '*' : (2, -1),
    '+' : (1, -1),
    '-' : (1, -1)
}

# If char is valid operator
def is_op(char):
    return char == '+' or char == '-'  or char == '*' \
    or char == "/" or char == '^'   

# if char is a valid function
def is_func(char):
    return char == 'u' or char == 's'  or char == 't' \
    or char == "c" or char == 'o' or char == 'l' or char == 'e'
   
# Shunting Yard Algorithm to convert equation into Reverse Polish Notation
def shunt(exp):
    ops_stk = [];
    output_que = [];
    for x in exp:
        # If a number, add to queue
        if x.isnumeric():
            output_que.append(x)
        # if a function, push to stack
        if is_func(x):
            ops_stk.append(x)
        # If an operator
        elif is_op(x):
            # while the operator on top is not a left paren,
            # AND has greater precedence OR same precedence and cur op is left-associative
            for i, o in reversed(list(enumerate(ops_stk))):
                if not ops_stk: break;
                #pop ops from stack onto queue 
                """ TODO: FIXXXXXXX
                while(o != '(' and attributes[o][0] > attributes[x][0] or \
                      (attributes[o][0] == attributes[x][0] and attributes[x][1] == -1)): 
                    #pop from stack onto queue
                    output_que.append(ops_stk.pop(i))
                """
            # push current op to stack
            ops_stk.append(x)
        # if left paren, push to stack
        elif x == '(' or x == '{':
            ops_stk.append(x)
        # if right paren
        elif x == ')' or x == '}':
            # while the top of the stack isn't a left paren
            for i, o in reversed(list(enumerate(ops_stk))):
                if o != '(': #or o != '{':
                    #pop ops from stack onto queue
                    output_que.append(ops_stk.pop(i))
                else:
                    #pop and discard left paren
                    ops_stk.pop(i)
            #if the top of the op stack is a func
            if ops_stk and is_func(ops_stk[-1]):
                #pop func to queue
                output_que.append(ops_stk.pop())
    #while there are ops on stack, pop to queue
    for i, o in reversed(list(enumerate(ops_stk))):
        output_que.append(ops_stk.pop(i))
          
    print(output_que)
    
    """ TODO: catch overflow exception """
    # evaluates reverse polish notation
    for op in output_que:
            if op.isdigit():
                ops_stk.append(op)
            elif is_func(op):
                num = int(ops_stk.pop())
                print(operations[op](num))
                ops_stk.append(operations[op](num))
            else:
                num2 = int(ops_stk.pop())
                num1 = int(ops_stk.pop())  
                print(operations[op](num1, num2))
                ops_stk.append(operations[op](num1, num2))
       
    print("\n= ", end='')  
    print(ops_stk[-1])
        
    
def validate(exp):
    """ ERROR: 
        more/less left parenthesis than right 
        Not a Number
        multiple operators in succession (excluding multiple minuses)
        dividing by zero
        
        CONVERSION:
        convert sin to s, unary '-' to u etc
        join multi digit number/decimals to one value"""
    return exp

if __name__ == '__main__':
    print("What would you like to evaluate!? Enter \"help\" for possible operations and formatting, and \
          \"exit\" to stop the calculator\n")
    # Loop
    while(True):
        expression = input("Input: ")
        
        #Get clean input with no white space
        expression = ''.join(expression.split())
        if expression == "help":
            print("\nWhen entering expressions, don't worry about excess spaces.")
            print("list of acceptable operators:")
            print("\n + \n - \n * \n / \n ^ \n sin() \n tan() \n cos() \n cot() \n log() \
                  - evaluates log 10 \n ln() - natural log\n")
        elif expression == "exit":
            sys.exit(0)
        else:
            validate(expression)
            shunt(expression)
    
    