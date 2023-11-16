function solution(number, limit, power) {        
    var answer = 0;
    for (let num=1; num<=number; num++) {
        let count = 0; 
        for (let i=1; i<=Math.sqrt(num); i++) {
            if (num%i === 0) count+=1;
        }
        count*=2;
        if (Math.sqrt(num) %1 ===0) count-=1; //중복제거
        if (count > limit) answer+=power;
        else answer+=count;
    }
    return answer;
}