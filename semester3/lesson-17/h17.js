// Join
const elements=["BAnana","Car","Limon"]


console.log(elements.join());

console.log(elements.join(''))

console.log(elements.join('-'))

var el1=elements.join();
console.log(el1);

var el2=elements.join(", ");
console.log(el2);

var el3=elements.join(" + ");
console.log(el3)


// Slice
const info=['pensil','bison','apple','banana','pear','eggplant','pumkin']
console.log(info.slice(2))

console.log(info.slice(2,4))


console.log(info.slice(-1))

var inf={
    color:"red",
    wheeels:4,
    engine:{cylinders:3,size:2.2},
};

var mycar=[inf,2, "в хорошем состоянии", "приобретена в 1997"];

console.log(mycar)
console.log("mycar = "+  mycar.toSource());

console.log("Color:",mycar[0].color);
inf.color = "yellow";
console.log("Changed info: ", inf.color)


// splice
var myinfo=["angel", "clown", "mandarin", "sturgeon"]
var removed=myinfo.splice(2,2,'drum');
//  первый элемент 2 это индекс в списке а второй элемент 2 количество удаленных  а drum будет добавлен 
console.log("Удаленные: ",removed)
console.log(myinfo)

var itisforneg=myinfo.splice(-2,3);
console.log(itisforneg)
console.log(myinfo)


//shift - удаляет первый элемент
var info=["ангел", "клоун", "мандарин", "хирург"];

var shifted=info.shift();

console.log("Удаленный элемент: "+shifted)
console.log(info)

Unshift - добавляет элеиент в начала списка
info.unshift(-2,-1)
console.log(info)



// Concat - объединяет
const info1=['car1','car2','car3']

const info2=['car4','car5','car6']

const info3=info1.concat(info2);

console.log(info3);


// Task - 2
function addToArray(arr = []) {
    arr.push(23);
    console.log(arr)
  }
  
addToArray();
addToArray();
addToArray();
addToArray();


// Task-3
function isIsogram(str) {
    if (str.isEmpty) {
      return true;
    } else {
      str = str.toLowerCase();
    }
    var array = str.split('');
    var sortedArr = array.slice().sort();
  
    for (var i = 0; i < array.length; i++) {
      if (sortedArr[i + 1] == sortedArr[i]) {
        return false;
      }
    }
    return true;
  }

console.log(isIsogram('moOse')); 
console.log(isIsogram('to be or not to be')); 
console.log(isIsogram('wasdfgerty');

// Task-4
var isAnagram = function(test, original) {
    let len1=test.length;
    let len2=original.length;
    if(len1 !== len2){
        return  false
    }
    let str1=test.split('').sort().join();
    let str2=original.split('').sort().join();
    if (str1 === str2){
        return true;
    }
    else{
        return false;
    };
};




console.log(isAnagram("indian","ndiani"))