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
        }

        #who.small, #register.small {
            font-size: 12px;
        }

        .nav-register-box.small, .nav-who-box.small {
            margin-top: 40px;
        }
        .nav-box.small {
            width: 40%;
        }
    `;
    const styleTag = document.createElement('style');
    styleTag.innerHTML = style;
    document.head.appendChild(styleTag);
}

addStyles(navbarSelector);

const who = document.querySelector('#who');
const register = document.querySelector('#register');
const navRegisterBox = document.querySelector('.nav-register-box');
const navWhoBox = document.querySelector('.nav-who-box');
const navBox = document.querySelector('.nav-box')

window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navbar.classList.add('small');
        who.classList.add('small');
        register.classList.add('small');
        navRegisterBox.classList.add('small');
        navWhoBox.classList.add('small');
        navBox.classList.add('small');
    } else {
        navbar.classList.remove('small');
        who.classList.remove('small');
        register.classList.remove('small');
        navRegisterBox.classList.remove('small');
        navWhoBox.classList.remove('small');
        navBox.classList.remove('small');
    }
});
