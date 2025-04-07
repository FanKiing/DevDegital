let livre = document.getElementById("livre");
let prix = document.getElementById("prix");
let tbody = document.getElementById("tbody");
let resultat = document.getElementById("resultat");

let livres = [
    { "ID": "001", "titre": "Langage C", "image": "c.png", "prix": 150 },
    { "ID": "002", "titre": "Programmation Javascript", "image": "js.png", "prix": 250 },
];

let currentEditId = null;
let currentDeleteButton = null;

function charger() {
    livres.forEach(livre => {
        addRow(livre);
    });
    updateTotal();
}

function addRow(livre) {
    tbody.innerHTML += `
        <tr>
            <td>${livre.ID}</td>
            <td>${livre.titre}</td>
            <td>${livre.prix}</td>
            <td>
                <button class="btn btn-warning btn-sm me-2" onclick="openEditModal('${livre.ID}', '${livre.titre}', '${livre.prix}')">Modifier</button>
                <button class="btn btn-danger btn-sm" onclick="openDeleteModal(this)">Supprimer</button>
            </td>
        </tr>
    `;
}

function ajouter(event) {
    event.preventDefault();
    let livreValue = livre.value;
    let prixValue = prix.value;

    if (livreValue.trim() === "" || prixValue.trim() === "") {
        alert("Veuillez remplir tous les champs !");
        return;
    }

    const newBook = {
        ID: Math.random().toString(36).substr(2, 5),
        titre: livreValue,
        prix: parseFloat(prixValue)
    };
    livres.push(newBook);
    addRow(newBook);
    updateTotal();
    livre.value = "";
    prix.value = "";
}


function retirer(event) {
    event.preventDefault();
    tbody.innerHTML = "";
    livres = [];
    updateTotal();
}

function openEditModal(id, titre, prix) {
    currentEditId = id;
    document.getElementById("editId").value = id;
    document.getElementById("editTitre").value = titre;
    document.getElementById("editPrix").value = prix;
    new bootstrap.Modal(document.getElementById('editModal')).show();
}

function saveEdit() {
    const titre = document.getElementById("editTitre").value;
    const prix = document.getElementById("editPrix").value;

    const index = livres.findIndex(livre => livre.ID === currentEditId);
    livres[index].titre = titre;
    livres[index].prix = parseFloat(prix);

    const row = tbody.querySelector(`tr td:first-child`).parentElement;
    row.children[1].textContent = titre;
    row.children[2].textContent = prix;

    updateTotal();
    new bootstrap.Modal(document.getElementById('editModal')).hide();
}

function openDeleteModal(button) {
    currentDeleteButton = button;
    new bootstrap.Modal(document.getElementById('deleteModal')).show();
}

function confirmDelete() {
    const row = currentDeleteButton.closest("tr");
    const id = row.querySelector("td:first-child").textContent;
    livres = livres.filter(livre => livre.ID !== id);
    row.remove();
    updateTotal();
    new bootstrap.Modal(document.getElementById('deleteModal')).hide();
}

function updateTotal() {
    const total = livres.reduce((sum, livre) => sum + livre.prix, 0);
    resultat.textContent = total;
}

charger();