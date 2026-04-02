# functions -> block of statements that perform a specific task
'''
syntax:
def function_name (parameter1, parameter2, ...): # function definition
    some work
    return value

function_name(argument1, argument2, ...) # function calling
''' 
def cal_sum(a,b):
    sum = a + b
    return sum

print(cal_sum(88,99))

def print_hello(): # no parameters
    print("hello world")

print_hello() # no arguments
output = print_hello()
print(output) # none since it doesnot return anything

# average of 3 numbers
def cal_avg (a,b,c):
    avg = (a + b + c)/3
    return avg

print(cal_avg(1,2,3))

# function types
'''
there are two types of functions
1. built in
2. user defined

1. built in functions
1.1 print()
print("apnacollege", "python") # sep = " "
print("apnacollege", "python") # end = "\n"
if we don't want the letters to be seperated by space, then we can pass a different seperator
print("apnacollege", "python", sep = "_") # sep = "_"
print("apnacollege", "python", end = " - ") # end = "\n"
1.2 len()
1.3 type()
1.4 range()
'''

# default parameters -> assigning a default value to parameter, which is used when no argument is passed
def cal_prod(a,b=6): # we can assign some default value in the (last) parameters itself
    prod = a * b
    return prod

print(cal_prod(5))

# practice questions
# 1. WAF to print the length of a list. (list is the parameter)
cities = ["Mumbai", "Delhi", "Pune", "Bangalore"]
team = ["MS Dhoni", "Virat Kohli", "Jadeja"]
def cal_len(list):
    return len(list)

print(cal_len(cities))
print(cal_len(team))

# 2. WAF to print the elements of a list in a single line. (list is the parameter)
def print_list(list):
    for item in list:
        print(item, end = " ")

print(print_list(team))

# 3. WAF to find the factorial of n. (n is the parameter)
def print_fac(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

print_fac(5)

# 4. WAF to convert USD to INR
def converter(usd_value):
    inr_value = 90 * usd_value
    print(usd_value, "USD =", inr_value, "INR")

converter(5)

# recursion -> when a function calls itself repeatedly
# WAP to print n to 1 backwards 
def show(n):
    if ( n == 0): # base case
        return
    print(n)
    show(n-1)

show(6)

# WAP to print n factorial
def cal_fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * cal_fact(n-1)
    
print(cal_fact(4))

# practice questions
# 1. write a recursive function to calculate the sum of first n natural numbers
def get_sum(n):
    if ( n == 0 ):
        return 0
    else:
        return n + get_sum(n-1)

print(get_sum(4))

# 2. write a recursive function to print all elements in a list. (use list and index as parameters)
def print_list(list, idx = 0):
    if ( idx == len(list)):
        return 
    else:
        print(list[idx])
        print_list(list, idx+1)

fruits = ["banana", "mango", "orange"]
print_list(fruits)
