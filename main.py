# keys() method
week = {1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wednesday', 5: 'thursday', 6: 'friday', 7: 'saturday'}

#create a key view
keys = week.keys()
print(keys)
abbr = ["st", "nd" , "rd", "th"]
for key in keys:
  values = week[key]
  abbr_key = str(key) + abbr[(key - 1)] if key < 4 else str(key) + abbr[-1]
  print( abbr_key , " day is " , values )

# values() method
values = week.values()
print(values)
for value  in values:
  print(value.upper())

#membership test
print("monday" in week.values())
print(4 in  week.keys())

#items() method
week = week.items()
print(week)
for key , value in week:
  print( key , " --- ", value)



# using while
# x = True
# while x :
  
#   read_line = input('Enter days of the week e.g 2 or Monday', "Enter end to stop")
#   if read_line == "end".lower():
#     x = False
  

