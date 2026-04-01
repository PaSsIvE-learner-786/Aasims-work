num = int(input('enter any number you want to prinnt table of:'))
for i in range (1,11):                  # you can also use range (10) and replace i with i+1
  output=(f"{num} x {i} = {num * i}")
  with open('C:\\Users\\asus\\Desktop\\codings\\python\\Python Programs\\table_creater\\table.txt','a') as f:
    f.write(output)
    f.write('\n')
with open('C:\\Users\\asus\\Desktop\\codings\\python\\Python Programs\\table_creater\\table.txt','a') as f:
  f.write('------------------------')
  f.write('\n')