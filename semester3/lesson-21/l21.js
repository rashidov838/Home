// let anchor=document.querySelector("a");
// anchor.parentElement.style.fontSize="20px";

// anchor.children[0].style.display="block"

// How to create and add element inside in html
// let paragraph=document.createElement("p")
// paragraph.id="info"
// paragraph.innerHTML="The text inside the par"
// document.body.append(paragraph)

// We can remove elemtn <p> inside div block
// let paragraph_2=document.querySelector("div>p")
// document.querySelector("div").removeChild(paragraph_2)


// we can remove element last element which we added before
// let paragraph_2=document.querySelector("body>p");
// document.body.removeChild(paragraph_2)
// var count = 0;
// var countEl = document.getElementById("count");
// function plus(){
//     count++;
//     countEl.value = count;
// }
// function minus(){
//     count--;
//     countEl.value = count;
// }   


let text=document.querySelector("p")
function bgColor(){
    let red = Math.random() * 255;
    let blue = Math.random() * 255;
    let green = Math.random() * 255;
    document.body.style.backgroundColor=`rgb(${red},${green},${blue})`
    let fs=Math.random() *100;
    document.body.style.fontSize=`${fs}px`
    let ffamily=["italic","Impact", "Haettenschweiler", "Franklin Gothic Bold", "Charcoal"," Helvetica Inserat", "Bitstream Vera Sans Bold", "Arial Black","Arial Black", "Arial Bold", "Gadget", "sans-serif","Geneva", "Tahoma", "Verdana"]
    document.body.style.fontFamily=ffmNUm(ffamily)
}

text.addEventListener("click",bgColor);
text.addEventListener("wheel", )

// let numbers=[1,2,3,4,5];
function ffmNUm(fami){
    return fami[Math.floor(Math.random() * number.length)]
}