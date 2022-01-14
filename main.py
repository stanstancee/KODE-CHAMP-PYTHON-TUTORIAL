#Recursion
"""
4! = 4 * 3!
n! = n * (n- 1)
"""
def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(4))
# using recursion , sum all numbers 1 - 10
def sum(num):
  if num > 0:
    return num + sum(num - 1)
  else:
    return 0
print(sum(10))
for i in range(1,101):
  print(i, sum(i))

# sum of all elements in a list raised to the power of 2.
#[2,3,4,5] = [4,9,16,25] = 4 + 9 + 16 + 25 =  54
def calc(list):
    if len(list) == 0:
        print("break")
        return 0
    else:
        result =  list[0]**2 + calc(list[1:])
        return result 

list = [2,4,4,3]
x = calc(list)        
print(x)

#fibonacci sequence
fib_list = []
def fib(index):
  if index <= 1:
    return index
  else:
   fn =  fib(index - 1)+ fib(index - 2)
   return fn
n = int(input("Please enter a positive integer: "))

if n <= 0:
  print("Please enter a positive integer")
else:
  for i in range(1,n+ 1):
    fib_list.append(fib(i))
print(fib_list)

