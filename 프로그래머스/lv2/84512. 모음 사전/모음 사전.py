def solution(word):
    dic={'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    tmp = [781, 156, 31, 6, 1]
    answer = 0
    for idx,w in enumerate(word):
        answer +=  dic[w] * tmp[idx] + 1

    return answer