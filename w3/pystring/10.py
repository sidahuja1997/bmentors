def stri10():
    a=input("enter a string to swap first and last characters")
    n=len(a)
    a=a[n-1:]+a[1:n-1]+a[:1]
    return a
