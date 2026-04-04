# file i/o -> python can be used to perform operations on a file. (read and write only)
'''
types of files:-
1. text: .txt, .docx, .log etc
2. binary files: .mp4, .mov, .png, .jpeg etc 
'''

# open, read, and close file -> we have to open a file before reading or writing
'''
f = open("file name", "mode")
file name -> sample.txt, demo.docx etc
mode -> r (read mode), w (write mode) 
data =f.read
f.close()
'''

f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

'''
character and meaning
'r' - open for reading (default)
'w' - open for writing, trauncating the file first 
'x' - create a new file and open it for writing
'a' - open for writing, and appending at the end of the file if it exists
'b' - binary mode
't' - text mode (by default)
'+' - open a disk file for updating (reading and writing)
'''

# reading a file
f = open("demo.txt", "r")
line1 = f.readline() #reads one line at a time i.e. line 1
print(line1)
line2 = f.readline() #reads one line at a time i.e. line 2
print(line2)
f.close
 
# writing to a file
f = open("demo.txt", "w")
f.write("\n this is a new line.") # overwrites the entire file
f.close()

f = open("demo.txt", "a") # append
f.write("\n i will learn python libraries next") # adds to the file
f.close()

# with syntax
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
# we don't need to close the file here. it closes automatically

with open("demo.txt", "w") as f:
    f.write("new data")

# deleting a file 
# using the os module
# module (like the code library) is a file written by another programmer that generally has a function we can use
import os
os.remove("demo.txt")   
