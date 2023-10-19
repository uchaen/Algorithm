from collections import deque
def solution(people, limit):
    people.sort()
    deq = deque(people)
    answer=0
    while(deq):
        boat = deq.pop() #무거운사람 태움        
        if deq and boat+deq[0]<=limit:
            deq.popleft() #가벼운사람도 태움
        answer+=1

    return answer