#continue statement for while loop
my_numbers = "123456789"
#sum all odd digits inside the string
# 1 + 3 + 5 + 7 + 9 = 25
sum = 0
n = 0
len_of_numbers = len(my_numbers)
while n < len_of_numbers:

  num = my_numbers[n]
  num = int(num)
  n = n + 1
  #if number is even, skip to the next loop
  if(num % 2 == 0):
    continue
  sum += num
  
print(sum)

# continue statement with for
# in the range of 0 to 19
# print out all numbers except 5, 10  and 15
numbers = range(20)
for num  in  numbers:
  if num == 5 or num == 10 or num == 15:
    print("skiped")
    continue
  print(num)

