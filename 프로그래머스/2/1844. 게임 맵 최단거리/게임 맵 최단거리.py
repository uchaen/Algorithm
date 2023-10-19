from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    deq = deque([(0,0,1)])
    maps[0][0]="@"
    
    while deq:
        x,y,c = deq.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<n and 0<=yy<m and maps[xx][yy]==1:
                maps[xx][yy]=c+1
                if xx==n-1 and yy==m-1: return c+1
                deq.append((xx,yy,c+1))

    return -1