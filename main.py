#Assign 10 to x and 5 to y
x = 10
y  = 5
#if x is greater than y: then, print "x is greater than y" 
if x > y:
  print("x is greater than y")

#nesting ifs
#Assign 4 to x and -4 to y
x, y = 4, -4
#if x is not equal to y
if x != y:
  print("Not equal")
  if x > 0:
    print("x is a positive integer")
  if y > 0:
    print("y is a positive integer")

#if- else
color = "red"
if color == "blue":
  print("Up blues")
else:
  print("Your blood is red!")

#if-else nesting
num = 40
if num >= 90:
  print("Your grade is A")
else:
  if num >= 70:
    print("Your grade is B")
  else:
    if num >= 60:
      print("You grade is C")
    else:
      if num >= 40:
        print("Your grade is D")
      else:
        print("Please kindly take the course again.")

#elif statement 
num = 65
if num >=90:
   print("Your grade is A")
elif num >= 70:
   print("Your grade is B")
elif num >= 60:
   print("You grade is C")
elif num >= 40:
   print("Your grade is D")
else:
   print("Please kindly take the course again.")

age = 7
covid_19 = False
colour = "green"
if not covid_19:
  if (age >= 16) and (colour == "red"):
    print("Thanks for coming:")
    print("Pass to the main hall")
  elif(age > 16) and (colour != "red"):
    print("Thanks for coming:")
    print("Pass to the second hall")
  else:
    print("We couldn\'t allow you because of your age. ")
else:
  print("Sorry, You are covid_19 positive.Go home and take care of yourself")

#pass statement
total = 9
if num > 10:
  print("Sorry we cant take more than 10 ")
elif num >= 8 :
  pass 
else:
  print("You have successfully registered.")



