
a = 1
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
a = 5
b = 3
print(a//b) #floor divide
c = -3
print(abs(c))
a = -3
b = 5
c = 2.6
d = (a+b)
print (a/b)
a = 5 
b = float(a)
print(type(b))
c= 3.14
d = int(c)
print(d)
a = -3
b = 5
print(max(5,3))
a= 1+1j
b= 1-1J
print(type(a))
Pi = 3.14
R = 5
area = Pi * R**2

print(2*Pi*R)
s = 'hello coding girls'
print(type(s))
print(s)

saving = 1000
while saving<100000:
  print('work harder')
  saving = saving + 1000
  print('current saving is {}'. format(saving))
  print('financial freedom achieved')

my_friens = ['Lily', 'Lucy', 'Jessica']
print(help(my_friens.pop))
x = my_friens.pop(0)
print(x)
print(my_friens)
while len(my_friens)>0: 
  friend = my_friens.pop(0)
  print('Hello {}'.format(friend))
  print(my_friens)
  
  
age = 19

if age>= 21:
  print('Welome in')
else: print('Bye Bye')

year  = 2004
if year%400 == 0:
  print('{} is a leap year'.format(year))
elif year%4 ==0 and year%100 !=0:
  print('{} ia a leap year'.format(year))
else:
  print( '{} is not a leap year'.format(year))

l = list( range(1, 21, 2)) 
print(l)

m = 20 
while m>0:
  if m%2==0:
    print(m)
  m = m-1
  
limit = 20
num = 1 
while num<20:
  print(num)
  num = num + 1 
  
my_friens = ['lily', 'lucy', 'jean']  
for friend in my_friens:
  print("Hello {}".format(friend))

numbers = [2, 7, 11, 15]
target = 9 
for x in numbers:
  for y in numbers:
    if x+y ==target:
      print([numbers.index(x), numbers.index(y)])

numbers = [2, 7, 11, 15]
target = 9 
result = set()
for x in numbers:
  for lookFor in numbers:
    if x + lookFor == target:
      print(numbers.index(x), numbers.index(lookFor))
      
import random
counter = 0 
islucky = False

while not islucky:
  counter = counter + 1 
  pool = list(range(1,50))
  my_pick = set([])
  while len(my_pick) < 6:
    picked_number = random.choice(pool)
    my_pick.add(picked_number)
    
  pool_pick = set([]) 
  while len(pool_pick) < 6:
    picked_number = random.choice(pool)
    pool_pick.add(picked_number)
  if len(my_pick.intersection(pool_pick))>4:
   print('ok, Lucky!{}'.format(len(my_pick.intersection(pool_pick))))
   islucky = True
  else:
    print('You have sent {}'.format(counter))
    print('my_pick{}'.format(my_pick))

      






































