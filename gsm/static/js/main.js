var num = 0;
var button = document.getElementById("answer");


/*coin*/
function coin() {
  num += 11;
  var numbers = document.getElementById("coinAm");
  //upgrade level for printing
  var upgradeLevel = document.getElementById("upgradeLevel");
  numbers.innerHTML = num;
}

function coin2() {
  num += 21;
  var numbers = document.getElementById("coinAm");
  //upgrade level for printing
  var upgradeLevel = document.getElementById("upgradeLevel");
  numbers.innerHTML = num;
}

function coin3() {
  num += 31;
  var numbers = document.getElementById("coinAm");
  //upgrade level for printing
  var upgradeLevel = document.getElementById("upgradeLevel");
  numbers.innerHTML = num;
}

function coin4() {
  num += 41;
  var numbers = document.getElementById("coinAm");
  //upgrade level for printing
  var upgradeLevel = document.getElementById("upgradeLevel");
  numbers.innerHTML = num;
}
function coin5() {
  num += 51;
  var numbers = document.getElementById("coinAm");
  //upgrade level for printing
  var upgradeLevel = document.getElementById("upgradeLevel");
  numbers.innerHTML = num;
}
function coin6() {
  num += 6;
  var numbers = document.getElementById("coinAm");
  //upgrade level for printing
  var upgradeLevel = document.getElementById("upgradeLevel");
  numbers.innerHTML = num;
}
function coin7() {
  num += 7;
  var numbers = document.getElementById("coinAm");
  //upgrade level for printing
  var upgradeLevel = document.getElementById("upgradeLevel");
  numbers.innerHTML = num;
}

/*result*/
function result1() {
  if(num <=20) {
    location.href="result.html";
  }
}
function result2() {
  if(num >= 21 && num <=30) {
    location.href="result2.html";
  }
}
function result3() {
  if(num >= 31 && num <=40) {
    location.href="result3.html";
  }
}
function result4() {
  if(num >= 41 && num <=50) {
    location.href="result4.html";
  }
}
function result5() {
  if(num >= 51 && num <=60) {
    location.href="result5.html";
  }
}