document.addEventListener('DOMContentLoaded', function() {
    const typeVehiculeSelect = document.getElementById('id_type_vehicule'); // Remplacez 'id_type_vehicule' par l'ID réel si différent

    typeVehiculeSelect.addEventListener('change', function() {
        const terrestreDiv = document.getElementById('terrestreDiv');
        const airDiv = document.getElementById('airDiv');
        const aquaDiv = document.getElementById('aquaDiv');
        const deplacementDiv = document.getElementById('deplacementDiv');
        

        if (this.value === 'Terrestre') {
            terrestreDiv.style.display = 'block'; // Afficher le formulaire terrestre
        } else {
            terrestreDiv.style.display = 'none'; // Masquer le formulaire terrestre
        }
        if (this.value === 'Aquatique') {
            aquaDiv.style.display = 'block'; // Afficher le formulaire terrestre
        } else {
            aquaDiv.style.display = 'none'; // Masquer le formulaire terrestre
        }
        if (this.value === 'Aérien') {
            airDiv.style.display = 'block'; // Afficher le formulaire terrestre
        } else {
            airDiv.style.display = 'none'; // Masquer le formulaire terrestre
        }
        
    });
});

function toggleCompartiment(id) {
    const compartiment = document.getElementById(id);
    if (compartiment.style.display === "none" || compartiment.style.display === "") {
        compartiment.style.display = "block";
    } else {
        compartiment.style.display = "none";
    }
}

function startRobotAnimation() {
    const robotBtn = document.getElementById('robotBtn');
    const effectDiv = document.getElementById('robotEffect');
    const mainCompartiment = document.getElementById('compartiment');

    robotBtn.style.display = "none"; // Cacher le bouton dès le début de l'animation
    effectDiv.style.display = "block"; // Afficher "Chargement..."

    setTimeout(() => {
        effectDiv.style.display = "none"; // Cacher "Chargement..."
        mainCompartiment.style.display = "block"; // Afficher le compartiment principal
    }, 900); // Après 1 seconde
}