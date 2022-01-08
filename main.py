week = ["sunday","monday","tuesday", "wednesday", "thursday", "friday", "saturday"]
num = [2,6,7,4,65,3,5]

# max()
max_week = max(week) # maximum starting character
max_num = max(num)
print(max_week) # wednesday
print(max_num) # 65

# min()
min_week = min(week) # maximum starting character
min_num = min(num)
print(min_week) # friday
print(min_num) # 2

# sorted()
sorted_list = sorted(num)
reverse_sorted_list = sorted(num, reverse = True)
print(sorted_list)
print(reverse_sorted_list)

# methods
#index
num_index = num.index(4)
monday_index = week.index("monday")
print(num_index)
print(monday_index)

# remove()
num.remove(2) #remove number 2
print(num)

# pop()
num.pop() # remove from the last index
num.pop(4) # remove index 4
print(num)

# del keyword
del num[1] # delete index 1
print(num)
del num  # delete num list
print(num) # num not defined




