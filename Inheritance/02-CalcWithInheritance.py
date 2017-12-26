class Calculator:
    "This is a calcuator demo"

    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 0


class Add(Calculator):

    def __init__(self):
        super().__init__()

    def sum(self):
        self.c = self.a + self.b
        print("Sum is : ",self.c)


class Sub(Calculator):
    
    def __init__(self):
        super().__init__()
        self.a = 12
        self.b = 14
        self.c = 0

    def sub(self):
        self.c = self.a - self.b
        print("Sum is : ",self.c)


obj_1 = Add()

obj_1.sum()

obj_2 = Sub()

obj_2.sub()
