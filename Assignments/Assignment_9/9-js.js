/*Charlotte Baker CSCE 242*/

document.getElementById("btn-draw").onclick = () => {
  const cloudRow = document.getElementById("cloud-row");
  const treeRow  = document.getElementById("tree-row");
  const stage    = document.getElementById("stage");

  cloudRow.innerHTML = "";
  treeRow.innerHTML  = "";

  const hour = new Date().getHours(); 
  const isNight = (hour >= 18 || hour < 6);  

  document.body.classList.toggle("night", isNight);

  const oldSky = stage.querySelector(".sun, .moon");
  if (oldSky) oldSky.remove();
  const skyObj = document.createElement("div");
  skyObj.className = isNight ? "moon" : "sun";
  stage.append(skyObj);

  for (let i = 0; i < 6; i++) {
    const cloud = document.createElement("div");
    cloud.className = "cloud";
    cloudRow.append(cloud);
  }

  for (let i = 0; i < 6; i++) {
    const tree = document.createElement("div");
    tree.className = "tree";
    const leaves = document.createElement("div");
    leaves.className = "leaves";
    const trunk = document.createElement("div");
    trunk.className = "trunk";
    tree.append(leaves);
    tree.append(trunk);
    treeRow.append(tree);
  }
};
