age_x = 20
age_y = 15
height_x = 5
height_y = 6

print((age_x > age_y) and (height_x > height_y)) # prints False

print((age_x < age_y) or (height_x < height_y)) # prints True

print((age_x < age_y) and (height_x > height_y)) # prints False

print((age_x < age_y) or (height_x > height_y)) # prints False

print(not (age_y > age_x)) #True

print(not (age_x > age_y) and (height_x > height_y)) #False

print((not (age_x > age_y) and (height_x > height_y)) or (age_x > age_y)) #True
