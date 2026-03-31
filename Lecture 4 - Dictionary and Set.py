# dictionary -> dictionaries are used to store data values in key:value pair
# they are unordered (no index), mutable (changable) and don't allow duplicate keys
dic = {
    "name" : "Shraddha",
    "cgpa" : 8.7,
    "marks" : [98,97,95]
}

print(dic)
print(dic["name"])

# we can add a new key:value pair in a dictionary
dic["surname"] = "khapar"
print(dic)
print(dic["surname"])

# if we use the same key again, then the old key value pair is overwritten
# we can create a null dictionary and then add key value pair
null_dic = {}
null_dic["id"] = "101"
print(null_dic)

# nested dictionaries
student = {
    "name" : "shraddha",
    "marks" : {
        "physics" : 97,
        "chemistry" : 94,
        "maths" : 95
    },
    "grade" : "A" 
}
print(student)
print(student["marks"]["physics"])

# if we want to find the length of keys
print(len(student))

# dictionary methods
# 1. keys() -> returns all keys in a dictionary
print(student.keys())

# 2. values() -> returns all values in a dictionary
print(student.values())

# 3. items() -> returns all key:value pairs as tuples
print(student.items())

# 4. get("key") -> returns the key according go the value
print(student.get("grade"))

# print(student["name2"])  #return error
print(student.get("name")) # return none (no error)

# 5. update(newDict) -> insert the specified items to the dictionary
student.update({"city" : "pune"})
print(student)

#set -> set is a collection of unordered items in python.
# each element in the set must be unique and immutable (but sets are mutable)
# we don't store list and dictionary in a set since they are mutuable
nums = {1,2,3,4,5, "hello", "world"}
set2 = {1,2,2,3,3}
print(nums)
print(type(nums))
print(len(nums))
print(set2)

# empty set
collection = set() 
print(type(collection))

# sets method
# 1. add(element) -> adds an element in the set
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollege")
collection.add((3,4,5))
print(collection)

# 2. remove(element) -> removes the element in a set
collection.remove(1)
print(collection)

# 3. clear() -> empties a set
collection.clear()
print(collection)

# 4. pop() -> removes a randon value
collection.add(1)
collection.add(2)
collection.add("apnacollege")
collection.add((3,4,5))
collection.pop()
print(collection)

# 4. set.union(set2) -> combines both set values and returns new 
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))

# 5. set.intersection(set2) -> combines common value and returns new
print(set1.intersection(set2))

# practice questions:
# 1. store the following meanings
word_meaning = {
    "table" : ("a pair of furntiure", "list of facts and figure"),
    "cat" : "a small animal"
}
print(word_meaning)

# 2. you are given a list of subjects for classroom. assume 1 classroom is required for 1
# subject. how many classroom are required by all students
classroom = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
}
print(type(classroom))
print(len(classroom))

# 3. write a program to enter marks of 3 students from the user and store them in a 
# dictonary. start with an empty dictionary and add one by one. use subject name as keys
# and marks as values
# subject = {}
# subject["physics"] = input("enter marks in physics: ")
# subject["chemistry"] = input("enter marks in chemistry: ")
# subject["maths"] = input("enter marks in maths: ")
# print(subject)

# 4. figure out a way to store 9 and 9.0 as seperate values in the set
values = {9, "9.0"}
print(values)
# or
values = {
    ("int", 9),
    ("float", 9.0)
}
print(values)
