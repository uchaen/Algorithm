def solution(s):
    op=0
    for ss in s:
        if ss=="(": op+=1
        else: op-=1
        if op<0: return False
    
    if op==0: return True
    else: return False