# Day 3 of 30 days of python

#Exercises - Day 3

#Declare your age as integer variable
age = int

# Declare your height as a float variable
height = float

# Declare a variable that store a complex number
complex_number = complex

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input ("Enter the base: "))
Height = int(input ("Enter the height: "))
area = 0.5 * base * Height

print ("the area of the triangle is: ", area)

print("==================================================\n\n")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int (input ("Enter a: "))
b = int (input("Enter b: "))
c = int (input("Enter c: "))
perimeter = a+b+c

print("The perimeter of the triangle is: ", perimeter)

print("==================================================\n\n")




# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle"))
area_rectangle = length*width
perimeter_rectangle = 2*(length*width)

print ("The area of the rectangle is: ", area_rectangle)
print ("The perimeter of the rectangle is: ", perimeter_rectangle)

print("==================================================\n\n")


# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius_circle = int(input("Enter the radius of a circle: "))
PI = 3.142
area_circle = PI*radius_circle*radius_circle
circumference_circle = 2*PI*radius_circle

print ("the area of the circle is: ", area_circle)
print("The circumference of the circle is: ", circumference_circle)

print("==================================================\n\n")


