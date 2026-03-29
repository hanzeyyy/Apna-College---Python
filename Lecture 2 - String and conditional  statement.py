str1 = 'this is a string'
str2 = "apna college"
str3 = '''this is a python course'''
# why do we 3 different formats for writing a string?
# while writing a string, it can happen that we use ' or "" in the string itself. that's why we deployed 3 forms so that python can understand the difference

# \n -> new line (escape sequence character)
str1 = 'this is a string.\nwe are creating this in python'
print(str1)

# concatenation -> adding two strings
print(str2 + " " + str3)

# len() -> tells us the length of a string
print(len(str2))

# indexing -> numerical position of each character (numbering starts from zero)
print(str1[1])

# string is immutable -> cannot change characters of a string

# slicing -> accessing parts of a string
print(str2[0:4])
print(str2[0:]) #str2[0:10]
print(str2[:4]) #str2[0:4]

#  slicing: negative index 
print(str2[-7:-1])

str = "i am studying python from ApnaCollege"
# endswith(substring) -> returns True if string ends with a substring
print(str.endswith("ge"))

# capitalize() -> capitalize the first index of a string
print(str.capitalize())

# replace(old, new) -> replaces all occurance of old with new
print(str.replace('a', 'd'))

# find(word) -> returns 1st index of 1st occurrer
print(str.find("o"))

# count() -> counts the occurance of substring in a string
print(str.count("a"))

# conditional statement
age = 17
if (age >= 18):
    print("Eligible for voting and driver's license") #indentation -> proper spacing
else:
    print("Not eligible")

light = "Green"
if (light == "Red"):
    print("Stop")
elif (light == "Yellow"):
    print("Wait")
elif (light == "Green"):
    print("Go")
else:
    print("Light is broken")

marks = 88
if (marks >= 90):
    print("grade: A")
elif (marks >=80 and marks < 90):
    print("grade: B")
elif (marks >=70 and marks < 80):
    print("grade: C")
elif (marks < 70):
    print("grade: D")

# nesting conditonal statements
age = 31
if (age >= 18):
    if (age>=90):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")   
