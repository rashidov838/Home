// let name ="Bekzod"
// this.a=12;

// const goat={
//     diettype:"herbivore",
//     makeSound(){
//         console.log(this.diettype);
//     },
//     diet:()=>{
//         console.log(this.a);
//         console.log(this.diettype)
//     }

// }

// goat.diet();
// goat.makeSound();



// const bankAccount={
//     _amount:1000,
// }
// bankAccount._amount=10000000000000;
// console.log(bankAccount)


const robot = {
    _energylevel: 100,
    racharge() {
        this._energylevel += 30;
        console.log(`Recharges Energy is currently at ${this._energylevel}.`);

    },
};
robot._energylevel = "high";
robot.racharge();
console.log(robot._energylevel);

const person = {
    _firstname: "Bekzod",
    _lastname: "Rashidov",
    _age: 37,
    get fullName() {
        if (this._firstname && this._lastname) {
            return `${this._firstname} ${this._lastname}`
        }

        else {
            return "Missing a first name or lastname"
        }
    },
    set age(newAge) {
        if (typeof newAge === "number") {
            this._age = newAge;
        }
        else {
            console.log("You must assign a number to age")
        }
    },
    get age() {
        if (this._age) {
            return this._age
        }
        else {
            return "Age is empty or is 0"
        }
    }
}


// person.age=40;
// console.log(person.fullName);
// console.log(person.age)
const menu = {
    _meal: "beef",
    _price: 100,
    get mealAndPrice() {
        if (this._meal && this._price) {
            return `Today, we have ${this._meal} and price: ${this._price} in breakfast`
        }
        else {
            return `it is not`
        }
    },
    set newMeal(newfoodformeal) {
        if (typeof newfoodformeal === "string" && newfoodformeal) {
          this._meal = newfoodformeal;
        }
        else {
            return `it is not lunch`
        }
    },
    set price(newprice) {
        if (typeof newprice === "number" && newprice) {
          this._price = newprice;
        }
        else {
            return `it is not lunch`
        }
    }
}
menu.newMeal="chicken"
menu.price=400
console.log(menu.mealAndPrice)

function count(array){
    const newaaray={}
    for(let i=0; i<array.length; i++){
        if(Object.keys(newaaray).includes(array[i])){
            newaaray[array[i]]+=1
        }
        else{
            newaaray[array[i]]=1
        }
    }
    return newaaray
}

console.log(count(['james', 'james', 'john']) )