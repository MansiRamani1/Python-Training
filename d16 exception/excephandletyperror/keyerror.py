try: 
  dict1={'a':1,'b':2}
  print(dict1['c'])
except KeyError as e:
  print("c is not available")
  print(e.__class__)

