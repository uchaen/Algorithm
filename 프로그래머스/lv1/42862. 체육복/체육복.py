def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for l in lost[:]: #도난당하면 빌려줄수없음
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
            
    for l in lost[:]:
        if l-1 in reserve:
            reserve.remove(l-1)
            lost.remove(l)
        elif l+1 in reserve:
            reserve.remove(l+1)
            lost.remove(l)
        
    return n - len(lost)