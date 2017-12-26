import sqlite3

conn=sqlite3.connect("stud.db")
c=conn.cursor()


class STUDENT(object):
    def __init__(self):
        self.rollno=0
        self.clas=0
        self.name=""
        self.id=0
        
    def getdata(self):
        self.rollno=int(input("Enter the roll number : "))
        self.name = (input("Enter Name : "))
        self.clas = (input("Enter Class : "))
        self.id = int(input("Enter ID : "))
        
        self.display()

    def display(self):
        print("Roll number : ",self.rollno)
        print("ID : ",self.id)
        print("Name : ",self.name)
        print("Class : ",self.clas)


def stu():
    create_table()
    b=0
    d=dict()
    n=int(input("Enter the number of students whose data you want to store : "))
    while(b<n):
        s=STUDENT()
        s.getdata()
        s.display()
        a=input("If the data entered is correct and you want to commit it to the database, press y, else press n : ")
        if(a in  ['y','Y']):
            d[s.id]=[s.rollno,s.name,s.clas]
            data_entry(s.rollno,s.id,s.name,s.clas)
            print("Value committed!")
            b+=1
        else:
            pass
    choice=input("Enter y for deleting a record from the database : ")
    if(choice in ['y','Y']):
        del_dat()
    Print(d)


def Print(d):
    for i in d.keys():
        print(i ," : ",d[i])
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS student(Roll_no REAL,Id REAL, Naam TEXT,Class REAL )")
def data_entry(a,b,e,d):
    '''e = e.split()
    e = e[0] + "_" + e[1]'''
    qry="INSERT INTO student VALUES(%s,%s,'%s',%s)"%(str(a),str(b),str(e),str(d))
    print(qry)
    c.execute(qry)
   # c.execute("INSERT INTO student VALUES(?,?,?,?)",(a,b,e,d))

    conn.commit()

def del_dat():
    col=input("Enter the column name for condition : ")
    col=col.title()
    print(col)
    val=input("Enter the value that would be equated for column : ")
    print(val)




    c.execute("DELETE FROM student WHERE "+col+"="+val)
    conn.commit()


stu()
