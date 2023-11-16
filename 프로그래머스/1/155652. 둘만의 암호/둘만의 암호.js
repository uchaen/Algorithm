function solution(s, skip, index) {
    let alphabet = []
    const skiparr = [...skip]
    for (let i =0; i<26; i++){
        const temp = String.fromCharCode(97+i)
        if (!skiparr.includes(temp)) alphabet.push(temp);
    }
    const sarr = [...s]
    var answer = '';
    for (let i =0; i<sarr.length; i++){
        let idx = alphabet.indexOf(sarr[i]);
        answer += alphabet[(idx+index)%alphabet.length]
    }
    
    return answer;
}