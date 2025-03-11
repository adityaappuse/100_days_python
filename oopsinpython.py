class Register:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"{self.name}\t{self.age}")
a=Register("Aditya",23)
b=Register("Frentzen",24)
a.info()
b.info()



