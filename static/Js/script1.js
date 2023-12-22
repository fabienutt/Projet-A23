document.addEventListener("DOMContentLoaded", function () {
    const bodyElements = document.querySelectorAll('.deconstruct-element-body');
    const headerElements = document.querySelectorAll('.deconstruct-element-header');

    function animateElementIn(element) {
        TweenMax.fromTo(
            element,
            1.5, // durée de l'animation
            {
                opacity: 0,
                y: 30, // décalage vers le bas
                scale: 0.8 // échelle initiale
            },
            {
                opacity: 1,
                y: 0,
                scale: 1,
                ease: Power4.easeInOut // courbe d'animation
            }
        );
    }

    // Animation pour les éléments du corps (body)
    bodyElements.forEach(animateElementIn);

    // Animation pour les éléments de l'en-tête (header)
    headerElements.forEach(animateElementIn);
});
