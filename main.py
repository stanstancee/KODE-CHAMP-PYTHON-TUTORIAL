# function
def print_word():
  print("I love python !")

print_word()
print_word()

#passing parameters
def print_x_times(x):
  for i in range(x):
    print("I love python !")

print_x_times(20)

#return
def add(x,y):
  return x + y
print(add(10,23))

# functions inside function
def apply_twice(binary, x , y):
    return binary(binary(x,y), binary(x,y))

def add(x,y):
    return x + y 

print(apply_twice(add, 4,4))




