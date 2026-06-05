#1 - write a program which takes 2 inputs from the user : weight(kg)
# and height(meter) and prints the BMI in the output.
# BMI = weight / (square of height)
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (pow(height,2))
print(bmi)

#2 - write a program which takes the name of the user as input and
# replace all the occurrence of character 'a' in the name to 'b' and print it.
name = input("Enter your name: ")
name = name.replace("a", "b")
print(name)

#3- write a program which takes 2 inputs from user as principal amount (int) and rate of annual interest (float)
# and print the expected total amount  after  2 years.
# example : principle : 100 , interest percent 10  then amount after 2 years will be : 100*1.1*1.1 = 121
principal_amount = int(input("Enter your principal amount: "))
rate_of_annual_interest = float(input("Enter your rate of annual interest (%): "))
years = int(input("Enter your number of years: "))
expected_total_amount = principal_amount * pow((1 + rate_of_annual_interest/100),years)
print(int(expected_total_amount))

#4- write a program which takes city name from user input. irrespective of in which case user enters the
# city name, print the city name in camel case meaning first letter should be capital and rest in small.
# example : input : MYSORE ,  print - > Mysore

city = input("Enter your city: ")
city = city.title()
print(city)

#5- write a program which takes the name of the user as input and print the index of character 'a' in the
# string. if 'a' is not there then return -1.
name = input("Enter your name: ")
name = name.rfind("a")
print(name)

#6-  Display the number of letters in the below string
# my_word = "antidisestablishmentarianism"
my_word = "antidisestablishmentarianism"
print(len(my_word)+1)

#7- take 3 inputs from user : first name , last name and age . Display the information in below format
# example
# first name : MOhit
# last name : sharma
# age : 32
# Display : my name is Mohit Sharma and I am 32 years old.
# note that first letter of first name and last name both should be in capital letters and rest in small.
first_name = input("first name: ")
last_name = input("last name: ")
first_name = first_name.title()
last_name = last_name.title()
age = int(input("age: "))
print(f"my name is {first_name} {last_name} and I am {age} years old.")

#8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
# example
# first name : MOhit
# last name : sharma
# company : infosys
# Display : morma@infosys.com
# note full email id should be in lower case
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
company = input("Enter your company: ")
display = first_name[0:2]+last_name[-3:]+"@"+company+".com"
print(display.lower())
