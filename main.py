#Type casting
#simple calculator
num_1 = input("Please enter your first number\n") # Get first input
num_2 = input("Please enter your second number\n") # Get second input

#cast strings to floats
num_1_float = float(num_1)
num_2_float = float(num_2)

#sum the two floats
sum = num_1_float + num_2_float

#cast sum to strings
sum = str(sum)
#print sum
print("The sum of " + num_1 + " and " + num_2 + " is " + sum )

