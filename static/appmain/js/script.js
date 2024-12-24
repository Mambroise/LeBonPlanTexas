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
            transition: height 0.5s ease-in-out;
            background: linear-gradient(135deg, rgb(47, 80, 212), rgb(30, 33, 165), rgb(35, 72, 219));
        }

        #who.small, #register.small {
            font-size: 12px;
            transition:  0.3s ease-in-out;
        }

        .nav-register-box.small, .nav-who-box.small {
            margin-top: 40px;
        }
        .nav-box.small {
            width: 40%;
            transition:  0.5s ease-in-out;
        }
        .title.small {
            margin-top: 15px;
            font-size: 25px;
            transition:  0.3s ease-in-out;
        }
        .title span.small {
            font-size: 35px;
            transition:  0.3s ease-in-out;
        }
        .title-box.small {
            width: 30%;
            transition:  0.3s ease-in-out;
        }
        .contact-box.small {
            margin-top: 3%;
            width: 30%;
            transition:  0.3s ease-in-out;
        }
        .contact-box.small p {
            font-size: 20px;
            transition:  0.3s ease-in-out;
        }
        .white-flag-div.small {
            border: 2px solid var(--white-texas);
        }
        .red-flag-div.small {
            border: 2px solid var(--red-texas);
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
const title = document.querySelector('.title')
const titleSpan = document.querySelector('.title span')
const titleBox = document.querySelector('.title-box')
const contactBox = document.querySelector('.contact-box')
const redFlag = document.querySelector('.red-flag-div')
const whiteFlag = document.querySelector('.white-flag-div')


window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navbar.classList.add('small');
        who.classList.add('small');
        register.classList.add('small');
        navRegisterBox.classList.add('small');
        navWhoBox.classList.add('small');
        navBox.classList.add('small');
        title.classList.add('small');
        titleSpan.classList.add('small');
        titleBox.classList.add('small');
        contactBox.classList.add('small');
        redFlag.classList.add('small');
        whiteFlag.classList.add('small');
    } else {
        navbar.classList.remove('small');
        who.classList.remove('small');
        register.classList.remove('small');
        navRegisterBox.classList.remove('small');
        navWhoBox.classList.remove('small');
        navBox.classList.remove('small');
        title.classList.remove('small');
        titleSpan.classList.remove('small');
        titleBox.classList.remove('small');
        contactBox.classList.remove('small');
        redFlag.classList.remove('small');
        whiteFlag.classList.remove('small');
    }
});
