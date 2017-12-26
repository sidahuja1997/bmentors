class A:

    def __init__(self):
        self.name = "Ram"

    def display(self):
        print("Hello World")


class B(A):

    def __init__(self):
        super().__init__()

    def display(self):
        print(self.name)
        print("Bye World")


class C(A):

    def __init__(self):
        super().__init__()

    def display(self):
        print(self.name)



a = A()
b = B()

c = C()

b.display()
c.display()
