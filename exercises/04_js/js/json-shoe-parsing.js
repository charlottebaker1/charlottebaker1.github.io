// link like a script in html

const getShoes = async() => {
    const url = "https://portiaportia.github.io/json/shoes.json";
    try {
        const response = await fetch(url);
        return response.json();
    }
    catch (error) {
        console.log("sorry");
    }
        
};

const showShoes = async() => {
    const shoes = await getShoes();
    
    shoes.forEach((shoe)=>{
        const section = document.createElement("section");
        section.classList.add("shoe");

        const h3 = document.createElement("h3");
        h3.innerHTML = shoe.name;
        section.append(h3);

        const p = document.createElement("p");
        p.innerHTML = `<strong>Color:</strong> ${shoe.color}`;
        section.append(p);

        const p2 = document.createElement("p");
        p2.innerHTML = `<strong>Price:</strong> $${shoe.price}`;
        section.append(p2);

        const img = document.createElement("img");
        img.src = `images/json/${shoe.image}`;
        section.append(img);

        const ul = document.createElement("ul");
        section.append(ul);
        shoe.reviews.forEach((review)=>{
            const li = document.createElement("li");
            li.innerHTML = review;
            ul.append(li);
        });
    });
}
showShoes();