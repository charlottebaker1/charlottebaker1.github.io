// Charlotte Baker CSCE 242
const menu = document.getElementById("menu")
const menuBtn = document.getElementById("menuBtn")
menuBtn.onclick = (event) => {
  if (menu.classList.contains("open")) {
    menu.classList.remove("open")
    menuBtn.querySelector(".arrow").innerHTML = "▾"
  }
  else {
    menu.classList.add("open")
    menuBtn.querySelector(".arrow").innerHTML = "▴"
  }
}

const planting = document.getElementById("planting")
const clock = document.getElementById("clock")

document.getElementById("goPlant").onclick = () => {
  planting.classList.remove("hidden")
  clock.classList.add("hidden")
}

document.getElementById("goClock").onclick = () => {
  clock.classList.remove("hidden")
  planting.classList.add("hidden")
}

const days = document.getElementById("days")
const pImgWrap = document.getElementById("pImg")
const plantImg = document.getElementById("plantImg")
const p1 = document.getElementById("pMsg1")
const p2 = document.getElementById("pMsg2")

function showPlant(d) {
  if (!d) {
    pImgWrap.classList.add("hidden")
    p1.classList.add("hidden")
    p2.classList.add("hidden")
    return
  }

  if (d >= 1 && d <= 2) {
    plantImg.src = "images/plant_happy.png"
    plantImg.alt = "happy plant"
    p1.innerHTML = "It's been " + d + " days since watering your plant"
    p2.innerHTML = "Your plant is healthy and happy"
  }
  else if (d >= 3 && d <= 5) {
    plantImg.src = "images/plant_needs_water.png"
    plantImg.alt = "needs water"
    p1.innerHTML = "It's been " + d + " days since watering your plant"
    p2.innerHTML = "Your plant needs watering"
  }
  else if (d >= 6 && d <= 9) {
    plantImg.src = "images/plant_wilting.png"
    plantImg.alt = "wilting plant"
    p1.innerHTML = "It's been " + d + " days since watering your plant"
    p2.innerHTML = "Leaves are dropping, the color is changing, water soon"
  }
  else {
    plantImg.src = "images/plant_dead.png"
    plantImg.alt = "dead plant"
    p1.innerHTML = "It's been " + d + " days since watering your plant"
    p2.innerHTML = "Sorry, your plant is no longer with us"
  }

  pImgWrap.classList.remove("hidden")
  p1.classList.remove("hidden")
  p2.classList.remove("hidden")
}

days.oninput = (event) => {
  const value = parseInt(event.currentTarget.value, 10)
  showPlant(value)
}

function toTimeString(date) {
  const h = date.getHours()
  const m = date.getMinutes()
  const am = h < 12
  const hr = ((h + 11) % 12) + 1
  const mm = m < 10 ? "0" + m : "" + m
  const ap = am ? "am" : "pm"
  return hr + ":" + mm + " " + ap
}

function tick() {
  const now = new Date()
  document.getElementById("timeNow").innerHTML = toTimeString(now)
}

tick()
setInterval(() => {
  tick()
}, 1000)
