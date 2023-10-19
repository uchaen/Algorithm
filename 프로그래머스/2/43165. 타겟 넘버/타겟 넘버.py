def solution(numbers, target):
    global answer
    answer=0
    def dfs(idx, path):
        global answer
        if idx >= len(numbers):
            if sum(path)==target: answer+=1
            return
        
        dfs(idx+1, path+[numbers[idx]])
        dfs(idx+1, path+[-numbers[idx]])
            
    dfs(0,[]) 
    return answer