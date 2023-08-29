var count = 0;
var countElement = document.getElementById("count");
function plus() {
  count++;
  countElement.value = count;
}
function minus() {
  count--;
  countElement.value = count;
}
var questionheader = document.getElementById("questionheader");
var makeguess = document.getElementById("makeguess");
var images = document.getElementById("imgq");
var computernum = document.getElementById("computernum");
var winner = document.getElementById("winner");
makeguess.addEventListener("click", updateButton);

function updateButton() {
  questionheader.innerHTML = (Math.random() * 10).toFixed(3);
  computernum.textContent = Math.floor(Math.random() * 10);
  images.style.display = "none";
  computernum.style.visibility = "visible";
  let result;
  if (
    (questionheader.innerHTML >= computernum.innerText) &&
    questionheader.innerHTML >= countElement.value &&
    computernum.innerText >= countElement.value
  ) {
    result = `${computernum.innerText} won round computer`;
    winner.style.visibility = "visible";
    winner.style.backgroundColor = "black";
    makeguess.disabled = true;
    makeguess.style.backgroundColor = "grey";
  } else if (
    questionheader.innerHTML >= computernum.innerText &&
    questionheader.innerHTML >= countElement.value &&
    computernum.innerText <= countElement.value
  ) {
    result = `${countElement.value} won round me`;
    makeguess.style.backgroundColor = "black";
    makeguess.innerHTML = "Winner";
    makeguess.disabled = true;
  } else if (
    (questionheader.innerHTML <= countElement.value) &&
    ( questionheader.innerHTML <= computernum.innerText) &&
    ( countElement.value <= computernum.innerText)
  ) {
    result = `${countElement.value} won round meee`;
    makeguess.style.backgroundColor = "black";
    makeguess.innerHTML = "Winner";
    makeguess.disabled = true;
  } else if (
    ( questionheader.innerHTML <= computernum.innerText) &&
    (questionheader.innerHTML <= countElement.value) &&
    ( countElement.value >= computernum.innerText)
  ) {
    result = `${computernum.innerText} won round computerrr`;
    winner.style.visibility = "visible";
    winner.style.backgroundColor = "black";
    makeguess.disabled = true;
    makeguess.style.backgroundColor = "grey";
  }
  else if (
    (questionheader.innerHTML - countElement.value) <
    ( computernum.innerText - questionheader.innerHTML )
  ) {
    result = `${countElement.value} won round meee`;
    makeguess.style.backgroundColor = "black";
    makeguess.innerHTML = "Winner";
    makeguess.disabled = true;
  } 
    else if (
    (questionheader.innerHTML - countElement.value) >
    ( computernum.innerText - questionheader.innerHTML )
  ) {
    result = `${computernum.innerText} won round computerrr`;
    winner.style.visibility = "visible";
    winner.style.backgroundColor = "black";
    makeguess.disabled = true;
    makeguess.style.backgroundColor = "grey";
  }
  else{
    return "Nothing"
  }
    // document.getElementById("result").innerHTML = `
    //     <p>questionheader => ${questionheader.innerHTML}</p>
        
    //     <p>computernum => ${computernum.innerText}</p>
        
    //     <p>Me => ${countElement.value}</p>
        
    //     <p>winer => ${result}</p>
    //     `;
}

var next_round = document.getElementById("next_round");
var score_compElement = document.getElementById("scorecount_comp");
var score_meElement = document.getElementById("scorecount_me");
var roundElement = document.getElementById("roundNumber");
var scorecount_for_comp = 0;
var scorecount_for_make_guess = 0;

var roundNumber = 1;
next_round.addEventListener("click", next_round_Button);
function next_round_Button() {
  if (makeguess.innerHTML === "Winner") {
    scorecount_for_make_guess++;
    score_meElement.innerText = scorecount_for_make_guess;
    makeguess.disabled = false;
    makeguess.style.backgroundColor = "blue";
    roundNumber++;
    roundElement.innerHTML = roundNumber;
    makeguess.innerHTML="Make Guess"
  } else if (winner.innerText === "Winner") {
    scorecount_for_comp++;
    score_compElement.innerText = scorecount_for_comp;
    makeguess.disabled = false;
    makeguess.style.backgroundColor = "blue";
    winner.style.visibility = "hidden";
    roundNumber++;
    roundElement.innerHTML = roundNumber;
  }
  winner.style.visibility = "hidden";
}
