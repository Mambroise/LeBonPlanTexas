# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/templates/lebonplantexas/ajax_activites_view.html
# Author : Morice
# ---------------------------------------------------------------------------


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def get_activities(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        city = data.get('city')

        # Exemple de données des activités (remplacez par une requête à votre base de données)
        activities = {
            'austin': [
                {'title': 'Le Capitole d\'Austin', 'description': "Le Capitole d'Austin, majestueux bâtiment en granit rose, incarne la grandeur du Texas avec son architecture imposante et ses jardins verdoyants. Une visite incontournable pour plonger dans l'histoire et admirer des vues panoramiques sur la ville depuis ses environs.", 'image_url': '/static/images/best_of_cities/austin/austin_capitole.jpg'},
                {'title': 'Concerts live à 6th street', 'description': "Plongez dans l’effervescence musicale de 6th Street à Austin, où des concerts live animent chaque soir les bars et salles de cette rue emblématique. Une expérience vibrante qui reflète l’âme de la capitale mondiale de la musique live.", 'image_url': '/static/images/best_of_cities/austin/austin_6th_street.png'},
                {'title': 'Restaurant The Oasis ', 'description': "The Oasis, perché sur une falaise surplombant le lac Travis, offre une vue spectaculaire, particulièrement au coucher du soleil. Ce restaurant emblématique allie cuisine savoureuse et panoramas à couper le souffle, parfait pour une expérience mémorable.", 'image_url': '/static/images/best_of_cities/austin/the_oasis.png'},
            ],
            'dallas': [
                {'title': 'Rodeo Show', 'description': "Le Stockyards de Fort Worth vous plonge dans l’ambiance authentique du Texas avec ses rodéos palpitants. Une expérience captivante où traditions cow-boy et adrénaline se rencontrent dans une arène légendaire.", 'image_url': '/static/images/best_of_cities/dallas/bull_riding_fw.png'},
                {'title': 'Art contemporain', 'description': 'L\’œuvre "The Eye", une gigantesque sculpture hyperréaliste d\’un œil humain au cœur de Dallas, intrigue et fascine les passants. Ce symbole décalé ajoute une touche artistique unique au paysage urbain de la ville.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye_close.jpg'},
                {'title': 'Sixth Floor Museum', 'description': 'Retracez avec émotion l\’histoire de l’assassinat de John F. Kennedy depuis l’ancien dépôt de livres scolaires. Un lieu chargé d\’histoire, offrant une plongée captivante dans un événement marquant du XXe siècle.', 'image_url': '/static/images/best_of_cities/dallas/fusil_jfk.png'},
            ],
            'houston': [
                {'title': 'Rodeo Show', 'description': 'Découvrez un vrai spectacle de rodéo.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
                {'title': 'Musée d\'Art', 'description': 'Admirez des œuvres exceptionnelles.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
                {'title': 'Shopping', 'description': 'Profitez des meilleures boutiques.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
            ],
            'san_antonio': [
                {'title': 'Rodeo Show', 'description': 'Découvrez un vrai spectacle de rodéo.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
                {'title': 'Musée d\'Art', 'description': 'Admirez des œuvres exceptionnelles.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
                {'title': 'Shopping', 'description': 'Profitez des meilleures boutiques.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
            ],
            'port_isabel': [
                {'title': 'Rodeo Show', 'description': 'Découvrez un vrai spectacle de rodéo.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
                {'title': 'Musée d\'Art', 'description': 'Admirez des œuvres exceptionnelles.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
                {'title': 'Shopping', 'description': 'Profitez des meilleures boutiques.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye.jpg'},
            ],
            # add more cities
        }

        return JsonResponse({'activities': activities.get(city, [])})

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
