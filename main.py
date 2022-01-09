#for loop
small_letters = ["a", "b", "c", "d", "e"]
for letter in small_letters:
  print(letter.upper())

words = ["see", "another","end", "down", "inside"]
vowels = ["a", 'e', "i", "o", "u"]
for word in words:
  x = word[0] in vowels
  if x:
    print(word, " is a vowel" )
  else:
    print(word, " is a consonant")

#while loop
words = ["see", "another","end", "down", "inside"]
x = 0
while x < len(words):
  print(words[x])
  x += 1

words = ["see", "another","end", "down", "inside"]
y = 0
while y < len(words):
  print(words[y]+ " at index " + str(y))
  y += 1




