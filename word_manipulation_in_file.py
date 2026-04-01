# # # # # with open ("donkey.txt","r") as f :
# # # # #   content= f.read().lower()

# # # # # content_new=content.replace("donkey","do###y") # or content_new=content.replace("donkey","######")

# # # # # with open("donkey.txt","w") as f :
# # # # #   content= f.write(content_new)

 
# # # # words = ["donkey","monkey","pornky","ganda"]

# # # # with open ("donkey.txt","r") as f :
# # # #   content= f.read().lower()

# # # # for word in words:
# # # #   content = content.replace(word,"#"*len(word)) 

# # # # with open("donkey.txt","w") as f :
# # # #   content= f.write(content)
  

# # # line_no = 1
# # # with open ("log.txt","r") as f :
# # #   content= f.readlines()

# # # for line in content:
# # #   if 'python' in line:
# # #     print(f'your python is present in line {line_no}')
# # #     break
# # #   line_no +=1
# # # else : 
# # #   print('your pyhton is not present ')


# # ## wiping out the contents form a file
# # with open('log.txt','w') as f:
# #   f.write('')


# ## rename a file using python 
#1. import os

# old_name= "Oldfile.txt"
# new_name= "rename_by_python.txt"
# os.rename(old_name,new_name)

# or copy the content and paste in the new the new name and boom renamed