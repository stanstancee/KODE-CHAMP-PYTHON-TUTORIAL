#str
x = 24
y = 0.5
string_x = str(x) 
string_y = str(y)
print(string_x, string_y, sep=" + ") #outputs: 24 + 0.5
print(string_x  + string_y) #outputs: 240.5

#int
x = "50"
y = 8.9
integer_x = int(x)
integer_y = int(y)
print(integer_y) #prints 8
print(integer_y + integer_x) #prints 58

#floats conversion
x = "34"
y = 20
x = float(x) 
y = float(y)
print(x)       #prints 34.0
print(x - y)   #prints 14.0

#len
#len() cannot parse integers and floats, convert to strings before parsing
x , y , z = 1000, 33.89, "This is a string"
x , y = str(x) , str(y)
x,y,z = len(x), len(y) , len(z)
print(x) #outputs 4
print(y) #outputs 5
print(z) #outputs 16 : All character counted, including the spaces

