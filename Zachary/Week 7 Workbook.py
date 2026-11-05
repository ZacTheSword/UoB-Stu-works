#Week 7 Workbook

from datetime import date
import random

#Q1
print("My", "Name", "Is", "King", sep="$$")

#Q2
name1, name2, name3 = input("Enter three Names: ").split()
print(f"Name1: {name1}")
print(f"Name2: {name2}")
print(f"Name3: {name3}")

#Q3
print(f"{5.26459884:.2f}")

#Q4
year = 2023
quantity = 3
price = 450
print(f"I have bought {quantity} footballs for {price:.2f} £, in the year {year}.")

#Q5
sentence = "I have bought 3 footballs for 450.00 £, in the year 2023."
print(sentence[0])

#Q6
print(len("I have bought 3 footballs."))

#Q7
print(date.today())

#Q8
print(random.randint(1, 100))

#Q9
low = int(input("Enter the first number: "))
high = int(input("Enter the second number: "))
print(random.randint(low, high))

#Q10
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
print(f"Sum: {first + second}")