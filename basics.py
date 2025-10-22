# python is interpreted language and code is executed line by line
# variables are used to store data values
x = 5               # integer variable
y = "Hello World"   # string variable   
print(x)
print(y)
# Python supports multiple data types including integers, floats, strings, booleans, lists, tuples, and dictionaries
# Example of different data types
a = 10              # integer
b = 3.14            # float
c = "Hello World"   # string
d = [1, 2, 3]       # list
e = (1, 2, 3)       # tuple
f = {"name": "John", "age": 30} # dictionary
g = True            # boolean
h = None            # NoneType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# Type conversion or casting
sales="20850.75"
discount="500.50"
#total=sales-discount
#print(total)  # This will raise a TypeError because sales and discount are strings
# To perform arithmetic operations, we need to convert the strings to floats
total=float(sales)-float(discount)
print(total)  # This will print the correct total after conversion

#string concatenation
first_name="Umamahesh"
last_name="Reddy"
print(first_name + " " + last_name)  # Concatenating strings using + operator
print("my first name is "+first_name+" and my last name is "+last_name)  # Using string concatenation
print(f"my first name is {first_name} and my last name is {last_name}")  # Using f-strings for formatted output
print("my first name is {} and my last name is {}".format(first_name, last_name))

# Getting user input
name=input("Enter your name: ")  # Prompting user for input
salary=input("Enter your salary: ")
hike=input("Enter your hike percentage: ")
new_salary=float(salary)+(float(salary)*float(hike)/100)
print(f"Hello {name}, your new salary after a hike of {hike}% is {new_salary}")
