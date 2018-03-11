
def isPalindrome(num):
  numStr = str(num)
  numStrReverse = numStr[::-1]
  if numStr == numStrReverse:
    return True
  else:
    return False
  
def findLargest():
  for num1 in range(100, 1000):
    for num2 in range(100. 1000):
      product = num1 * num2
      if isPalindrome(product):
        large = max(large, product)
  print(large)
  
findLargest()
  
  
  
  
  
  
  
  
  
  