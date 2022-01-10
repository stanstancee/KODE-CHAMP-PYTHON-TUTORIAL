# using for
week = {1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wednesday', 5: 'thursday', 6: 'friday', 7: 'saturday'}

for day in week:
  print(day)

abbr = ("st", "nd", "rd", "th")
for day in week:
  day_abbr = str(day)+ abbr[(day-1)] if day < 4 else str(day)+ abbr[-1]
  print(day_abbr , " day is " , week[day] )
  """
1st  day is  sunday
2nd  day is  monday
3rd  day is  tuesday
4th  day is  wednesday
5th  day is  thursday
6th  day is  friday
7th  day is  saturday
 """