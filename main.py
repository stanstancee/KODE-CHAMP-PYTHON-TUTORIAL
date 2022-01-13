# function args positional argument
def my_average(*args):
  my_len = len(args)
  average = sum(args) // my_len
  return average
  

print(my_average(23, 45, 56)) # 41

def area(*args):
  base , height = args
  calc = 1/2 * (base * height)
  print("Area of the triangle = {}".format(calc))

area(29,4)

def force(**kwargs):
  # unpacking variables
  m, v, u, t = kwargs.values()
  a = (v - u)/t
  f = m * a
  return "force = {}N".format(f)

"""
Mass of the body, m = 3 kg
Initial speed of body, u = 2 m/s
Final speed of body, v = 3.5 m/s
Time, t = 25 s
"""
force = force(m = 3, v = 3.5, u = 2, t = 25)
print(force)