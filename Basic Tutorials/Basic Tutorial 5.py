import datetime

dt = datetime.date.today()
print(dt)

#tm = datetime.datetime.now()
#print(tm)

print(dt, type(dt))
print(dir (dt))

print(dt.weekday())
print(help(dt.replace))

x = dt.replace(year = 2020)
print(x)

print(help(dt.isoformat))
print(dt.isoformat())



  
  
  
  
  
  
  
  
  
  