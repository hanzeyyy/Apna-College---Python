    # list -> a built in data type that stores set of values
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))

# indexig in list 
print(marks[1])

# slicing in list
student = ["Karan", 95.4, 17, "Delhi"]
print(student[3])
print(student[3][0:2])

# list are mutable (can be changed/modified)
student[0] = "Aditya"
print(student)

list = [2,1,3]
# append() -> add an element at the end of the list 
list.append(4)
print(list)

# sort() -> sorts list in asceneding order
list.sort()
print(list)

# sort(reverse = True) -> sorts list in desceneding order
list.sort(reverse = True)
print(list)

# reverse() -> reverse list 
list.reverse()
print(list)

# insert(index, element) -> inserts element at a particular index
list.insert(2, 1)
print(list)

# remove() -> removes first occurance of an element
list.remove(1)
print(list)

# pop() -> removes an element at a particular index. by default, last element will be removed
list.pop()
print(list)

# tuples -> a built-in datatype that help us create immutable sequence of values
tup = (2, 1, 3, 1)
print(type(tup))
print(tup[1])
print(tup[0:2])

# empty tuple -> a tuple with no element inside
tup = ()
print(tup)
print(type(tup))

# a single element tuple will be treated as int, str, float depending upon the element 
tup = (1)
print(type(tup))
tup = (1.0)
print(type(tup))
tup = ("Hi")
print(type(tup))

# to treat a single tuple as a tuple, we simply put a comma at the end
tup = (1,)
print(type(tup))

tup = (2, 1, 3, 1)
# index(element) -> returns the first occurance of an element 
print(tup.index(1))

# count(element) -> counts total occurance
print(tup.count(1))

# write a program to ask the user to enter names of their 3 fav movies and store them in a list
# method 1
# mov1 = input("Enter 1st movie: ")
# mov2 = input("Enter 2nd movie: ")
# mov3 = input("Enter 3rd movie: ")
# movie = []
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# print(movie)

# #method 2
# movie = []
# mov = input("Enter 1st movie: ")
# movie.append(mov)
# mov = input("Enter 2nd movie: ")
# movie.append(mov)
# mov = input("Enter 3rd movie: ")
# movie.append(mov)
# print(movie)

# # method 3
# movie = []
# movie.append(input("Enter 1st movie: "))
# movie.append(input("Enter 2nd movie: "))
# movie.append(input("Enter 3rd movie: "))
# print(movie)

# write a program to check if a list contains a palindrome of elements
list1 = [1,2,1]
list1_copy = list1.copy()
list1_copy.reverse() 
if (list1 == list1_copy):
    print("palindrome")
else:
    print("not palindrome")

list2 = [1,2,3]
list2_copy = list2.copy()
list2_copy.reverse() 
if (list2 == list2_copy):
    print("palindrome")
else:
    print("not palindrome")

# write a program to count the number of student with A grade in the following tuple
grade = ("C", "D", "A", "A", "B","B", "A")
print(grade.count("A"))

# store the above values in list and sort them from "A" to "D"
list = ["C", "D", "A", "A", "B","B", "A"]
list.sort()
print(list)
