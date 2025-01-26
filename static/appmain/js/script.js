// # ---------------------------------------------------------------------------
// #                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
// # ---------------------------------------------------------------------------
// # File   : static/appmain/js/script.js
// # Author : Morice
// # ---------------------------------------------------------------------------


document.addEventListener("DOMContentLoaded", function () {
// Étape 3 : Gestion des catégories
const categoryCards = document.querySelectorAll(".category-card");
const selectedCategoriesInput = document.getElementById("selected-categories");
let selectedCategories = [];

categoryCards.forEach(card => {
    card.addEventListener("click", function () {
        const categoryId = this.getAttribute("data-category-id");
        
        // Ajouter ou supprimer la catégorie de la sélection
        if (selectedCategories.includes(categoryId)) {
            selectedCategories = selectedCategories.filter(id => id !== categoryId);
            this.classList.remove("selected");
        } else {
            selectedCategories.push(categoryId);
            this.classList.add("selected");
        }

        // Mettre à jour l'input caché
        selectedCategoriesInput.value = selectedCategories.join(",");
    });
});
});


// NAVBAR FUNCTIONAL PROGRAMMING
const navbarSelector = 'nav.navbar';
const navbar = document.querySelector(navbarSelector);

function addStyles(selector) {
    const style = `
        ${selector} {
            transition: height 0.3s ease-in-out;
        }
        ${selector}.small {
            height: 100px;
            transition: height 0.3s ease-in-out;
            background: var(--navbar-black);
            border-bottom: 1px solid var(--black-color);
        }

        #who.small, #register.small {
            font-size: 1.05rem;
            transition:  0.3s ease-in-out;
        }

        .nav-box.small {
            width: 40%;
            transition:  0.5s ease-in-out;
        }
        .title.small {
            margin-top: 15px;
            font-size: 1.6rem;
            transition:  0.3s ease-in-out;
        }
        .title span.small {
            font-size: 2.2rem;
            transition:  0.3s ease-in-out;
        }
        .title-box.small {
            width: 30%;
            transition:  0.3s ease-in-out;
        }
        .flag-img.small {
            width: 2rem;
            }
        .flag-img-us.small {
            width: 2.4rem;
        }
        .contact-box.small {
            width: 30%;
            transition:  0.3s ease-in-out;
        }
        .contact-link.small{
            padding: 0.8rem 0.8rem;
        }
        .contact-link.small a {
            font-size: 0.8rem;
        }

    `;
    const styleTag = document.createElement('style');
    styleTag.innerHTML = style;
    document.head.appendChild(styleTag);
}

addStyles(navbarSelector);

const who = document.querySelector('#who');
const register = document.querySelector('#register');
const navBox = document.querySelector('.nav-box')
const title = document.querySelector('.title')
const titleSpan = document.querySelector('.title span')
const titleBox = document.querySelector('.title-box')
const contactBox = document.querySelector('.contact-box')
const flagImg = document.querySelector('.flag-img');
const flagImgUs = document.querySelector('.flag-img-us');
const contactLink = document.querySelector('.contact-link');

window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navbar.classList.add('small');
        who.classList.add('small');
        register.classList.add('small');
        navBox.classList.add('small');
        title.classList.add('small');
        titleSpan.classList.add('small');
        titleBox.classList.add('small');
        contactBox.classList.add('small');
        flagImg.classList.add('small');
        flagImgUs.classList.add('small');
        contactLink.classList.add('small');

    } else {
        navbar.classList.remove('small');
        who.classList.remove('small');
        register.classList.remove('small');
        navBox.classList.remove('small');
        title.classList.remove('small');
        titleSpan.classList.remove('small');
        titleBox.classList.remove('small');
        contactBox.classList.remove('small');
        flagImg.classList.remove('small')
        flagImgUs.classList.remove('small')
        contactLink.classList.remove('small')

    }
});

// NAVBAR BURGER

function toggleMenu() {
    console.log('click');
    
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

// TEXAS CULTURE WORDS BANNER
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/index/') {

        const words = document.querySelectorAll('.word');
        const banner = document.querySelector('.texas-banner');
        const fadeInTime = 300; // fade-in length (ms)
        const visibleTime = 4000; // Temps visible (ms)
        const fadeOutTime = 300; // fade-out length (ms)
        const pauseTime = 5000; // break between cycles (ms)
    
        // Fonction pour distribuer horizontalement et mélanger les positions
        function distributeWordsEvenly() {
            const totalWidth = banner.offsetWidth;
            const step = totalWidth / words.length; // Espacement horizontal
            const positions = Array.from({ length: words.length }, (_, i) => i * step); // Liste des positions horizontales
    
            // Mélanger les positions avec l'algorithme de Fisher-Yates
            for (let i = positions.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [positions[i], positions[j]] = [positions[j], positions[i]];
            }
    
            words.forEach((word, index) => {
                const top = Math.random() * (banner.offsetHeight - 50); // Position verticale aléatoire
                const rotation = Math.random() * 60 - 30; // Rotation aléatoire entre -30° et 30°
                word.style.left = `${positions[index]}px`;
                word.style.top = `${top}px`;
                word.style.transform = `rotate(${rotation}deg)`;
            });
        }
    
        // Fonction d'animation des mots
        function animateWords() {
            let delay = 0;
    
            words.forEach(word => {
                setTimeout(() => {
                    word.style.opacity = 1; // Fade in
                }, delay);
    
                setTimeout(() => {
                    word.style.opacity = 0; // Fade out
                }, delay + visibleTime);
    
                delay += fadeInTime + 200; // Espacement entre les mots
            });
    
            // Répéter après une pause
            setTimeout(() => {
                distributeWordsEvenly();
                animateWords();
            }, delay + fadeOutTime + pauseTime); // Ajouter une pause après tous les mots
        }
    
        // Initialiser l'animation
        distributeWordsEvenly();
        animateWords();
    }
});

