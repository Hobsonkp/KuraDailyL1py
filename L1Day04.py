# Area of a Triangle
# Write a function that takes the base and height of a triangle and return its area.
# Examples
#   tri_area(3, 2) ➞ 3
#   tri_area(7, 4) ➞ 14
#   tri_area(10, 10) ➞ 50
# Notes
#   The area of a triangle is: (base * height) / 2

def triangle_area(base, height):
    return float((float(base) * float(height))/2)


firstNumber = input("Enter base of triangle : ")
secondNumber = input("Enter height of triangle : ")
unitOfMeasure = input("Enter unit of measure  : ")

print("Area of triangle is: (",firstNumber," * ",secondNumber,")/2 = ",triangle_area(firstNumber,secondNumber),unitOfMeasure,"^2")
