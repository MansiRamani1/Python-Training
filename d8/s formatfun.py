
a="welcome {} the {} board meeting".format("to","on")
print(a) 

a="welcome {0} the {1} board meeting".format("to","on")
print(a) 

a="welcome {1} the {0} board meeting".format("to","on")
print(a) 

a="welcome {1:11} the {0} board meeting".format("to","on")
print(a)

a="welcome {1:>11} the {0} board meeting".format("to","on")
print(a)

a="welcome {1:^11} the {0} board meeting".format("to","on")
print(a)
