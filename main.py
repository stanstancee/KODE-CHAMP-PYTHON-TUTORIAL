# empty cury braces
greetings = "Hi , {}! , its {}, in {}."
greeting = "good morning"
my_time = "11:23 AM"
city = "Lagos"
greetings = greetings.format(greeting, my_time, city)
print(greetings)

# named indexes
greetings = "Welcome, {first_name} {last_name}."
print(greetings.format(first_name = "Stanley", last_name ="Luke"))

#numbered indixes
introduction = "My name is {1}, I am {0} years old!"
print(introduction.format(34, "Paul"))


items = 100;
while True:
  if items >= 100:
    read_line = input("Please enter quantity of item(s) sold \n Enter E to stop \n Qty : " )
  else:
      read_line = input("Qty : ")
 
  try:
    qty = float(read_line)
    items  -=  qty
    if items > 0:
       message = "You have {} items left in the store."
       print(message.format(items))
    
  except  :
    if not read_line.lower() == "e":
      print(read_line + " is not a number.", "Please enter a valid number")
      
  if( read_line.lower() == "e"):
      print("goodbye !")
      break
  elif(items <= 0):
      print("No items left in store!")
      break
  
 
  


