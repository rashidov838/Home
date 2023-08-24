Task-1
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

Task-2
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


Task-3
function killer(suspects,dead){
    const info= new Array()
        for(i of dead){
            console.log(i)
}
        for (let [key, value] of Object.entries(suspects)){   
            if(value.includes(i)){
                    info.push(key)
                }
        }
        return info[0]
}


console.log(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']), 'James')
console.log(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']))


Task-4
function findOdd(array) {
    const newaaray={}
    array.forEach(element => {
        if(newaaray[element]){
            newaaray[element]+=1;
        }
        else{
            newaaray[element]=1;
        }
    });
    console.log(newaaray)
    const info=[]
    for(let [key,val] of Object.entries(newaaray)){
        if( val%2 !== 0){
            return parseInt(key)
        }
    }
}

console.log(findOdd([7,7,1,1,1])) 


Task-5
function fibonacci(n){
    if(n<1) return 1;
    else if(n===1) return 0;
    else return fibonacci(n-1)+fibonacci(n-2)
}

console.log(fibonacci(4))