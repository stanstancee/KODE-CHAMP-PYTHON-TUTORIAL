#list construction
#using list constructor
my_numbers = list((1,2,3,4,5,6,7,8,9))
print(my_numbers)

#using sqare brackets
week = ["sunday","monday","tuesday", "wednesday", "thursday", "friday", "saturday"]
print(week)

# indexing an array
first_day = week[0] # list index starts from 0
third_day = week[2]
print(first_day) # sunday
print(third_day) # wednesday

# negative index
# last element in the list has index -1
last_day = week[-1]
print(last_day) # saturday

#index error 
# looking up for the wrong index raises an error 
# unknown_day = week[9]
# print(unknown_day) #IndexError: list index out of range

#slicing
week = ["sunday","monday","tuesday", "wednesday", "thursday", "friday", "saturday"]
#slice from index 2 to index 5 (index 5 excluded)
some_days = week[2 : 5] 
print(some_days) # ["tuesday", "wednesday", "thursday",]

# begin at the original list
some_days = week[: 5] #  ["sunday","monday","tuesday", "wednesday"]
print(some_days)

# end at the very end of the original list
some_days = week[3: ]
print(some_days) # ["wednesday", "thursday", "friday", "saturday"]

# getting the length of a list 
print(len(week)) # 7

#list membership operators
check = "monday" in week
print(check) # True

check = "April" not in week 
print(check) # True

# list muatability
week[3] = "march"
print(week)
week[3] = "wednesday"
print(week)











