def solution(arr1, arr2):
    ll = len(arr1)
    nn = len(arr2)
    mm = len(arr2[0])
    answer = [[0]*mm for _ in range(ll)]
    
    for m in range(mm):
        for l in range(ll):
            for n in range(nn):
                answer[l][m] += arr1[l][n]*arr2[n][m]
                    
    return answer