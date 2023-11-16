function solution(today, terms, privacies) {
    let termsdic = {};
    for (const term of terms){
        const tmp = term.split(" ");
        termsdic[tmp[0]] = tmp[1];
    }
    
    const todayDate = new Date(today);
    var answer = [];
    for (let i=0; i<privacies.length; i++) {
        const tmp = privacies[i].split(" ");
        const tmpDate = new Date(tmp[0]);
        tmpDate.setMonth(tmpDate.getMonth() + Number(termsdic[tmp[1]]));
        if(tmpDate <= todayDate) 
            answer.push(i+1);
    }
    
    return answer;
}