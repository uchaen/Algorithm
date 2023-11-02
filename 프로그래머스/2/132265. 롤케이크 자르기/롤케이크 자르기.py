def solution(topping):
    chulsoo = dict()
    bro = dict()
    
    for t in topping:
        if t in bro:
            bro[t]+=1
        else:
            bro[t]=1

    result = 0
    for t in topping:
        if len(chulsoo)==len(bro):
            result+=1
        if t in chulsoo:
            chulsoo[t]+=1
        else:
            chulsoo[t]=1
        bro[t]-=1
        if bro[t]==0: del bro[t]
    
    
    return result