class Person:

    def __init__(self):
        self.name = ""
        self.category = ""
        self.email = ""


class Employee(Person):

    def __init__(self):
        super().__init__()
        self.category = "Employee"

    def display(self):
        print(self.name, "is a", self.category)


class Customer(Person):

    def __init__(self):
        super().__init__()
        self.category = "Customer"

    def display(self):
        print(self.name, "has a",self.email)


emp = Employee()
emp.name = "Ram"

emp.display()


cust = Customer()
cust.name = "Shyam"
cust.email = "shyam@gmail.com"

cust.display()
