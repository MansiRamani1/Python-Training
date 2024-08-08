a="welcome"
print(a.isalpha())#True
print(a.isalnum())#True

a="welcome123"
print(a.isalpha())#False
print(a.isdigit())#False
print(a.isalnum())#True

a="2805"
print(a.isdigit())#True
print(a.isalnum())#True

a="mansi@gmail"
print(a.isalnum())#False
