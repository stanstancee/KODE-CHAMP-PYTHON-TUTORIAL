#This is a comment
#python will convert integer (whole number) to float to avoid data loss
x = 23.7
y = 19
sum = x + y # 23.7 + 19.0
print(sum) # 42.7

#python will convert any bool to an int using arithmetic ooperators on both
x = True
y = 1
sum = x + y # 1 + 4
print(sum) #prints 5

#python will not be implicitly convert in some cases like:
#suming int and string, or boolean and string
print("Hello" + 1) #raise type error
print(True + "False") # Raise type error