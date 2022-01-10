# Adding and removing of dictionary keys
week = {1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wednesday', 5: 'thursday', 6: 'friday', 7: 'saturday'}

# using .pop() method to remove a key
print(week.pop(2, None)) #return None if key is not found
print(week)

# using .update() to add a key
week.update({2 : "monday"})
print(week)



