function solution(name, yearning, photo) {
    var answer = [];
    let dic ={};
    for (let i =0; i<name.length; i++){
        dic[name[i]] = yearning[i]
    }
    for (let i =0; i<photo.length; i++) {
        let tmp=0;
        for (let j=0; j<photo[i].length; j++) {
            if (photo[i][j] in dic) tmp += dic[photo[i][j]];            
        }
        answer.push(tmp);
    }
    return answer;
}