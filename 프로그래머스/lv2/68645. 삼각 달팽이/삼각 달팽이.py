def solution(n):
    
    count=1
    answer = [[0]*i for i in range(1,n+1)]
    idx=0
    x,y=0,-1
    for d in range(n): #방향 /0 -1 `2
        for i in range(d,n):
            if d%3==0:
                y+=1
            elif d%3==1:
                x+=1
            else:
                x-=1
                y-=1
            answer[y][x]=count
            count+=1
    
    
    return [answer[i][j] for i in range(n) for j in range(i+1)]