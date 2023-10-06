import heapq
def solution(scoville, K):
    if K==0: return len(scoville)
    heapq.heapify(scoville) #O(n)
    if scoville[1]==0: return -1
    
    count = 0
    while scoville[0] < K:
        if len(scoville)<=1: return -1 #완성전 1개남음
        tmp = heapq.heappop(scoville) + 2*heapq.heappop(scoville) #O(logn)
        count+=1
        heapq.heappush(scoville, tmp) #O(logn)
        
    return count