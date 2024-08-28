class Person:

    name="Mansi"
    std="MSc.IT"
    sub="Python"

    def info(self):
        print(f"{self.name} in a {self.std}")

a=Person()
print(a.name,a.std)
a.name="army"
a.std="MCA"
a.info()