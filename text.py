def comment_division():
    print("=========================")

# Variables
first_name = "Alice"
surname = "Smith"
group = 24
is_student = False

print(first_name + " " + surname + " #" + str(group))

number = 25
pi_value = 2.718
greeting = "Hi"
is_rainy = True

comment_division()

# Type conversion
score = 8.45
print(int(score))

height = 180
print(str(height))

cost = "14.50"
print(float(cost))

# Challenge
name = "Lucas"
last_name = "Mendez"
age = 30
print("Hello " + name + " " + last_name + ", you are " + str(age) + " years old.")

comment_division()

# Operators
a = 12
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

comment_division()

# Comparison Operators
x = 20
y = 15

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

m = 4
n = 8
print(m > 2 and n < 10)
print(m > 5 or n > 7)
print(not(m < 5))

comment_division()

# Lists
animals = ["lion", "tiger", "bear"]
print(animals)
print(animals[0])
print(animals[-1])

animals.append("elephant")
print(animals)

animals.remove("tiger")
print(animals)

print(animals.pop(1))
print(animals)

print(animals.index("lion"))

animals.append("lion")
print(animals)
print(animals.count("lion"))

comment_division()

# If statements
score = 45
if score >= 50:
    print("Pass")
else:
    print("Fail")

temp = 25

if temp > 30:
    print("It's hot")
elif temp == 25:
    print("Perfect weather")
else:
    print("It's cool")

for i in range(3):
    print(i)

colors = ["red", "blue", "green"]

for color in colors:
    print(f"Color: {color}")

comment_division()

# Functions
def welcome():
    print("Welcome to the program")

welcome()

def greet_person(name):
    print("Greetings, " + name)

greet_person("Sophie")
