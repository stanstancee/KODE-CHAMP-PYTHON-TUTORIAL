my_string = "Success"
#print all characters in capital letter 
for char in my_string:
  print(char.upper())


#iterating over list
numbers = [2,5,6]
#multiply each number in the list by 2
for number in  numbers:
  print(number * 2)

#for/else loop
digits_in_string = "123456"
for digit in digits_in_string:
  if int(digit) % 2 == 0:
    print(digit + " is " + "even")
   
else:
  print("Finished getting even numbers.")

