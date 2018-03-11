l = [ 1, 2, 0, 5, 6]

for num in l:
  try:
    print( 6/num)
  except: 
    print( 'skipping {} and goes on'. format( num))
  finally:
    print('finished processing {}'. format(num))
    
l = [ 1, 2, 0, 5, 6]  
l.sort()
print(l)
p = sorted(l)
print(p)


limit =1000
total = 0
for num in range(1, limit):
  if (i%3 == 0 or num%5 == 0):
    total = total + num
print(total)
