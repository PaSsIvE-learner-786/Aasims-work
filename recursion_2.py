def sum(n):
  # print(n)
  if n ==1 :
    return 1
  return sum(n-1) + n
print(sum(int(input("Enter a number: "))))


n = int (input("Enter a number: "))
def odd_even(n):
  if n%2==0:
    print ( "even")
  else:
    print("odd")
  if n==0:
    return  
  odd_even(n-1)
  print(n) 

odd_even(n)