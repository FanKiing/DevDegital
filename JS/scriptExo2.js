document.getElementById("loanForm").addEventListener("submit", function (event) {
    event.preventDefault();

    // Récupérer les valeurs du formulaire
    let amount = parseFloat(document.getElementById("amount").value); //le montant total
    let duration = parseInt(document.getElementById("duration").value);//le nombre de mois
    let rate = parseFloat(document.getElementById("rate").value) / 100; //taux interet annuel
    let startDate = new Date(document.getElementById("startDate").value);// la date debut de crédit

    // Calcul de la mensualité avec la formule du crédit
    let monthlyRate = rate / 12;
    let monthlyPayment = (amount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -duration));

    // Affichage des résultats
    document.getElementById("results").innerHTML = `
        <h3>Résultats :</h3>
        <p><strong>Mensualité :</strong> ${monthlyPayment.toFixed(2)} €</p>
        <p><strong>Date de fin du prêt :</strong> ${addMonths(startDate, duration).toISOString().split("T")[0]}</p>
    `;

    // Générer le tableau des paiements
    let tableBody = document.querySelector("#schedule tbody");
    tableBody.innerHTML = "";  // Réinitialiser le tableau

    let remainingBalance = amount;
    for (let i = 1; i <= duration; i++) {
        let interest = remainingBalance * monthlyRate;
        let capital = monthlyPayment - interest;
        remainingBalance -= capital;

        let paymentDate = addMonths(startDate, i);
        let row = `
            <tr>
                <td>${i}</td>
                <td>${paymentDate.toISOString().split("T")[0]}</td>
                <td>${monthlyPayment.toFixed(2)}</td>
                <td>${capital.toFixed(2)}</td>
                <td>${interest.toFixed(2)}</td>
                <td>${remainingBalance.toFixed(2)}</td>
            </tr>
        `;
        tableBody.innerHTML += row;
    }
});

// Fonction pour ajouter un nombre de mois à une date
function addMonths(date, months) {
    let newDate = new Date(date);
    newDate.setMonth(newDate.getMonth() + months);
    return newDate;
}
