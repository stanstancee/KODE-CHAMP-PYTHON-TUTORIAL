#break inside simple while loop
x = 1
while x <= 10:
  print(x)
  if(x == 5):
    print("We have found 5. Goodbye!")
    break

  x += 1

i = 0
loading = True
while loading:
  i = i + 1
  if(i == 10):
    print("breaking....")
    break
  print("Loading....")
print("Goodbye!")


#break inside for loop
for val in "Stanley":
    if val == "l":
        break
    print(val)

print("The end")

#break inside for loop
one_to_twenty = range(34)
for val in one_to_twenty :
  mid_val = list(one_to_twenty)
  mid_val = len(mid_val)// 2
  if(val == mid_val):
    print(val,"breaking... mid-value reached")
    break
  print(val)
  

  
