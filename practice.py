# a=input('Enter a string Introduction:')
# b=int(input('Enter a integer 2:'))
# c=input('Enter a string python:')
# result = (a +' '+ str(b)+' '+ c)
# print (result)


# list = ['apple', 'banana', 'cherry', 'date', 'apple', 'banana']
# list.remove('banana')
# print(list)

# list = ['apple', 'banana', 'cherry', 'date', 'apple', 'banana']
# egg = list
# list.remove('banana')
# print(egg)

# import copy
# list = [[1,2],[3,4],[5,6]]
# list2 =copy.copy(list)
# list3 =copy.deepcopy(list)
# list[0].remove(2)
# print(list)
# print(list2)
# print(list3)


# class rectangle:
#   def __init__(self,w,h):
#     self.width=w
#     self.height=h
#   def  grow_rectangle(self,w,h):
#     self.width+=w
#     self.height+=h

# box=rectangle(60,80)
# box.grow_rectangle(40,20)
# print(box.width,box.height)


# class rectangle:
#   def __init__(self,w,h):
#     self.width=w
#     self.height=h
# class point:
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y

# def find_center(rec):
#   x=rec.corner.x + rec.width//2
#   y=rec.corner.y + rec.height//2
#   return (x,y)

# box=rectangle(60,80)
# box.corner=point(4,6)
# center =find_center(box)
# print(center)


# import sys,pyperclip

# text = {'agree':'message 1','busy':'message 2'}
# if len(sys.argv) < 2:
#   print('Usage: python mclip.py [keyphrase] - copy text to clipboard')
#   sys.exit()
# else:
#   keyphrase = sys.argv[1]
# if keyphrase in text:
#   pyperclip.copy(text[keyphrase])
#   print('Text for ' + keyphrase + ' copied to clipboard.')
# else:
#   print('There is no text for ' + keyphrase)



from pathlib import Path

Path("C:/Users/AI") / 'accounts.txt' / 'details.csv' #atleast one should be path object 

base = Path("C:/Users/AI")   
files = ['accounts.txt', 'details.csv', 'invite.docx']
for f in files:
    print(base / f)

print(Path.cwd())
print(Path.home())
