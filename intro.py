def comment_division():
    print("=========================")
# ====== Variables ======
name="Samuel"
last_name="Dominguez"
cohort=52
is_Active=True

print(name + "" + last_name + " #" + str(cohort))

integer=10 #Integer
float1=3.14 #Float
text="Hello" #String
is_sunny=False #Boolean

comment_division()
# =====Type conversion ======
num= 9.75
print(int(num)) # Convert a float to integer

age=25
print(str(age)) #Convert an integer to a string

precio= "19.99"
print(float(precio))

#Challenge
#Create some variables called: name, last_name, age and show them in a print
#"Hello", <name> <last_name>, you are <age> years old

name="Nerosqui"
last_name="Dominguez"
age= 57
print("Hello" + name + last_name + ", you are " + str(age) + "years old.")

comment_division()
# ====== Operators ======
x=5
y=3

print(x+y) #addition
print(x-y) #substraction
print(x*y) #multiplication
print(x/y) #division
print(x%y) #modulus
print(x**y) #exponentiation

comment_division()
# ===== Comparison Operators ======
a=10
b=5

print(a==b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to

x=5
y=10
print(x>3 and y<15) #True, because both conditions are true
print(x>3 or y>15) #True, because at least one condition is true
print(not(x>3)) #False, because x is greater than 3 and we are applying not

comment_division()
# ====== Lists ======
fruits=["apple", "banana", "cherry"]
print(fruits) #print the first element
print(fruits[0]) #accesing the first item
print(fruits[-1]) #accesing the last item

#list methods
fruits.append("grape")
print(fruits)

fruits.remove("banana") #removes "banana"
print(fruits)

print(fruits.pop(1)) #removes and prints item at index 1 "cherry"
print(fruits)

print(fruits.index("apple")) #return the index of "grape"

fruits.append("apple")
print(fruits) #returns the number of times "apple" appears in the 
print(fruits.count("apple")) #return how many times apple appears

comment_division()
# ====== if statements ======
age=20
if age>=18:
    print("You are an adult") #if the condition is true, print this message
else:
    print("You are a minor") #if the condition is false, print this message

x=10

if x>10:
    print("x is greater than 10") #if the condition is true, print this message
elif x==10:
    print("x is equal to 10") #if the first condition is false, check this
else:
    print("x is less than 10") #if all conditions are false, print this message

for i in range(5): #loop from 0 to 4
    print(i) #print each number in the range

fruits=["apple", "banana", "cherry"]

for x in fruits: #loop through each item in the list
    print(f"fruit: {x}") #print each item

comment_division()
# ====== Functions ======
def greet():
    print(f"Hello from greet function")

greet() #calls the function

def say_hi(name):
    print("Hi,"+name)

say_hi("Bruce")
