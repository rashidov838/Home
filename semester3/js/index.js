// console.log("indexing")

// const emp=[];
// emp[0]="one"
// emp[1]="two"


// emp[2.4]="Oranges";
// console.log(emp);

// console.log(Object.hasOwn(emp,2.4))


// Create array
// const myarray=new Array("Hello",3.123);
// console.log(myarray)


// const cats = [];
// cats[30] = ["Dusty"];
// console.log(cats);


// const colors=["red","yellow","blue"];
// for(let i=0; i<colors.length; i++){
//     console.log(colors[i])
// }

// const colors=["red","yellow","blue"];
// colors.forEach((color)=>console.log(color))


// Foreach we can use inly for array

// const sparseArray=["first","second",,"fourth"]
// sparseArray.forEach((element)=>{
//     console.log(element);
// })

// if (sparseArray[2]===undefined){
//     console.log("sparseArray[2] is undefined")
// }


// Pop delete last element in array: 
// const last=sparseArray.pop()
// console.log(sparseArray)

// Push add elemenet:
// const additioninfo=sparseArray.push("Monila")
// console.log(sparseArray)

// Concat , it is connected two arrays:
// let second__lst=['a','v','gm']
// sparseArray2=sparseArray.concat(second__lst)
// console.log(sparseArray2)

// Join:
// const lst=sparseArray.join("-")
// console.log(lst)

// Unshift add element left side:
// const sparseArray=["first","second",,"fourth"]
// sparseArray.unshift("3","4")
// console.log(sparseArray)


// Slice:
// sparse=sparseArray.slice(1,4)
// console.log(sparse)

//  At
// const sparseArray=["first","second","gm","fourth"]
// console.log(sparseArray.at(-2))

// Reverse
// let reverseleement=sparseArray.reverse();
// console.log(sparseArray)

// Flat 
// let myaray=[1,2,3,[5,6]];
// mynewarray=myaray.flat()
// console.log(mynewarray)
//result : [ 1, 2, 3, 5, 6 ]


// Sort 
// const myArray = ["Wind", "Rain", "Fire"];
// console.log(myArray.sort())


//IndexOf it help to know which index is stayed
// const a=["a", "b", "a", "b", "a"];
// console.log(a.indexOf("b"))
// console.log(a.indexOf("b",2))

// console.log(a.indexOf("z"))


// Lastindexof
// const a = ["a", "b", "c", "d", "a", "b"];
// console.log(a.lastIndexOf("b"))
// console.log(a.lastIndexOf("b",4))

// Map
// const a1=["a",'b',"c"]
// const a2 =a1.map((item)=>item.toUpperCase());
// console.log(a1)
// console.log(a2)


//FlatMap
// const a1=["a","b","c"]
// const a2=a1.flatMap((item)=>[item.toUpperCase(),item.toLowerCase()]);
// console.log(a2)


//Filter
// const a1=["a", 10, "b", 20, "c", 30];
// const a2=a1.filter((item) => typeof item==="number");
// console.log(a2)

//Find
// const i= a1.find((item) =>typeof item ==="number")
// console.log(i)

// FindLast
// const i = a1.findLast((item)=> typeof item==="number");
// console.log(i)

// FindIndex wiil return the index of first  item.For example  10 is index 1
// const a1=["a", 10, "b", 20, "c", 30];
// const i=a1.findIndex((item)=>typeof item === "number");
// console.log(i)


//findlastidex will return the index of last  item
// const a1=["a", 10, "b", 20, "c", 30];
// const i=a1.findLastIndex((item)=>typeof item === "number");
// console.log(i)

// delete
// const a1=["a", 10, "b", 20, "c", 30];
// delete a1[3]
// console.log(a1)

// ...
// const a1=[1,2,3, , , 5]
// const another=[...a1]
// console.log(another)