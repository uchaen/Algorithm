def solution(answers):
    il = [1, 2, 3, 4, 5]
    ee = [2, 1, 2, 3, 2, 4, 2, 5]
    sam = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ilpo, eepo, sampo = 0,0,0
    for idx,a in enumerate(answers):
        if il[idx%5] == a: ilpo+=1
        if ee[idx%8] == a: eepo+=1
        if sam[idx%10] == a: sampo+=1
    ans = []
    m = max(ilpo,eepo,sampo)
    if ilpo == m: ans.append(1)
    if eepo == m: ans.append(2)
    if sampo == m: ans.append(3)
    return ans