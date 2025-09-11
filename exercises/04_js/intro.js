/*
const sayHello = () => {
    console.log("Hello World");
}

document.getElementById("btn-click-me").onclick = sayHello;
*/

document.getElementById("btn-click-me").onclick = () => {
    document.getElementById("p-welcome").innerHTML = "Hello World";
    //document.getElementById("btn-click-me").classList.add("clicked");
    event.currentTarget.classList.add("clicked"); //current target is the button that was clicked

};

document.getElementById("happy-button").onclick = () => {
    document.getElementById("p-happy").innerHTML = "Have a great day!";
    event.currentTarget.classList.add("happy");
};

document.getElementById("sad-button").onclick = () => {
    document.getElementById("p-sad").innerHTML = "Cheer up!";
    event.currentTarget.classList.add("sad");
};

document.getElementById("clear-button").onclick = () => {
    document.getElementById("p-happy").innerHTML = "";
    document.getElementById("p-sad").innerHTML = "";
    document.getElementById("happy-button").classList.remove("happy");
    document.getElementById("sad-button").classList.remove("sad");
    event.currentTarget.classList.add("cleared");
}