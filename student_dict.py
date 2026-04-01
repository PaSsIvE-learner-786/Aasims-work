l=[]
d={}
n=int(input("Enter number of students: "))
key = ['name', 'age','department', 'marks']
for i in range(n):
  dict_name=f"student_{i+1}"
  d[dict_name]={}
  for j in key:
    value=input(f"Enter {j} of student {i+1}: ")
    d[dict_name][j]=value
  l.append(d[dict_name])
print(l)