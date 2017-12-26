class Customer (object):
    def __init__(self,name,custid,gender,age):
        self.name=name
        self.custid=custid
        self.gender=gender
        self.age=age

    def display(self):
        print("Name of customer : ",self.name)
        print("Customer id  : ",self.custid)
        print("Gender : ",self.gender)
        print("Customer Age : ",self.age)

class Loan(Customer):
    def __init__(self,name,custid,gender,age,lid,lamount):
        super().__init__(name,custid,gender,age)
        self.lid=lid
        self.lamount=lamount

    def display(self):
        print("Loan id : ",self.lid)
        print("Loan Amount : ",self.lamount)
        print(self.name," has a loan of ",self.lamount)
        
