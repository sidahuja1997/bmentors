class student(object):
    
    def __init__(self):
        self.rollno=0
        self.name=""
        self.maths=0
        self.english=0
        self.science=0
        self.data=[self.rollno,self.name,self.maths,self.english,self.science]
        
    def get_data(self):
        self.rollno=int(input("Enter the roll number : "))
        self.name=input("Enter name : ")
        self.maths=int(input("Enter mathematics marks : "))
        self.english=int(input("Enter english marks : "))
        self.science=int(input("Enter science marks : "))
        self.data=[self.rollno,self.name,self.maths,self.english,self.science]
        self.data=[self.data]
    def display(self):
        print("\nroll number : ",self.rollno)
        print("\nname : ",self.name)
        print("\nenglish marks : ",self.english)
        print("\nmathematics marks : ",self.maths)
        print("\nscinece marks : ",self.science)
    def csvwrite(self):
        import csv
        path="student.csv"
        files=open(path,"a",newline='')
        writer=csv.writer(files,delimiter=',')
        for row in self.data:
            writer.writerow(row)
def studentcsv():
    
    
    n=int(input("Enter the number of students you want to enter in the excel file : "))
    for i in range(n):
        s=student()
        s.get_data()
        s.display()
        s.csvwrite()
studentcsv()
