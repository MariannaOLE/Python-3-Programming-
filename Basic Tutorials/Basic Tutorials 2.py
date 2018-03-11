
def isPalindrome(n):
    s = str(n)
    reverseString = ""
    
    for i in range (len(s) - 1, -1, -1):
        reverseString += s[i]

    return reverseString == s

# returns largest palindrome that is a multiple of two 3 digit numbers
# and returns -1 if no such palindrome exists
def findLargestPalindrome():
    palindrome = -1
    
    for i in range (999, 99, -1):
        for j in range (i, 99, -1):
            
            # if product is palindrome and is greater than last recorded palindrome
            if isPalindrome(i * j) and i * j > palindrome:
                palindrome = i * j
    return palindrome;

print (findLargestPalindrome())

def isPalindrome(num):
  numStr = str(num)
  numStrReverse = numStr[::-1]
  if numStr == numStrReverse:
    return True
  else:
    return False
  

  
  
  
  
  
  
  
  
  
  
