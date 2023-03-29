function solution(polynomial) {
    let list = polynomial.split(" + ")
    let x = 0;
    let num = 0;
    for (let i=0; i<list.length; i++){
        if(list[i].includes('x')){
            if(list[i].length!=1){
                x += Number(list[i].slice(0,-1));
            }
            else{x+=1;}
        }
        else{
            num += Number(list[i]);
        }
    }
    let answer;
    if (x==1 && num !=0){
        answer = 'x + '+num.toString()
    }
    else if (x==1 && num ==0){
        answer = 'x';
    }
    else if (x==0 && num !=0){
        answer = num.toString()
    }
    else if (x!=0&& num ==0){
        answer = x.toString()+'x'
    }
    else if (x!=0&&num !=0){
        answer = x.toString()+'x + '+num.toString()
    }
    else{
        answer = '';
    }
    return answer;
}