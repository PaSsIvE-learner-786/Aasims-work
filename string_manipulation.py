# to replace the string value 
str = 'I am name from place'
string=str.replace('name','aasim')    #old string is not changd but a new string is created
new_str=string.replace('place','nepal')
print(new_str)


# To detect and replace the double space with single in the string
str = "this is a  simple  text"
print(str.replace("  "," "))

# To detecct the double space in the string
str = "this is a  simple text"
print(str.find("  "))

# escape sequence method
# letter = "Dear Harry,This Python course is nice.Thanks!"

letter = "Dear Harry,\n\tThis \"Python course\" is nice.\nThanks!"
print(letter)

# sum of the list 
a = [8, 9, 26, 59]
print(sum(a))

# count the number in the tuple and list
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))
b = [7, 0, 8, 0, 0, 0, 0, 9]
print(b.count(0))

# dictionary use 
dic ={
  "name" : 'ali',
  'age' : 20,
  'city' : 'karachi'
}
for i in dic:
  print(i,':',dic[i])

  