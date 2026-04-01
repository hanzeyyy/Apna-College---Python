# loops -> loops are used to repeat instructions
# 1. while loop 
count = 1
while count <= 5:
    print("hello")
    count += 1


# practice questions
# 1. print number from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# 2. print numbers from 100 to 1
i = 1
while i >= 1:
    print(i)
    i -= 1

# # 3. print the multiplication table of n
n = int(input("enter number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1 

# 4. print the elements of the following list using a loop:
list = [1,4,9,16,25,36,49,56,81,100]
i = 0
while i < len(list):
    print(list[i])
    i +=1

# 5. search for a number x in the tuple using loop
tuple = (1,4,9,16,25,36,49,56,81,100)
n = int(input("enter number: "))
i = 0
while i < len(tuple):
    if (tuple[i] == n):
        print ("found at index", i)
    i +=1

# break and continue:
# break -> used to terminate the loop once encountered
# continue -> terminates the execution in the current iteration and continue iteration of the loop in the next iteration
i = 0
while i <= 5:
    print(i)
    if (i == 3):
        break # end
    i +=1
print("end of loop")

i = 0
while i <= 10:
    if (i%2 == 0):
        i +=1
        continue # skip
    print(i)
    i +=1
print("end of loop")

# loops are used for sequential traversal. for traversing list, tuple, sting etc
# 2. for loop
list = [1,2,3]
for i in list:
    print(i)

# for loop with else
list = [1,2,3]
for i in list:
    print(i)
else:
    print("the end")

str = "apnacollege"
for i in str:
    print(i)

# practice questions
# 1. print the elements of the following list using a loop:
list = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)

# 2. search for a number x in the tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100)
num = int(input("Enter the number: "))
idx = 0
for i in tuple:
    if (i == num):
        print("index", idx)
        break
    idx +=1

# range() -> range function returns a sequence of numbers, starting from 0 (by defult), and incremenst by 1 (by default), and stops 
# before a specified number
# range(start?, stop, step?)
print(range(5))

for el in range(5): #range(stop)
    print(el)

for el in range(1,5): #range(start, stop)
    print(el)

for el in range(1,5,2): #range(start, stop, step size)
    print(el)

# practice questions
# using range and for loop
# 1. print number from 1 to 100
for i in range(1, 101):
    print(i)

# 2. print number from 100 to 1
for i in range(100,0,-1):
    print(i)

# 3. print the multiplication table of n
n = int(input("Enter number: "))
for i in range(1,11):
    print(n*i)

# pass statement -> pass is a null statement that does nothing. it is used as a placeholder for future code
for i in range(10):
    pass

if i > 3:
    pass

# practice questions
# 1. write a program to find the sum of first n numbers (while loop)
n = int(input("Enter number: "))
i = 0
sum = 0
while i < n:
    sum = sum + i
    i +=1
print(sum)

# 2. write a program to find the factorial of first n numbers (for loop)
n = int(input("Enter number: ")
fact = 1
for i in n:
    fact = fact*n
print(fact)
