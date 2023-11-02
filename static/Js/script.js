document.addEventListener('DOMContentLoaded', function() {
    const typeVehiculeSelect = document.getElementById('id_type_vehicule');

    const terrestreDiv = document.getElementById('terrestreDiv');
    const airDiv = document.getElementById('airDiv');
    const aquaDiv = document.getElementById('aquaDiv');
    const deplacementDiv = document.getElementById('deplacementDiv');
    
    function showDeplacementDiv() {
        deplacementDiv.style.display = 'block';
    }

    function hideDeplacementDiv() {
        deplacementDiv.style.display = 'none';
    }

    function resetAllDivs() {
        terrestreDiv.style.display = 'none';
        airDiv.style.display = 'none';
        aquaDiv.style.display = 'none';
        hideDeplacementDiv();
    }

    terrestreDiv.addEventListener('change', showDeplacementDiv);
// IMPORTANT : TROUVER UN MOYEN DE CACHER DEPLACEMENTDIV LORSQUE LON SELECTIONNE PLANEUR 
//             APRES AVOIR SELECTIONNE HELICES
    airDiv.addEventListener('change', function(){
        if (this.value !== 'Planeur') {
            showDeplacementDiv();
        } else {
            hideDeplacementDiv();
        }
    });

    aquaDiv.addEventListener('change', showDeplacementDiv);

    typeVehiculeSelect.addEventListener('change', function() {
        resetAllDivs();
        
        switch (this.value) {
            case 'Terrestre':
                terrestreDiv.style.display = 'block';
                break;
            case 'Aquatique':
                aquaDiv.style.display = 'block';
                break;
            case 'Aérien':
                airDiv.style.display = 'block';
                break;
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Votre code existant ici pour la logique de formulaire
    
    // Afficher robotEffect immédiatement au chargement de la page
    document.getElementById('robotEffect').style.display = 'block';

    // Autre code JavaScript pour les écouteurs d'événements et fonctions
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



document.getElementById('submitAll').addEventListener('click', function() {
    submitForm('formInspection');
    submitForm('formTransport');
    submitForm('formManipulation');
});

function submitForm(formId) {
    const form = document.getElementById(formId);
    form.submit(); // Cette commande soumet le formulaire
}
