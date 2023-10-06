def solution(n, words):
    tmp =[]
    for idx,w in enumerate(words):
        if not tmp:
            tmp.append(w)
            continue
        if tmp[-1][-1] != w[0] or w in tmp: #탈락
            return [idx%n +1, int(idx/n) +1]
        else:
            tmp.append(w)
    return [0,0] #탈락자x