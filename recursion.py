def fact(n):
  if n==1 or n==0:
    return 1
  return n*fact(n-1)
n = int(input("Enter a number: ")) # or you can use n as variable instead of f
print(fact(n)) # and you can use fact(n) instead of fact(f)
