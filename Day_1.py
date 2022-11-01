import numbers
from pydoc import tempfilepager
from tkinter.font import names
from traceback import print_tb
from unicodedata import name


variale = 20
variale = 30.9765
#print("Hello World")
#Boolean
bool_try = False
#print(variale)
###Exercise###
patient_name = "John Smith"
patient_age = 20
patient_status = "NEW"
print(patient_name,patient_age,patient_status)
namae = input("What is your name? ")

#Recieving Input
print("Hello " + namae)

#Type-Conversion (int, float, bool)
birth_year = input("Enter your birth year: ")
age_person = 2020 - int(birth_year)
print("Age: ".format("age_person"))

#Basic Calculator Program
first_num = input("First:")
second_num = input("Second:")
sum_inputs = float(first_num) + int(second_num)
print(sum_inputs)
#print("Sum: ".format(sum_inputs))
print("Sum: " + str(sum_inputs))

#STRINGS
str_var = 'I like anime and manga'
print(str_var.upper())
print(str_var.find('man'))
print(str_var.replace('and','&'))
print('anime' in str_var) #returns boolean value

#Arithmetic Operators
print(10//3) #output is int
print(10/3) #output is float
print(10**3) #10^3
x = 10
x *= 3
print(x)


#comparision operators(> >= < <= == !=)

#logical operators
price = 25
print(price>10 | price<30)
print(not price>10)

#if statements
temperature = 25

if temperature > 30:
    print("Its a hot day!")
elif temperature>20:
    print("Its a nice day")
elif temperature>10:
    print("Its a cold day")
else:
    print("Its cold")

#Exercise
weight = input("W: ")
k_l = input("kg or lb: ")

if k_l == "kg" or "k":
    print("Weight in kg is....")
elif k_l == "lb" | "l":
    print("Weight in LLLLBBBBBBB is....")
else:
    print("Invalid option")

#WHILE LOOP
i = 1
while i <= 5:
    print(str(i) + '*')
    i = i+1

#LIST
names = ["Ragi", "Ragini", "Ginira", "Misara"]
names[1]="Pehlanaam"
print(names[1])
print(names[-1])
print(names[:2])

#LIST METHODS
numbers_list = [1,2,3,4,5]
numbers_list.append(6)
numbers_list.insert(0,-1)
numbers_list.remove(3)
#numbers_list.clear()
print(1 in numbers_list)
print(len(numbers_list))
print(numbers_list)

#FOR LOOP
numbers_list = [1,2,3,4,5]
for item in numbers_list:
    print(item)

numbers_list = [1,2,3,4,5]
i = 0
while i < len(numbers_list):
    print(numbers_list[i])
    i = i+1

#RANGE FUNC
ran_obj = range(5, 10, 2)   #start and end values and jump
for i in ran_obj:
    print(i)

#TUPLES
enum_numbers = (1,2,3)  #tuples are immutable, unchangeable
print(enum_numbers.count())
print(enum_numbers.index(3))
#use tuple so someone doesn't modify list