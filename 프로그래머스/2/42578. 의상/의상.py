from itertools import combinations as cb
def solution(clothes):
    dic = {}
    keys = []
    for cl in clothes:
        if cl[1] in dic:
            dic[cl[1]]+=1
        else:
            keys.append(cl[1])
            dic[cl[1]]=1

    answer = 1
    for k in keys:
        answer *= (dic[k]+1)
    
    return answer - 1