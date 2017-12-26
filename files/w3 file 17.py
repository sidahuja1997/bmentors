with open('abc.txt','r+') as files:
    a=files.readlines()
    print(a)
    for i in range(len(a)):
        a[i]=a[i].split('\n')

        b=a[i][0]
        a[i]=b
    files.writelines(a)

    print(a)
