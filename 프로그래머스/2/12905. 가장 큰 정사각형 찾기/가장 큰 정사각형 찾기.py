def solution(board):
    n = len(board[0])
    m = len(board)
    answer = 0
    
    if m==1:
        if 1 in board[0]: return 1
        else: return 0
    if n==1:
        for i in range(m):
            if board[i][0]: return 1
        return 0       
            
    for i in range(1,m):
        for j in range(1,n):
            if board[i][j]==1:
                board[i][j] = min(board[i-1][j-1],board[i][j-1],board[i-1][j]) +1
            answer = max(answer,board[i][j])    

    return answer**2