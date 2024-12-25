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
    console.log("intem length"+totalItems);
    
    console.log("click");
    
    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = totalItems - 1;
    } else if (currentIndex >= totalItems) {
        currentIndex = 0;
    }

    const carouselImages = document.querySelector('.carousel-images');
    carouselImages.style.transform = `translateX(-${currentIndex * 100}%)`;
}
