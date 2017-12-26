def stri25(a):
    b=""
    d={"x":"a","y":"b","z":"c"}
    for i in a:
        if(i=="x"):
            b+="a"
        elif(i=="y"):
            b+="b"
        elif(i=="z"):
            b+="c"
        elif(i==" "):
            b+=" "
        else:
            b+=chr(ord(i)+3)
    return b
def ntstri25(a):
    b=""
    for i in a:

        b+=chr(ord(i)-3)

    return b
