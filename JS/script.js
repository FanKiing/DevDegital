// Tableau de produits initial
let produits = [
    { id: 1, nom: "Ordinateur", prix: 1200 },
    { id: 2, nom: "Téléphone", prix: 800 },
    { id: 3, nom: "Tablette", prix: 500 }
];


const form = document.getElementById("productForm");
const productIdInput = document.getElementById("productId");
const productNameInput = document.getElementById("productName");
const productPriceInput = document.getElementById("productPrice");
const productTable = document.getElementById("productTable");


function afficherProduits() {
    productTable.innerHTML = ""; 

    produits.forEach((produit) => {
        let row = document.createElement("tr");

        row.innerHTML = `
            <td>${produit.id}</td>
            <td>${produit.nom}</td>
            <td>${produit.prix} €</td>
            <td>
                <button class="btn btn-warning btn-sm me-2" onclick="modifierProduit(${produit.id})"> Modifier</button>
                <button class="btn btn-danger btn-sm" onclick="supprimerProduit(${produit.id})"> Supprimer</button>
            </td>
        `;

        productTable.appendChild(row);
    });
}



form.addEventListener("submit", function (event) {
    event.preventDefault(); 

    const id = productIdInput.value ? parseInt(productIdInput.value) : null;
    const nom = productNameInput.value.trim();//compacter =>strip en python
    const prix = parseFloat(productPriceInput.value);

    if (nom === "" || isNaN(prix) || prix <= 0) {
        //sweetalert
        alert("Veuillez entrer un nom et un prix valide.");
        return;
    }

    if (id) {
       
        let produit = produits.find(p => p.id === id);
        if (produit) {
            produit.nom = nom;
            produit.prix = prix;
        }
    } else {
      
        let newId = produits.length > 0 ? Math.max(...produits.map(p => p.id)) + 1 : 1;
        produits.push({ id: newId, nom, prix });
    }

    form.reset(); 
    productIdInput.value = ""; 
    afficherProduits(); 
});


function modifierProduit(id) {
    let produit = produits.find(p => p.id === id);
    if (produit) {
        productIdInput.value = produit.id;
        productNameInput.value = produit.nom;
        productPriceInput.value = produit.prix;
    }
}


function supprimerProduit(id) {
    //vous pouvez utiliser des sweetalert
    if (window.confirm("Voulez-vous vraiment supprimer ce produit ?")) {
        produits = produits.filter(p => p.id !== id);
        afficherProduits(); 
    }
}

//au chargement de la page (onload)
afficherProduits();
