def solution(n):
    fs =[0]
    fs.append(1)
    for i in range(2,n+1):
        fs.append(fs[i-1]+fs[i-2])
    
    return fs[n]%1234567