

""" for x in range(2,11,3):
    print(x)
 """

#table = int(input("enter table value:"))

""" 2X1= 2
2x2 = 4
2x3= 6 """

""" for x in range(1,10):
    print(f"{table} X {x} = {table*x}") """

student= ["aman","mohan","sohan","rohan","gohan","rita","rinku"]

""" print(len(student))
print(type(student))

print(student[2]) """

""" for s in student:
    print(s) """

""" for s in range(5):
    print(f"{s} - {student[s]}") """

""" for s in range(len(student)):
    print(f"{s} - {student[s]}") """
#1. Print numbers 1 to 10 using a for loop
""" for numbers in range(1,11):
    print(numbers) """
#2. Print even numbers from 1 to 20 using a for loop
""" for numbers in range(2,21,2):
    print(numbers) """
#3. Find the sum of numbers from 1 to 100 using a for loop. 
""" sum=0
for x in range (1,101):
    sum=sum+x
print(sum) """
#4. Print the multiplication table of 5 using a for loop.
""" for table in range(1,11):
    print(f"5*{table}={5*table}") """
# Sample raw hours from a timecard export (strings)
raw_hours = ["40.0", "37.5", "45.0", "42.0"]

# Task: Cast to float, calculate overtime (>40 hrs), and log standard vs OT hours
""" for h in raw_hours:
    total_hours = float(h)
    if total_hours > 40:
        regular = 40.0
        overtime = total_hours - 40.0
    else:
        regular = total_hours
        overtime = 0.0
        
    print(f"Total: {total_hours} | Regular: {regular} | Overtime: {overtime}") """
#5. Print each character of a string using a for loop.
""" text=input("Enter a string:")
for character in text:
    print(character) """
#6. Reverse a string using a for loop.
""" text = input("Enter a string: ")
reverse = ""

for character in text:
    reverse = character + reverse

print(reverse) """
#7. Count the number of vowels in a string using a for loop.
""" text = input("Enter a string: ")

vowels = "aeiou"

count = 0

for character in text:
    if character in vowels:
        count = count + 1

print("Number of Vowels:", count) """
#8. Find the largest number in a list using a for loop. 
""" numbers=[10,25,7,18,42,15,62,]
smallest=numbers[0]

for number in numbers:
    if number < smallest:
        smallest=number

print("Smallest number:", smallest) """
#10. Check if a number is prime using a for loop.
""" number=int(input("Enter a number:"))
is_prime=True

for i in range(2, number):
    if number % i == 0:
        is_prime = False

if is_prime:
    print("Prime")

else:
    print("Not Prime") """
