from collections import deque

def solution(n):
    deq = deque([])
    answer = 0
    
    for i in range(1,n+1):
        deq.append(i)
        while sum(deq) > n:
            deq.popleft()        
        if sum(deq) == n: answer+=1
            
    return answer