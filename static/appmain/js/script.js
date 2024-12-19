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