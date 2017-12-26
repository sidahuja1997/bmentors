def stri6(a):
    if(not(len(a) <=3)):
        if(a[(len(a)-3):]=="ing"):
            a+="ly"
        else:
            a+="ing"
    else:
        pass
    print(a)
    
    
