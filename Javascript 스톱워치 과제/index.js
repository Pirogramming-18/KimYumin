let timerld;
let time = 0;
let hour, min, sec, msec;

const recordItem = document.querySelector('.list-items')
const check = document.createElement("div");






const screen = document.getElementById('screen-text');


function printTime(){
    time++;
    screen.innerText = getTimeFormatString();

}

function startClock(){
    printTime();
    stopClock();
    timerld = setTimeout(startClock, 1000);
}

function stopClock(){
    if(timerld != null){
        clearTimeout(timerld);
    }
    recordClock();
}


function recordClock(){
    const list_item = document.createElement("li");
    
    list_item.innerHTML = `<input class="check" type="checkbox" /><li class="list-item">${screen.innerText}
    </li>
    `;
  recordItem.appendChild(list_item);
  
}

function deleteRecord(){
    const check = document.querySelector(".check")
    for(let i = 0; i < check.length; i++){
        if(check[i].checked ){
            check[i].remove();
        }
    }
   
}
    



function resetClock(){
    stopClock();
    screen.innerText = "00:00";
    time = 0;
}

function getTimeFormatString(){
  
    hour = parseInt(String(time / (60*60)));
    min = parseInt(String((time - (hour * 60 * 60 ))/ 60));
    sec = time % 60;
   
    
    return String(min).padStart(2,'0') + ":" + String(sec).padStart(2, '0');
}

