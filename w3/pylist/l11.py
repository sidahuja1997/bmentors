def l11(l,m):
    flag=0
    if(len(l)>len(m)):
        step=l
        pest=m
    else:
        step=m
        pest=l
    for i in step:
        if(i in pest):
            flag=0
            return True
            break
        else:
            flag+=1
    if(flag==len(step)):
        return False

        
    
