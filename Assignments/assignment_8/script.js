const manButton = document.getElementById("manButton");
const man = document.getElementById("man");
const thermoInput = document.getElementById("thermoInput");
const thermometer = document.getElementById("thermometer");
const goalText = document.getElementById("goalText");

let running = false;
let manPosition = 0;
let thermoValue = 0;

manButton.addEventListener("click", toggleRunning);

function toggleRunning() {
    running = !running;
    manButton.disabled = true; 
    moveMan();
}

function moveMan() {
    if (running) {
        manPosition++;
        man.style.marginLeft = manPosition + "px";
        man.style.backgroundImage = manPosition % 2 === 0 ? "url('man_walking.png')" : "url('man_running.png')";
        if (manPosition < window.innerWidth - man.clientWidth) {
            requestAnimationFrame(moveMan); 
        } else {
            manButton.disabled = false; 
        }
    }
}

document.getElementById("updateThermometer").addEventListener("click", updateThermometer);

function updateThermometer() {
    const value = parseInt(thermoInput.value);
    if (!isNaN(value) && value >= 0) {
        thermoValue = value;
        updateThermoDisplay();
    }
}

function updateThermoDisplay() {
    const goal = 10000;
    const percentage = (thermoValue / goal) * 100;
    thermometer.style.backgroundImage = `linear-gradient(to top, #FF0000 ${percentage}%, transparent ${percentage}%)`;
}
