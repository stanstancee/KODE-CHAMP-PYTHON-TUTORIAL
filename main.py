my_name = "Stanley"
def introduction():
  global my_name
  my_name = my_name + " Ifeoha"

  print("Hi, my name is {}".format(my_name))

introduction() 

def add(y):
  global x
  x = 10
  return x + y

add = add(20)
print(add)
print(x)