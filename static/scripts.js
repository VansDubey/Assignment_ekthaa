// Example countdown for Deals of the Day
let countdown = 24 * 60 * 60; // 24 hours in seconds

function updateTimer() {
    let hours = Math.floor(countdown / 3600);
    let minutes = Math.floor((countdown % 3600) / 60);
    let seconds = countdown % 60;

    document.querySelector('.deals-of-day h2').innerText = 
        `Deals of the Day | ${hours}:${minutes}:${seconds} Left`;

    countdown--;
    if (countdown < 0) countdown = 0;
}

setInterval(updateTimer, 1000);
