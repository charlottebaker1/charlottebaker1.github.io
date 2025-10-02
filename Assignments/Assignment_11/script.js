// Charlotte Baker CSCE 242
class Painting {
  constructor(title, artist, imgFile, framed) {
    this.title = title;
    this.artist = artist;
    this.imgFile = imgFile;
    this.framed = framed === true; 
  }

  get item() {
    const section = document.createElement("section");
    section.classList.add("painting");

    const h3 = document.createElement("h3");
    h3.textContent = this.title;
    section.append(h3);

    const img = document.createElement("img");
    img.src = `images/${this.imgFile}`;
    img.alt = this.title;
    section.append(img);

    section.onclick = () => {
      showModal(this);
    };

    return section;
  }
}

const paintings = [];
paintings.push(new Painting("Mona Lisa", "Leonardo Da Vinci", "monalisa.jpg", true));
paintings.push(new Painting("Starry Night", "Vincent Van Gogh", "starrynight.jpg", false));
paintings.push(new Painting("Girl with a Pearl Earring", "Johannes Vermeer", "girlwithapearl.jpg", false));
paintings.push(new Painting("The Scream", "Edvard Munch", "thescream.jpg", true));
paintings.push(new Painting("Bridge over a Pond of Waterlilies", "Claude Monet", "waterlillies.jpg", false));

const list = document.getElementById("painting-list");
paintings.forEach(p => list.append(p.item));

const modal = document.getElementById("detailsModal");
const closeModal = document.getElementById("closeModal");
const closeBtn = document.getElementById("closeBtn");

function showModal(painting) {
  document.getElementById("modalTitle").textContent = painting.title;
  document.getElementById("modalArtist").textContent = "by " + painting.artist;

  const img = document.getElementById("modalImage");
  img.src = `images/${painting.imgFile}`;
  img.alt = painting.title;

  const frameWrap = document.getElementById("frameWrap");
  const frameNote = document.getElementById("frameNote");

  if (painting.framed) {
    frameWrap.classList.remove("frame-off");
    frameWrap.classList.add("frame-on");
    frameNote.textContent = "Framed";
  } else {
    frameWrap.classList.remove("frame-on");
    frameWrap.classList.add("frame-off");
    frameNote.textContent = "Not framed";
  }

  modal.style.display = "block";
}

closeModal.onclick = () => modal.style.display = "none";
closeBtn.onclick = () => modal.style.display = "none";
window.onclick = (e) => {
  if (e.target === modal) modal.style.display = "none";
};
