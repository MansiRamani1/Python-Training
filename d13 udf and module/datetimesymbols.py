import datetime

x=datetime.datetime.now()
m=x.strftime("%Y")#return full year 2024 
print(m)
print()

x=datetime.datetime.now()
print(x.strftime("%y"))#return number of recent year 24
print(x.strftime("%m"))#month
print(x.strftime("%H"))#recent hour according 24 hour


