// Task-1

// function disemvowel(str) {
//     newWords=str.replace(/[aeiou]/gi,'');
//     return newWords;
//   }
// console.log(disemvowel("This website is for losers LOL!"))

// Task-2
function squares(x, n){
    const info__lst=[]
    for ( i = 1; i<n+1; i++){
        if (i<=2){
        first = x**i;
        info__lst.push(first);
    }
        else if (i<=3){
            second=info__lst[1]**2;
            info__lst.push(second);
        }
        else if (i<=4){
            third=info__lst[2]**2;
            info__lst.push(third);
        }
        else if (i>=5){
            fourth=info__lst[3]**2;
            info__lst.push(fourth);
        }
        else if (i<=6){
            f=info__lst[4]**2;
            info__lst.push(f);
    }
}
    return info__lst 

}
console.log(squares(2,6))

// Task-3
// function reverseWordsForLoop(str) {
//     let newString = ""
//     for (let i = str.length - 1; i >= 0; i--) {
//       newString += str[i];
//     }
//     return newString;
//   }

// console.log(reverseWordsForLoop("lama"))