def generate_table(i):
  table = ""
  for j in range (1,11):
    table += (f"{i} X {j} = {i*j}\n")
  with open(f"table_of_{i}.txt","a") as f:
    f.write(table)

for i in range (2,21):
  generate_table(i)

i = int (input('Enter which table you want to see (2-20): '))
with open (f"table_of_{i}.txt","r") as f:
  print(f.read())

# def generate_table(i):
#   for j in range (1,11):
#     m = (f"{i} X {j} = {i*j}")
#     with open(f"table_of_{i}.txt","a") as f:
#       f.write('\n')
#       f.write(str(m)) 

# for i in range (2,21):
#   generate_table(i)

# i = int (input('Enter which table you want to see (2-20): '))
# with open (f"table_of_{i}.txt","r") as f:
#   print(f.read())