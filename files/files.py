with open('abc.txt','r+') as fo:
    gg = fo.readlines()
    for i in range(len(gg)):
        if gg[i]!='\n':
           # print(i,end='')
            gg[i]=gg[i][:len(gg[i])-2]
            print(gg[i])
        else:
            gg[i]=''
print('\n\n')


