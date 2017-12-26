import csv
path="output.csv"

data = ['First Name, Last Name'.split(","),'Sachin, Tendulkar'.split(","),'Virat, Kohli'.split(","),'MS, Dhoni'.split(","),'John, Cena'.split(",")]

def csvwrite(data,path):
    files=open(path,"w",newline='')
    writer=csv.writer(files, delimiter=',')
    for row in data:
        writer.writerow(row)

csvwrite(data,path)

