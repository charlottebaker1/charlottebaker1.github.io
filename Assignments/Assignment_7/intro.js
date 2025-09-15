//Charlotte Baker CSCE 242
document.getElementById("sec-sunny").onclick = () => {
    document.getElementById("sunny-lyrics").innerHTML = `
        <p>Here comes the sun</p>
        <p class="indent">Sun</p>
        <p class="indent">Sun</p>
        <p class="indent">Sun</p>
        <p>Here it comes</p>
    `;
};

document.getElementById("color-picker").oninput = (event) => {
    const picked = event.currentTarget.value;
    const pColor = document.getElementById("p-color");
    pColor.style.color = picked;
    pColor.innerHTML = picked;
};

document.getElementById("img-weather").onclick = (event) => {
    document.getElementById("img-weather").setAttribute("src", "sunny.png");
};

document.getElementById("txt-emotion").onkeyup = (event) => {
    const userInput = event.currentTarget.value;
    document.getElementById("p-emotion").innerHTML = `You are feeling ${userInput}.`;
    document.getElementById("img-emotion").classList.remove("hidden");
};
