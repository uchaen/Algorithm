def solution(files):
    answer = []
    for file in files:
        findnumber = False
        nidx,tidx=0,0
        for idx,f in enumerate(file):            
            if not findnumber and f.isdigit(): #number시작
                nidx = idx
                findnumber = True
            elif findnumber and not f.isdigit(): #tail시작
                tidx = idx
                break
        if tidx>0:
            answer.append([file[:nidx],file[nidx:tidx],file[tidx:]])
        else:
            answer.append([file[:nidx],file[nidx:],""])
                
    answer.sort(key=lambda x: (x[0].lower(),int(x[1])))
    return ["".join(a) for a in answer]