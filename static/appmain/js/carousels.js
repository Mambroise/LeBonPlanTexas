// # ---------------------------------------------------------------------------
// #                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
// # ---------------------------------------------------------------------------
// # File   : static/appmain/js/carrousels.js
// # Author : Morice
// # ---------------------------------------------------------------------------


// bdd-activities 
let currentIndex = 0;

function moveCarousel(direction) {
    const items = document.querySelectorAll('.carousel-item');
    const totalItems = items.length;
    
    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = totalItems - 1;
    } else if (currentIndex >= totalItems) {
        currentIndex = 0;
    }

    const carouselImages = document.querySelector('.carousel-images');
    carouselImages.style.transform = `translateX(-${currentIndex * 33.33}%)`;
}

// Fonction pour changer automatiquement les images
function autoMoveCarousel() {
    moveCarousel(1); // Passe à l'image suivante
}

// Ajouter un intervalle de 6 secondes
setInterval(autoMoveCarousel, 6000);
