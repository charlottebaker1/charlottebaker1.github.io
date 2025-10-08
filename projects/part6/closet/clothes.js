// Charlotte Baker CSCE 242
//Closets script for JSON Parsing
document.addEventListener("DOMContentLoaded", async () => {
  const grid = document.getElementById("closet-grid");
  if (!grid) return;

  const JSON_URL = "https://charlottebaker1.github.io/projects/part6/json/clothes.json";

  grid.innerHTML = '<p class="muted">Loading items…</p>';

  try {
    const res = await fetch(JSON_URL, { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const items = await res.json();

    const frag = document.createDocumentFragment();

    items.forEach(item => {
      const card = document.createElement("div");
      card.className = "item";

      const img = document.createElement("img");
      img.src = item.img;     
      img.alt = item.title || "";

      const h3 = document.createElement("h3");
      h3.textContent = item.title || "Item";

      const meta = document.createElement("p");
      meta.className = "muted";
      meta.textContent = `${item.type || ""} • ${item.color || ""} • ${item.season || ""}`;

      const pBtn = document.createElement("p");
      const a = document.createElement("a");
      a.href = "../upload-item/index.html";
      a.className = "btn";
      a.textContent = "View/Edit Item";
      pBtn.appendChild(a);

      card.appendChild(img);
      card.appendChild(h3);
      card.appendChild(meta);
      card.appendChild(pBtn);
      frag.appendChild(card);
    });

    grid.innerHTML = "";
    grid.appendChild(frag);
  } catch (err) {
    console.error(err);
    grid.innerHTML = '<p class="muted">Could not load items. Check your JSON URL and try again.</p>';
  }
});
