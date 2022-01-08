# with copy function
week = ["sunday","monday","tuesday", "wednesday", "thursday", "friday", "saturday"]
my_list = week.copy()
print(my_list)

#with list
another_list = list(week)
print(another_list)

#list comprehension
new_list = [ week[:3] for week in week]
print(new_list)

nums = [x for x in range(1,11,3)] 
print(nums) # [1, 4, 7, 10]

sequence = [x for x in range(20) if not x % 2] #even numbers 0 - 20
print(sequence) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
