// Charlotte Baker CSCE 242
//Closets script for JSON Parsing

document.addEventListener("DOMContentLoaded", async () => {
  const grid = document.getElementById("closet-grid");
  const typeSel = document.getElementById("filter-type");
  const colorSel = document.getElementById("filter-color");
  const seasonSel = document.getElementById("filter-season");
  if (!grid) return;

  const JSON_URL = "https://charlottebaker1.github.io/projects/part6/json/clothes.json";
  grid.innerHTML = '<p class="muted">Loading items…</p>';

  let items = [];
  try {
    const res = await fetch(JSON_URL, { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    items = await res.json();
  } catch (e) {
    console.error(e);
    grid.innerHTML = '<p class="muted">Could not load items. Check your JSON URL.</p>';
    return;
  }

  const uniq = (arr) => Array.from(new Set(arr.filter(Boolean))).sort((a,b)=>`${a}`.localeCompare(`${b}`));
  const fill = (el, vals) => el && vals.forEach(v => {
    const opt = document.createElement("option");
    opt.value = v; opt.textContent = v; el.appendChild(opt);
  });
  fill(typeSel,   uniq(items.map(i => i.type)));
  fill(colorSel,  uniq(items.map(i => i.color)));
  fill(seasonSel, uniq(items.map(i => i.season)));


  const eq = (a,b) => String(a||"").toLowerCase() === String(b||"").toLowerCase();
  const passes = (it) =>
    (!typeSel  || typeSel.value  === "all" || eq(it.type,   typeSel.value))  &&
    (!colorSel || colorSel.value === "all" || eq(it.color,  colorSel.value)) &&
    (!seasonSel|| seasonSel.value=== "all" || eq(it.season, seasonSel.value));

  const makeCard = (item) => {
    const card = document.createElement("div");
    card.className = "item";

    const img = document.createElement("img");
    img.src = item.img;          
    img.alt = item.title || "";

    const h3 = document.createElement("h3");
    h3.textContent = item.title || "Item";

    const pBtn = document.createElement("p");
    const a = document.createElement("a");
    a.href = "../upload-item/index.html";
    a.className = "btn";
    a.textContent = "View/Edit Item";
    pBtn.appendChild(a);

    card.appendChild(img);
    card.appendChild(h3);
    card.appendChild(pBtn);
    return card;
  };

  const render = () => {
    const list = items.filter(passes);
    if (!list.length) {
      grid.innerHTML = '<p class="muted">No items match those filters.</p>';
      return;
    }
    const frag = document.createDocumentFragment();
    list.forEach(it => frag.appendChild(makeCard(it)));
    grid.innerHTML = "";
    grid.appendChild(frag);
  };

  [typeSel, colorSel, seasonSel].forEach(s => s?.addEventListener("change", render));
  render();
});
