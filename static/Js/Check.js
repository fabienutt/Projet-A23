document.addEventListener('DOMContentLoaded', function() {
    // Récupérez tous les boutons
    const buttons = document.querySelectorAll('.groupe-button');

    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Récupérez l'ID du div des sous-items à basculer
            const toggleId = button.getAttribute('data-toggle-id');
            const subItemsDiv = document.getElementById(toggleId);

            // Basculez l'affichage des sous-items
            if (subItemsDiv.style.display === 'none' || subItemsDiv.style.display === '') {
                subItemsDiv.style.display = 'block';
            } else {
                subItemsDiv.style.display = 'none';
            }
        });
    });
});
