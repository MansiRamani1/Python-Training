try: 
    number = int("abc")
except ValueError as e:
    print("ValueError")
    print(e.__class__)