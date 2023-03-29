function solution(a) {
    var answer;
    if ((a[0]-a[1])==(a[1]-a[2])){ //등차수열
        answer = a[a.length-1]+(a[2]-a[1]);
    }
    else{//등비수열
        let r = a[1]/a[0];
        answer = a[a.length-1]*r
    }
    return answer;
}