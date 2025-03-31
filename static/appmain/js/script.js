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

if (!window.location.pathname.includes('/register/') && !window.location.pathname.includes('/privacy_policy/')) {
    
    function addStyles(selector) {
        const style = `
            ${selector} {
                transition: height 0.3s ease-in-out;
            }
            ${selector}.small {
                height: 5rem;
                }
            .navbar-container.small {
                border-bottom: 1px solid var(--black-color);
                transition:  0.5s ease-in-out;
                background: var(--navbar-black);
            }
            #texas-star-base.small {
                width: 4rem;
                transition:  0.3s ease-in-out;
            }
            #service.small, #register.small {
                font-size: 1.5rem;
                font-weight: normal;
            }
            .title.small {
                font-size: 1.5rem;
                transition:  0.3s ease-in-out;
            }
            .title.small p {
                line-height: 1.35rem;
            }
            .title span.small {
                font-size: 2.5rem;
                transition:  0.3s ease-in-out;
            }
            .title-box.small {
                width: 30%;
                transition:  0.3s ease-in-out;
            }
            .title-box.small ul li {
                margin-bottom: 1rem;
            }
            .contact-link.small{
                border: 3px solid var(--brick-color);
                background: transparent;
                padding: 0.8rem 0.8rem;
            }
            .contact-link.small a {
                color: var(--white-texas);
            }
    
        `;
        const styleTag = document.createElement('style');
        styleTag.innerHTML = style;
        document.head.appendChild(styleTag);
    }
    
    addStyles(navbarSelector);
    
    const navBox = document.querySelector('.nav-box')
    const navContain = document.querySelector('.navbar-container')
    const star = document.querySelector('#texas-star-base');
    const service = document.querySelector('#service');
    const register = document.querySelector('#register');
    const title = document.querySelector('.title')
    const titleSpan = document.querySelector('.title span')
    const titleBox = document.querySelector('.title-box')
    const contactBox = document.querySelector('.contact-box')
    const contactLink = document.querySelector('.contact-link');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 10) {
            navbar.classList.add('small');
            navContain.classList.add('small');
            star.classList.add('small');
            service.classList.add('small');
            register.classList.add('small');
            title.classList.add('small');
            titleSpan.classList.add('small');
            titleBox.classList.add('small');
            contactBox.classList.add('small');
            contactLink.classList.add('small');
    
        } else {
            navbar.classList.remove('small');
            navContain.classList.remove('small');
            star.classList.remove('small');
            service.classList.remove('small');
            register.classList.remove('small');
            title.classList.remove('small');
            titleSpan.classList.remove('small');
            titleBox.classList.remove('small');
            contactBox.classList.remove('small');
            contactLink.classList.remove('small')
    
        }
    });
}

// NAVBAR BURGER

function toggleMenu() {
    
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
}

// TEXAS CULTURE WORDS BANNER
document.addEventListener('DOMContentLoaded', () => {
    
    if (window.location.pathname === '/fr/' ||
         window.location.pathname === '/en/' ||
          window.location.pathname === '/es/'||
           window.location.pathname.includes('/thanku/')) {

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

// WHO_ARE_WE PAGE SCRIPT
    if (window.location.pathname.includes("/contact/")) {
        function updateClocks() {

            const userLang = navigator.language || navigator.userLanguage;
            const isEnglish = userLang.startsWith('en');
            const format = isEnglish ? 'en-US' : 'fr-FR'; // Format US or FR
            const secondCity = isEnglish ? "EL PASO" : "PARIS";
            const secondTimezone = isEnglish ? "America/Denver" : "Europe/Paris";

            const options = { timeZone: 'America/Chicago', hour: '2-digit', minute: '2-digit', second: '2-digit' };
            const austinTime = new Intl.DateTimeFormat(format,options).format(new Date());          
            
            options.timeZone = secondTimezone;
            const parisTime = new Intl.DateTimeFormat(format, options).format(new Date());

            // Updating html elements
            document.getElementById('second-city').textContent = secondCity;
            document.getElementById('clock-austin').textContent = austinTime;
            document.getElementById('clock-paris').textContent = parisTime;
        }

        setInterval(updateClocks, 1000);
        updateClocks();
    }

});



