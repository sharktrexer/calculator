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


"""Dictionary of value to operation function"""
operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
    '^' : math.pow,
    'sin' : math.sin,
    'tan' : math.tan,
    'cos' : math.cos,
    'cot' : cot,
    'log' : math.log10,
    'ln' : math.log
}

""" 
Loop thru token
"""


# Calls operation function if it's unary or binary
def operate(operator, num1, num2):
    if math.isnan(num2):
        return operations[operator](num1)
    else:
        return operations[operator](num1, num2)
   
def is_op(char):
    return char == '+' or char == '-'  or char == '*' or char == "/" or char == '^'   
   
# Shunting Yard Algorithm to convert equation into Reverse Polish
def shunt(exp):
    ops_stk = [];
    output_que = [];
    for x in exp:
        # If a number, add to queue
        if x.isnumeric():
            output_que.append(x)
        # If an operator
        elif is_op(x):
            # while the operator on top has greater precedence
            for i, o in reversed(list(enumerate(ops_stk))):
                #pop ops from stack onto queue
                """ TODO: CHECK PRECEDENCE """
                #output_que.append(ops_stk.pop(i))
                break;
            # push op to stack
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
    #while there are ops on stack, pop to queue
    for i, o in reversed(list(enumerate(ops_stk))):
        output_que.append(ops_stk.pop(i))
        
    print(output_que)
    
    """ TODO: catch overflow exception """
    for op in output_que:
            if op.isdigit():
                ops_stk.append(op)
            else:
                num2 = int(ops_stk.pop())
                num1 = int(ops_stk.pop())
                if op == '*':
                    ops_stk.append(num1 * num2)
                elif op == '+':
                    ops_stk.append(num1 + num2)
                elif op == '-':
                    ops_stk.append(num1 - num2)
                elif op == '/':
                    ops_stk.append(num1 // num2)
                elif op == '^':
                    ops_stk.append(math.pow(num1, num2))
    print( ops_stk[-1])
        
    
def validate(exp):
    """ ERROR: 
        more/less left parenthesis than right 
        Not a Number
        multiple operators in succession (excluding multiple minuses)"""
    return exp

if __name__ == '__main__':
    while(True):
        expression = input("What would you like to evaluate!? Enter \"help\" for possible operations and formatting.\n")
        expression = expression.split()
        #print(expression)
        if expression[0] == "help":
            print("\nWhen entering expressions, don't worry about excess spaces. (However, don't include a space between "-" and a number if you want it to be negated)")
            print("list of acceptable operators:")
            print("\n + \n \- \n * \n / \n ^ \n sin() \n tan() \n cos() \n cot() \n log(x) \\- evaluates log 10 \n ln() \\- natural log\n")
        else:
            validate(expression)
            shunt(expression)
    
    