'''
  **Pattern Module**
  *
 ***
*****
'''
n = int(input('enter the number of rows:'))
for i in range(1,n+1):
  print(' '*(n-i) + '*'*(2*i-1))

'''
  **Pattern Module**
*
**
***
'''
n = int(input('enter the number of rows:'))
for i in range(1,n+1):
  print('*'*i)

n = int(input('enter the number of rows:'))
for i in range(1,n+1):
  if i == 1 or i == n:
    print('* '*n)
  else:
    print('* ' + '  ' * (n - 2) + '*') 

# /* this is for hollow square pattern */
# for filling the spaces which to makee it as square i kept star with space after it
# and in the below line i kept space with space and any one side of star with one space
#  to make it equal to star with space after it



# * * * 
# * *
# *
# def prin_S(n):
#   if n == 0:
#     return
#   print(n * "* ")
#   prin_S(n-1)

# prin_S(int(input('Enter a number: ')))