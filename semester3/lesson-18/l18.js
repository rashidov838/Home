// for (let counter=0; counter<4;counter++){
//     console.log(counter);
// }

// let number =[];
// for (let counter=0;counter<10;counter++){
//     number.push(counter);
// }
// console.log(number)


// let counterTwo=4;
// while (counter<4){
//     console.log(counterTwo);
//     counter++;

// }

// let countString=""
// let i=0;
// do{
//     i++;
//     countString+i;
// }
// while(i<5);



var info=[]
for (let count=0;count<7;count++){
    let day=prompt("Bведите день: ");
    let hours=parseInt(prompt("Напишите число: "));
    console.table(day,hours); 
    info.push(hours);
}
const averagefindday=(info)=>{
    let amount=0
    for (const i of info){
        amount+=i;
        console.log(amount);
    }
    return Math.floor(amount/info.length);
}
console.log(averagefindday(info))

// const spaceship = {
//     telescope: {
//       yearBuilt: 2018,
//       model: "91031-XLT",
//       focalLength: 2032,
//     },
//     crew: {
//       captain: {
//         name: "Sandra",
//         degree: "Computer Engineering",
//         encourageTeam() {
//           console.log("We got this!");
//         },
//       },
//     },
//     engine: {
//       model: "Nimbus2000",
//     },
//     nanoelectronics: {
//       computer: {
//         terabytes: 100,
//         monitors: "HD",
//       },
//       "back-up": {
//         battery: "Lithium",
//         terabytes: 50,
//       },
//     },
//   };


// console.log(spaceship.crew.captain.encourageTeam())