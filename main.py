#count 1 to 100
count = 1
while count <= 100: 
  print(count) #for each loop, print count
  count += 1 #increase count by 1.


x = 1
while x <= 12:
  product = 2 * x #for each loop multiply x by 2
  print("2 x {} = {}".format(x, product)) #print to screen
  
  x += 1 # add 1 to x for every loop.

# while/else block
downloading = True
perc = 0

while downloading and perc < 100 :
  print("downloading " + str(perc) + "%")
  if(perc > 70):
    print("Almost done")
  perc = perc + 10
else:
  print("download completed")