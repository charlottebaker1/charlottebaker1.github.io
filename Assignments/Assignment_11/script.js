// Charlotte Baker CSCE 242

const beforeBears = [];
beforeBears["Grizz"]  = "https://placebear.com/400/300";
beforeBears["Panda"]  = "https://placebear.com/401/300";
beforeBears["Kodiak"] = "https://placebear.com/402/300";
beforeBears["Winnie"] = "https://placebear.com/403/300";

const afterBears = [];
afterBears["Grizz"]  = "https://placebear.com/500/360";
afterBears["Panda"]  = "https://placebear.com/501/360";
afterBears["Kodiak"] = "https://placebear.com/502/360";
afterBears["Winnie"] = "https://placebear.com/503/360";

const gallery = document.getElementById("gallery");
const popup = document.getElementById("popup");
const afterImg = document.getElementById("after-img");
const afterTitle = document.getElementById("after-title");
const closeBtn = document.getElementById("close");

window.onload = () => {
  gallery.innerHTML = "";

  for (let name in beforeBears) {
    const card = document.createElement("article");
    card.className = "card";
    card.title = `${name} (before adoption)`;

    const img = document.createElement("img");
    img.src = beforeBears[name];
    img.alt = `Before adoption photo of ${name}`;

    const cap = document.createElement("div");
    cap.className = "caption";
    cap.innerHTML = `Please adopt ${name}`;

    card.onclick = () => {
      afterTitle.innerHTML = `${name} after adoption`;
      afterImg.src = afterBears[name];
      afterImg.alt = `After adoption photo of ${name}`;
      popup.classList.remove("hidden");
    };

    card.append(img);
    card.append(cap);
    gallery.append(card);
  }
};

closeBtn.onclick = () => {
  popup.classList.add("hidden");
  afterImg.src = "";
};

popup.addEventListener("click", (evt) => {
  if (evt.target === popup) {
    popup.classList.add("hidden");
    afterImg.src = "";
  }
});

document.addEventListener("keydown", (evt) => {
  if (evt.key === "Escape" && !popup.classList.contains("hidden")) {
    popup.classList.add("hidden");
    afterImg.src = "";
  }
});
