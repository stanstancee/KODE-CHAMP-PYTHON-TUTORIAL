# dictionaries
# empty dictionary
elements = {}
week = {1:"sunday", 2:"monday", 3:"tuesday", 4:"wednesday", 5:"thursday", 6:"friday", 7:"saturday"}
print(week)

elements["hydrogen"] = 1
elements["helium"] = 2
elements["carbon"] = 6
print(elements)

#indexing
helium = elements["helium"]
second_day = week[2]
print(second_day) # monday
print(helium) # 2

""" using get() """
week_3 = week.get(3)
week_none = week.get(23)
print(week_3 , week_none, sep="\n") # tuesday , None