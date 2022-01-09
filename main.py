# slicing
cities = ("Ikeja", "Asaba", "Benin" , "Ibadan", "Lokoja" , "Jos")
# from index 3 to index 5 (5 not included)
three_to_five = cities[3:5]
print(three_to_five ) # ('Ibadan', 'Lokoja')
# from 2 till the end
two_till_end = cities[2:]
print(two_till_end) # ( 'Benin' , 'Ibadan', 'Lokoja' , 'Jos')
#from start to 5
start_to_five =  cities[:5]
print(start_to_five) # ('Ikeja', 'Asaba', 'Benin' , 'Ibadan', 'Lokoja' )

# tuple unpacking
dimensions = 20 , 6 , 50
length, width , height = dimensions
product = length * width * height 
print(length) # 20
print(height) # 50
print(product) #6000
#imutability
dimensions[0] = 40 #TypeError
print(dimensions)