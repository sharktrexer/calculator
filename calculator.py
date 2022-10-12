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

srt_paren = ['(', '{']
end_paren = [')', '}']

# If char is valid operator
def is_op(char):
    return char == '+' or char == '-'  or char == '*' \
    or char == "/" or char == '^'   

# if char is a valid function
def is_func(char):
    return char == 'u' or char == 's'  or char == 't' \
    or char == "c" or char == 'o' or char == 'l' or char == 'e'
    
#returns true if the char can be converted into an int or float, otherwise return false
def is_num(char):
    try:
        int(char)
        return True
    except ValueError:
        try:
            float(char)
            return True
        except ValueError:
            return False

# returns number as a float or int using isinstance()
def get_num_type(num):
    if isinstance(num, int):
        return int(num)
    else:
        return float(num)
   
# Shunting Yard Algorithm to convert equation into Reverse Polish Notation
def shunt(exp):
    ops_stk = [];
    output_que = [];
    for x in exp:
        # If a number, add to queue
        if is_num(x):
            output_que.append(x)
        # if a function, push to stack
        if is_func(x):
            ops_stk.append(x)
        # If an operator
        elif is_op(x):
            # while the operator on top is not a left paren,
            # AND has greater precedence OR same precedence and cur op is left-associative
            for i, o in reversed(list(enumerate(ops_stk))):
                if not is_op(o): break;
                if(attributes[o][0] > attributes[x][0] or \
                      (attributes[o][0] == attributes[x][0] and attributes[x][1] == -1)): 
                    #pop from stack onto queue
                    output_que.append(ops_stk.pop(i))
                else: break;
            # push current op to stack
            ops_stk.append(x)
        # if left paren, push to stack
        elif x == '(' or x == '{':
            ops_stk.append(x)
        # if right paren
        elif x == ')' or x == '}':
            # while the top of the stack isn't a left paren
            for i, o in reversed(list(enumerate(ops_stk))):
                if not o in srt_paren:
                    #pop ops from stack onto queue
                    output_que.append(ops_stk.pop(i))
                else:
                    #pop and discard left paren
                    ops_stk.pop(i)
                    break;
            #if the top of the op stack is a func
            if ops_stk and is_func(ops_stk[-1]):
                #pop func to queue
                output_que.append(ops_stk.pop())
                
    #while there are ops on stack, pop to queue
    for o in ops_stk:
        output_que.append(ops_stk.pop())
          
    print(output_que)
    
    """ TODO: catch overflow exception """
    # evaluates reverse polish notation
    for op in output_que:
            if is_num(op):
                ops_stk.append(op)
            elif is_func(op):
                num = get_num_type(ops_stk.pop())
                print("evaluating: ", end='')
                print(op)
                print('with number: ', end='')
                print(num)
                print(operations[op](num))
                ops_stk.append(operations[op](num))
            else:
                num2 = get_num_type(ops_stk.pop())
                num1 = get_num_type(ops_stk.pop())  
                
                print("evaluating: ", end='')
                print(num1, end = ' ')
                print(op,  end = ' ')
                print(num2)
                
                #Check for divide by zero
                if(num2 == 0 and op == '/'):
                    print("~Cannot divide by zero")
                    return;
                
                print(operations[op](num1, num2))
                
                ops_stk.append(operations[op](num1, num2))
       
    print("\n= ", end='')  
    print(ops_stk[-1])
        
    
def validate(exp):
    #get exp string into an array of chars for easy iteration
    chars = list(exp)
    length = len(chars)
    new_exp = []
    i = 0;
    start = 0;
    
    left_paren = 0
    right_paren = 0
    
    while i < length:
        # if a digit, loop until a non-digit is found to get the entire number/decimal
        if chars[i].isdigit():
            start = i
            while i < length and (chars[i].isdigit() or chars[i] == '.'):
                i += 1
            #check for invalid decimal value
            num = chars[start:i]
            dec = 0
            for c in num:
                if c == '.': dec += 1
            
            if dec > 1: return '~Invalid decimal number'
            
            new_exp.append(''.join(num))
            i -= 1
        # if char is a potential beginning of sin, cot, etc, then check if the rest of the func is there
        # otherwise an invalid function is present
        elif chars[i] in 'sctl':
            if i + 2 >= length: return '~Invalid input'
            #convert function to one char value
            func = ''.join(chars[i:i+3])
            nat = ''.join(chars[i:i+2])
            func_to_token = ''
            
            if func == "sin": func_to_token = 's'
            elif func == 'tan': func_to_token = 't'
            elif func == 'cos': func_to_token = 'c'
            elif func == 'cot': func_to_token = 'o'
            elif func == 'log': func_to_token = 'l'
            elif nat == 'ln': func_to_token = 'e'
            else: return ''
                
            new_exp.append(func_to_token)
            
            #make sure to change index based on if a 3 or 2 letter func was used
            if nat == 'ln': i+= 1
            else: i += 2
        # Converting a minus if:
        elif chars[i] == '-':
            # at the start of the expression, then it is unary
            if i == 0: new_exp.append('u')
            # the previous key is an operator or starting paren, then it is unary
            elif is_op(chars[i-1]) or chars[i-1] in srt_paren: new_exp.append('u')
            # there is another minus, then convert to binary plus
            elif chars[i+1] == '-':
                i += 1
                new_exp.append('+')
            # if the next key isn't a left paren or a digit, then something is wrong
            elif not chars[i+1] in srt_paren and not chars[i+1].isdigit(): return '~Invalid use of operations'
            # otherwise it is binary minus
            else: new_exp.append(chars[i])
        # if an operation check if there is another operation ahead
        elif is_op(chars[i]):
            if(is_op(chars[i+1]) and chars[i+1] != '-'): return '~Invalid use of operators'
            new_exp.append(chars[i])
        # if a paren keep count
        elif chars[i] in srt_paren: 
            left_paren += 1
            new_exp.append(chars[i])
        elif chars[i] in end_paren: 
            right_paren += 1
            new_exp.append(chars[i])
        # invalid token
        else: return '~Invalid input'
        
        #increment
        i += 1
      
    if right_paren != left_paren: return '~Mismatching parenthesis'
    
    print("validated exp: ", end="")
    print(new_exp)
    return new_exp

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
            print("Accepts regular \'()\' and curly \'{}\' brackets interchangeably\n")
            print("\n~~~~~~~~~~~~~List of acceptable operations~~~~~~~~~~~~~")
            print("Binary operators:\n+, -, *, /, ^\n")
            print("Trigonmetry Functions (returns values in radians): \nsin(), tan(), cos(), cot()\n")
            print("Logarithmic Functions: \nlog(): evaluates log10, ln(): evaluates natural log")
        elif expression == "exit":
            sys.exit(0)
        else:
            validated = validate(expression)
            if '~' in validated: print(validated)
            else: shunt(validated)
    
    