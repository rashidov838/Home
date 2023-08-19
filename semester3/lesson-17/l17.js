// function userInfo(name,password="secret"){
//     star="*"
//     newword=password.replace(/[qwertyuiopasdfghjklzxcvbnm]/gi,"*")
//     return `Your name is ${name} and your password ${newword}`
// }
// console.log(userInfo()) 


// Function expression()


// (function (day){
//     if (day==="Wednesday"){
//         return true;
//     }
//     return false;

// });


// const isWednsday=function(day){
//     if(day=== "Wednesday"){
//         return true;
//     }
//     return false;
// };
// console.log(isWednsday("Wednesday"));

// Arrow Function

// const rectangleArea=(width,height)=>{
//     let area=width*height;
//     return area;

// }

// console.log(rectangleArea(34,23))




// const dummy=(singleParagm)=>singleParagm+12;
// console.log(dummy(12))


// 
// const dummy =(singleParagm) =>{
//     if (singleParagm){
//         return true;
//     }
// }
// console.log(dummy(12))

// const rectangleArea=(width,height)=>{
//     let area=width*height;
//     return area;

// }


// const gameRPS=(user1,user2)=>{
//     if (user1==="Rock" && user2==="Scissors"){
//         return `Rock destroys scissors. Winner is user1`
//     }
//     else if (user1==="Scissors" && user2==="Paper"){
//         return `Scissors cut paper. Winner is user1`
//     }
//     else if (user1==="Paper" && user2==="Rock"){
//         return `Paper covers rock. Winner is user1`
//     }

//     else if (user1==="Scissors" && user2==="Rock"){
//         return `Rock destroys scissors. Winner is user2`
//     }
//     else if (user1==="Paper" && user2==="Scissors"){
//         return `Scissors cut paper. Winner is user2`
//     }
//     else if (user1==="Rock" && user2==="Paper"){
//         return `Paper covers rock. Winner is user2`
//     }
//     else{
//         return `If there’s a tie, then the game ends in a draw.`
//     }
// }
// console.log(gameRPS("Rock","Paper"))



// Var -global
// Let- it is used inside block
// const - it is not changed


var name="Bekzod"

let last_name="something"
const age=12
// if (true){
//     let last_name="test12"
//     const age=12;
//     console.log(last_name,age);
// }

// console.log(last_name,age);


// function testSCope(){
//     //local
//     var name;
//     name="aaaaaaaaaaaaaaaaaaaaaa";
//     function testSCope2(){
//         //local
//         var name;
//         name="AAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHH"
//     }
//     testSCope2();


//     console.log(name);
// }

// testSCope();
// console.log(name);