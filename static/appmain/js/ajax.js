// # ---------------------------------------------------------------------------
// #                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
// # ---------------------------------------------------------------------------
// # File   : static/appmain/js/ajax.js
// # Author : Morice
// # ---------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', function () {
    
    if (window.location.pathname === '/fr/' || window.location.pathname === '/en/') {
        
        const form = document.getElementById('city-selector-form');
        const container = document.getElementById('activities-container');
        
        if (form && container) {
            // Fonction pour charger les activités
            const lang = window.location.pathname.split('/')[1];
            function loadActivities(city_id) {
                fetch(`/${lang}/get_activities/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}' // Inclure le token CSRF pour les requêtes POST
                    },
                    body: JSON.stringify({ city: city_id })
                })
                    .then(response => response.json())
                    .then(data => {
                        container.innerHTML = ''; // Réinitialiser le contenu du conteneur
                        
                        if (data.activities && data.activities.length > 0) {
                            data.activities.forEach(activity => {
                                const card = document.createElement('div');
                                card.className = 'card';
                                card.innerHTML = `
                                    <div class="card-image">
                                        <img src="${activity.image_url}" alt="${activity.title}">
                                    </div>
                                    <div>
                                        <h4 class="text-center c-white card-title">${activity.title}</h4>
                                        <hr class="hr">
                                    </div>
                                    <div class="card-content">
                                        <p class="no-mt">${activity.description}</p>
                                    </div>
                                `;
                                container.appendChild(card);
                            });
                        } else {
                            container.innerHTML = '<p class="text-center">Aucune activité disponible pour cette ville.</p>';
                        }
                    })
                    .catch(error => {
                        console.error('Erreur lors de la récupération des activités:', error);
                    });
            }

            // Load dallas data on document loading
            loadActivities(2);

            // add listener for select button
            form.addEventListener('change', function (e) {
                e.preventDefault(); // prevent reload on submit
                const city_id = document.getElementById('city-select').value;
                loadActivities(city_id); 
            });
        }
    }
});
