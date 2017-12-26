def stri14():
    a=input("enter a string saperated by commas : ")
    a=a.split(",")
    a.sort()
    for i in a:
        print(i+(" "),end="",flush=True),
