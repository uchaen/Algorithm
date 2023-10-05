from itertools import permutations as pm

def solution(k, dungeons):
    n= len(dungeons)
    tmp = list(pm([i for i in range(n)],n))
    
    answer=0
    for idxs in tmp:
        res=0
        now=k
        for i in idxs:
            if dungeons[i][0] <= now:
                res+=1
                now-=dungeons[i][1]
        # print(idxs,res)
        answer=max(answer,res)  
    
    return answer