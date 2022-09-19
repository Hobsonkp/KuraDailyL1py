# Return the Sum of Two Numbers
# Convert Minutes into Seconds
# Write a function that takes an integer minutes and converts it to seconds.
# Examples
#   convert(5) ➞ 300
#   convert(3) ➞ 180
#   convert(2) ➞ 120

def convert_time(intMinutes):
    return int(intMinutes) * 60

print("Enter time in minutes to convert to seconds")

firstNumber = input("Enter time in minutes : ")

print(firstNumber,"minutes = ",convert_time(firstNumber)," seconds.")