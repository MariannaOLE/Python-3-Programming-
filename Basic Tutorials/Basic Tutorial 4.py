def isSureWin (n):
  if n in [1, 2, 3]:
   return True
  elif n == 4:
    return False
  else:
    if isSureWin(n-1) and isSureWin(n-2 and isSureWin(n-3)):
      return False
    else:
      return True
    
def play():
  for n in range(1, 101):
    print(n, isSureWin(n))
    
play()


  
  
  
  
  
  
  
  
  
  