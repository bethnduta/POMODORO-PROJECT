// tapping into DOM elements
let workTime = document.querySelector("#w_minutes").textContent;
let breakTime = document.querySelector("#b_minutes").textContent;
let sessionCount = document.querySelector("#counter").textContent;

// variables for the timmer
my_session = 5;
resetBreak = breakTime;
resetWork = workTime;

// logic for the timmer
function startBreak() {
  let breakInterval = setInterval(function () {
    if (breakTime > 0) breakTime--;
    else {
      breakTime = 0;
      clearInterval(breakInterval);
      startWork();
    }
    document.querySelector("#b_minutes").textContent = breakTime;
  }, 1000);

  function startWork() {
    let workCountdown = setInterval(function () {
      if (workTime > 0) workTime--;
      else {
        workTime = 0;
        clearInterval(workCountdown);
        sessionCount++;
        if (sessionCount != my_session) {
          breakTime = resetBreak;
          workTime = resetWork;
          startBreak();
        }
      }
      document.querySelector("#counter").textContent = sessionCount;
      document.querySelector("#w_minutes").textContent = workTime;
    }, 1000);
  }
}

if (breakTime != 0 && workTime != 0) {
  startBreak();
}
