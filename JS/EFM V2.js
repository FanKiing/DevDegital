document.getElementById('invoiceForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const id = document.getElementById('ID').value;
    const title = document.getElementById('titre').value;
    const quantity = parseFloat(document.getElementById('quantity').value);
    const price = parseFloat(document.getElementById('price').value);
    const tva = parseFloat(document.getElementById('tva').value);

    const totalHT = quantity * price;
    const totalTTC = totalHT * (1 + tva / 100);

    const tableBody = document.getElementById('myProduct');
    const newRow = document.createElement('tr');

    newRow.innerHTML = `
        <td>${id}</td>
        <td>${title}</td>
        <td>${quantity}</td>
        <td>${price.toFixed(2)} €</td>
        <td>${tva}%</td>
        <td>${totalHT.toFixed(2)} €</td>
        <td>${totalTTC.toFixed(2)} €</td>
        <td><button class="btn btn-danger btn-sm" onclick="deleteRow(this)">Supprimer</button></td>
    `;

    tableBody.appendChild(newRow);

    updateTotals();
    document.getElementById('invoiceForm').reset();
});

function deleteRow(button) {
    const row = button.closest('tr');
    row.remove();
    updateTotals();
}

function updateTotals() {
    const rows = document.querySelectorAll('#myProduct tr');
    let totalHT = 0;
    let totalTTC = 0;

    rows.forEach(row => {
        totalHT += parseFloat(row.cells[5].textContent);
        totalTTC += parseFloat(row.cells[6].textContent);
    });

    document.getElementById('totalHT').textContent = totalHT.toFixed(2);
    document.getElementById('totalTTC').textContent = totalTTC.toFixed(2);
}