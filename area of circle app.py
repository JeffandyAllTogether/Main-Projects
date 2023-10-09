#There are multiple ways to solve a problem!

#method 1
print("This program is to calculate the area of a circle.")

radius = input("Enter the circle's radius: ")
radius = int(radius)
result = 3.14159 * radius ** 2
print(result)

#method 2
r=float(input("Enter the radius of circle : "))
pi =3.14159
area=pi*(r**2)
print("Area of the cicle with given radius is : ",area)

#method 3
import math

def calculate_Area(radius):
    return math.pi * (radius * radius)

user_input = float(input("key in your radius:\n"))
print("The area of the radii is:", calculate_Area(user_input))


#solution
'''import math: This line imports the math module in Python. 
The math module provides various mathematical functions and constants, including 
the value of π (pi).

def calculate_Area(radius):: This line defines a function named calculate_Area that 
takes one argument, radius. Inside the function, it calculates the area of a circle 
using the formula π * (radius * radius) and returns the result.

user_input = float(input("key in your radius:\n")): This line prompts the user to enter a value for the radius of the circle. It uses the input function to take user input, which is a string by default. Then, it converts the user input to a floating-point number using float() and stores it in the variable user_input.

print("The area of the radii is:", calculate_Area(user_input)): 
This line calculates the area of the circle using the calculate_Area function 
and the user-provided radius stored in user_input. It then prints the result as a 
message to the console. The print statement consists of two parts: the first part is a 
string "The area of the radii is:", and the second part is the result of calling the 
calculate_Area function with user_input as its argument. This displays the calculated area 
along with the message.  '''

