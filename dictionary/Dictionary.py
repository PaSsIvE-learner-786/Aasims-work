dictionary = { 
  "cat" : "small animal",
  "dark" : "no light"  ,
  "money" : "valuable item used for trading ",
  "integer":[1,2,3]
}
l = len(dictionary)
n = 1

while n <= l: 
  ask = input('if you want to find meaning yes type Y/y no type N/n:')

  if (ask == 'Y' or ask == 'y'):
    user = input('type the word here for meaning :')
    print(user,':', dictionary.get(user))
    
# to continuing the loop until the words are finished
    if user in dictionary:
      n+=1 
  

  elif (ask == 'N' or ask == 'n'):
    print('thankyou for using us!')
    break
  
  else:
    print('invalid input')
    break

else:
  print('the words are finished')

