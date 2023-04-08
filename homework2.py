# PPHA 30535
# Spring 2023
# Homework 2

# Tianhua Song
# SkySong4

# Due date: Sunday April 9th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

def sum_and_classify(a, b):
    sum_value = a + b
    if sum_value > 10:
        return "big"
    elif sum_value == 10:
        return "just right"
    else:
        return "small"

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

result_list = [sum_and_classify(a, b) for a, b in start_list]

print(result_list)

#result_list=['just right', 'big', 'small', 'small', 'small']

# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 30
    return a + b
x = my_func()

#using argument instead of global variable

def my_func(a):  # accept an argument 'a' instead of using a global variable
    b = 30
    return a + b

x = my_func(10)  # Pass the value of 'a' as an argument when calling the function
#The function can now work with any value of 'a' passed to it, rather than relying on a specific global variable.
#it is easier to see the dependencies of a function, which helps reduce the risk of unintended side effects when changing the code in the future.

# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random
  
import random
import string

def generate_password(length, special_chars=True, numbers=True):
    if length < 8 or length > 16:
        print("Make sure your password length between 8 and 16 characters.")
        return

    chars = string.ascii_letters  # Upper-case and lower-case letters
    if special_chars:
        chars += "!@#$%^&*"
    if numbers:
        chars += string.digits

    password = "".join(random.choices(chars, k=length))
    return password

# Usage examples:
password1 = generate_password(9)  # Default settings
print(password1)

password2 = generate_password(9, special_chars=False, numbers=False)  # No special characters or numbers
print(password2)
  
  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 3, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes a container holding any number of these 
# instances and returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

class Person:
    def __init__(self, name, vaccine, doses, had_covid):
        self.name = name
        self.vaccine = vaccine
        self.doses = doses
        self.had_covid = had_covid

    def get_record(self):
        print(f"{self.name} has {self.doses} doses of {self.vaccine} and {'has' if self.had_covid else 'has not'} had COVID.")

    def same_shot(self, other_person):
        if self.vaccine == other_person.vaccine:
            print(f"{self.name} and {other_person.name} have the same kind of vaccine ({self.vaccine}).")
        else:
            print(f"{self.name} and {other_person.name} have different vaccines ({self.vaccine} and {other_person.vaccine}).")

def all_data(person_list):
    return [[person.name, person.vaccine, person.doses, person.had_covid] for person in person_list]



