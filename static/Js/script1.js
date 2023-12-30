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
    const effectDiv = document.getElementById('robotEffect');

    // Génère un seul caractère Matrix qui tombe
    function generateMatrixCharacter() {
        const character = document.createElement('span');
        character.textContent = String.fromCharCode(33 + Math.random() * (127 - 33)); // Caractères imprimables ASCII
        character.classList.add('matrix-character');
        character.style.left = Math.random() * 100 + 'vw';
        character.style.opacity = Math.random(); // Varie l'opacité pour plus de réalisme
        // Durée et délai aléatoires pour l'animation
        const duration = Math.random() * 5 + 5; // Entre 5 et 10 secondes
        character.style.setProperty('--animation-duration', `${duration}s`);
        character.style.setProperty('--animation-delay', `${-duration}s`);
        
        effectDiv.appendChild(character);

        // Supprime le caractère après qu'il a fini de tomber pour nettoyer le DOM
        character.addEventListener('animationend', () => {
            effectDiv.removeChild(character);
        });
    }

    // Génère plusieurs caractères pour l'animation
    function populateMatrix() {
        const numberOfCharacters = window.innerWidth / 10; // Un caractère tous les 10 pixels de largeur d'écran
        for (let i = 0; i < numberOfCharacters; i++) {
            generateMatrixCharacter();
        }
    }

    // Démarre l'animation et repopule de temps en temps pour ajouter de nouveaux caractères
    populateMatrix();
    setInterval(populateMatrix, 5000); // Toutes les 5 secondes

    // Optionnel : arrêter l'animation après un certain temps
    // setTimeout(() => effectDiv.style.display = 'none', 30000); // Arrête après 30 secondes
}

// Démarrez l'animation lorsque le contenu est chargé
document.addEventListener('DOMContentLoaded', startRobotAnimation);








document.getElementById('submitAll').addEventListener('click', function() {
    submitForm('formInspection');
    submitForm('formTransport');
    submitForm('formManipulation');
});

function submitForm(formId) {
    const form = document.getElementById(formId);
    form.submit(); // Cette commande soumet le formulaire
}