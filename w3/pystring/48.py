def stri48():
    final=0
    while (final==0):
        s=input("Enter a number with a comma and a decimal : ")
        if(("," in s) and ("." in s)):
            final=1
        else:
            print("The number you entered does not contain both \",\" and \".\" \nTry again !!")
    com=s.find(",")
    dot=s.find(".")
    print(com)
    print(dot)
    b=""
    for i in range(len(s)):
        if(i==com):
            b+=s[dot]
        elif(i==dot):
            b+=s[com]
        else:
            b+=s[i]
    print(b)
    
