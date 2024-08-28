class Account:

    def __init__(self,accno,passacc):
        self.accno=accno
        self.__passacc=passacc

    # def reset_pw(self):
    #     print(self.__passacc)


acc1=Account(123456,45677)

print(acc1.accno)
print(acc1.passacc)
# print(acc1.reset_pw())