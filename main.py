# infinite loop with  python generators
def all_even():
    n = 0
    while True:
        yield n
        n += 2

for i in all_even():
  print(i)

#pipeline generators
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
 
def square(nums):
    for num in nums:
        yield num**2

fib = fibonacci_numbers(10)
my_square = square(fib)
print(my_square)
for i in my_square:
  print(i)

#factorial
# fn = fn - 1
def fac(num):
  add = 1
  for i in range(1,num + 1):
    add = add * i
    yield add

x = 1
for i in fac(10):
  print( "factorial of ", x  ," is ", i)
  x += 1
    
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


def infinite_sequence():
  num  = 0
  while True:
    yield num
    num += 1

for i in infinite_sequence():
  pal = is_palindrome(i)
  if pal:
    print(i)



    


