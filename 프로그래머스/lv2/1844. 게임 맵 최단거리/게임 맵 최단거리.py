def solution(maps):
    n=len(maps)
    m=len(maps[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=[(0,0,1)]
    
    while que:
        i,j,c = que.pop(0) # 제일먼저 들어온애 pop
        
        for k in range(4):
            xx = i + dx[k]
            yy = j + dy[k]
            if 0<=xx<n and 0<=yy<m and maps[xx][yy]==1:
                if xx==n-1 and yy==m-1: return c+1
                maps[xx][yy] = -1 #방문체크
                que.append((xx,yy,c+1))
            
    return -1