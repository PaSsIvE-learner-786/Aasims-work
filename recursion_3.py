def print_list(l, idx):
  if idx == len(l):
    return

  print(l[idx])
  
  print_list(l, idx+1)

print_list([1,'tree','56',433,'hello'],0)
