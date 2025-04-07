// Sélection des éléments du DOM
const form = document.getElementById("product-form");
const productName = document.getElementById("product-name");
const productPrice = document.getElementById("product-price");
const productImage = document.getElementById("product-image");//input
const previewImage = document.getElementById("preview-image");// tag img
const productList = document.getElementById("product-list");//container des list of products
const productIdField = document.getElementById("product-id"); // id of hidden field

// Récupération des produits depuis LocalStorage
let products = JSON.parse(localStorage.getItem("products")) || [];

// Fonction pour afficher les produits
function displayProducts() {
    productList.innerHTML = "";
    products.forEach((product, index) => {
        const productCard = document.createElement("div");
        productCard.classList.add("product-card");
        productCard.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>${product.price} €</p>
            <button onclick="editProduct(${index})">Modifier</button>
            <button onclick="deleteProduct(${index})">Supprimer</button>
        `;
        productList.appendChild(productCard);
    });
}

// Gestion de l'ajout/modification d'un produit
form.addEventListener("submit", (e) => {
    e.preventDefault();
    
    const id = productIdField.value;
    const name = productName.value;
    const price = productPrice.value;
    const image = previewImage.src;


    if (!name || !price || image === "") {
        alert("Veuillez remplir tous les champs !");
        return;
    }

    const newProduct = { name, price, image }; 

    if (id) {
        products[id] = newProduct; // Modification
    } else {
        products.push(newProduct); // Ajout
    }

    localStorage.setItem("products", JSON.stringify(products));
    form.reset();
    previewImage.style.display = "none";//masquer l image
    productIdField.value = "";//vider hidden field
    displayProducts();
});

// Suppression d'un produit
function deleteProduct(index) {
    products.splice(index, 1);
    localStorage.setItem("products", JSON.stringify(products));
    displayProducts();
}

// Modification d'un produit
function editProduct(index) {
    const product = products[index];
    productName.value = product.name;
    productPrice.value = product.price;
    previewImage.src = product.image;
    previewImage.style.display = "block";
    productIdField.value = index;
}

// Gestion de l'affichage de l'image en temps réel
productImage.addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (event) {
            previewImage.src = event.target.result;
            previewImage.style.display = "block";
        };
        reader.readAsDataURL(file);
    }
});

// Affichage des produits au chargement de la page
displayProducts();
