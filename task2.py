#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

# volume of sphere is v = 4/3 3.14...*r cubed
import math

num = input("Enter radius of a sphere.")
num = int(num)
num2 = 4/3 * 3.14 * num ** 3
num2 = str(num2)
print("the volume of the sphere is " + num2)