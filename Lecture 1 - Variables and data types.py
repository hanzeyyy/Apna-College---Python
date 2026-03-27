print("Hello World!")
print("My name is Hanzala.", "I study at IIT Bombay")

name = "Hanzala" #string
age = 25 #intger
price = 16.95 #float

print("My name is:",name)
print("My age is:",age)

# '=' is called assignment operator (assigns values right to left)

# type() -> returns class of data type
print(type(name))
print(type(age))
print(type(price))

old = False
a = None
print(type(old))
print(type(a))

# python is a case sensitive language

a = 1000
b = 500
sum = a + b
diff = a - b
print(sum)
print(diff)

# arithmetic operators
a = 5 
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #a^b

#relational operators
a = 50
b = 20
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

# assignment operator
num = 10
num += 10 # num = num + 10
print("num:",num)
num -= 10 # num = num + 10
print("num:",num)
num *= 10 # num = num * 10
print("num:",num)
num /= 10 # num = num / 10
print("num:",num)
num %= 10 # num = num % 10
print("num:",num)
num **= 10 # num = num ** 10
print("num:",num)

# logical operators
print(not False)
print(not True)

val1 = True
val2 = True
print("answer is:", val1 and val2)

val1 = True
val2 = False
print("answer is:", val1 and val2)

val1 = True
val2 = True
print("answer is:", val1 or val2)

val1 = True
val2 = True
print("answer is:", val1 or val2)

# type conversion 
a = 2
b = 4.25
sum = a + b 
print(sum)

c = "3"
sum += int(c)
print(sum)

#input() -> takes input from the user
name = input("Enter your name: ")
print(type(name))
# result of input() is a string

num = int(input("Enter the number:"))
print(type(num))

num = float(input("Enter the number:"))
print(type(num))
