function accum(s){
    const result=[]
    const newWords = s.toLowerCase()

    for (let i=0; i<newWords.length; i++){
        let str=newWords[i].toUpperCase()
        for(let j=0; j<i;j++){
            str+=newWords[i]
        }
        result.push(str)
    }

    return result.join("-")
}

console.log(accum("ZpglnRxqenU"))

function inter(s1, s2){
    return s1.filter(x=>s2.includes(x));
  }

console.log(inter(["A","B"],["B","C"]))