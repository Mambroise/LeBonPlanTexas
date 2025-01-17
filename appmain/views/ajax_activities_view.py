# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/templates/lebonplantexas/ajax_activites_view.html
# Author : Morice
# ---------------------------------------------------------------------------


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import FileForImage

@csrf_exempt
def get_activities(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        city = data.get('city')

        activities = FileForImage.objects.get()
        # Exemple de données des activités (remplacez par une requête à votre base de données)
        # activities = {
        #     'austin': [
        #         {'title': 'Le Capitole d\'Austin', 'description': "Le Capitole d'Austin, majestueux bâtiment en granit rose, incarne la grandeur du Texas avec son architecture imposante et ses jardins verdoyants. Une visite incontournable pour plonger dans l'histoire et admirer des vues panoramiques sur la ville depuis ses environs.", 'image_url': '/static/images/best_of_cities/austin/austin_capitole.jpg'},
        #         {'title': 'Concerts live à 6th street', 'description': "Plongez dans l’effervescence musicale de 6th Street à Austin, où des concerts live animent chaque soir les bars et salles de cette rue emblématique. Une expérience vibrante qui reflète l’âme de la capitale mondiale de la musique live.", 'image_url': '/static/images/best_of_cities/austin/austin_6th_street.png'},
        #         {'title': 'Restaurant The Oasis ', 'description': "The Oasis, perché sur une falaise surplombant le lac Travis, offre une vue spectaculaire, particulièrement au coucher du soleil. Ce restaurant emblématique allie cuisine savoureuse et panoramas à couper le souffle, parfait pour une expérience mémorable.", 'image_url': '/static/images/best_of_cities/austin/the_oasis.png'},
        #     ],
        #     'dallas': [
        #         {'title': 'Rodeo Show', 'description': "Le Stockyards de Fort Worth vous plonge dans l’ambiance authentique du Texas avec ses rodéos palpitants. Une expérience captivante où traditions cow-boy et adrénaline se rencontrent dans une arène légendaire.", 'image_url': '/static/images/best_of_cities/dallas/bull_riding_fw.png'},
        #         {'title': 'Art contemporain', 'description': 'L’œuvre "The Eye", une gigantesque sculpture hyperréaliste d’un œil humain au cœur de Dallas, intrigue et fascine les passants. Ce symbole décalé ajoute une touche artistique unique au paysage urbain de la ville.', 'image_url': '/static/images/best_of_cities/dallas/dallas_eye_close.jpg'},
        #         {'title': 'Sixth Floor Museum', 'description': 'Retracez avec émotion l’histoire de l’assassinat de John F. Kennedy depuis l’ancien dépôt de livres scolaires. Un lieu chargé d’histoire, offrant une plongée captivante dans un événement marquant du XXe siècle.', 'image_url': '/static/images/best_of_cities/dallas/fusil_jfk.png'},
        #     ],
        #     'houston': [
        #         {'title': 'Visite du space center', 'description': 'Destination incontournable pour les passionnés d\'astronomie, offrant une immersion fascinante dans l\'histoire de la conquête spatiale. Expositon interactives, artefacts de la NASA et des visites guidées de mission, c’est un voyage unique au cœur de l’exploration de l\'univers.', 'image_url': '/static/images/best_of_cities/houston/houston_nasa.png'},
        #         {'title': 'Buffalo Bayou Park', 'description': 'Un havre de verdure avec ses sentiers de randonnée, ses espaces de loisirs et ses vues pittoresques sur le bayou. Un endroit idéal pour s\'évader en plein air, à quelques pas du centre-ville, tout en découvrant l\'histoire naturelle de la région.', 'image_url': '/static/images/best_of_cities/houston/buffalo_bayou_park.png'},
        #         {'title': 'Waterwall Park', 'description': 'Une oasis urbaine avec une impressionnante fontaine en arc de cercle, parfaite pour une pause rafraîchissante. Ce lieu emblématique offre une expérience apaisante et des clichés mémorables au cœur de la ville.', 'image_url': '/static/images/best_of_cities/houston/waterwall.png'},
        #     ],
        #     'san_antonio': [
        #         {'title': 'Fort Alamo', 'description': 'Un site historique emblématique, où s\'est déroulée la célèbre bataille de 1836. Aujourd\'hui, il raconte l’histoire de la résistance texane à travers ses bâtiments restaurés et ses expositions poignantes, offrant une immersion dans le combat pour l\'indépendance du Texas.', 'image_url': '/static/images/best_of_cities/san_antonio/alamo_san_antonio.png'},
        #         {'title': 'Riverwalk', 'description': 'Le River Walk de San Antonio est un réseau pittoresque de canaux bordés de restaurants, de boutiques et de ponts, offrant une atmosphère charmante et relaxante. Idéal pour une promenade paisible ou une croisière, c\'est l\'endroit parfait pour découvrir la ville sous un angle unique.', 'image_url': '/static/images/best_of_cities/san_antonio/riverwalk.jpg'},
        #         {'title': 'Lone star range', 'description': 'Un centre de tir et de loisirs en plein air offrant une expérience immersive pour les passionnés de sports de tir. Avec ses installations modernes et son cadre naturel, c\'est l\'endroit idéal pour s\'adonner à des activités de tir sécurisées tout en profitant de la campagne texane.', 'image_url': '/static/images/best_of_cities/san_antonio/range_laura.jpg'},
        #     ],
        #     'rockport': [
        #         {'title': 'Rockport beach', 'description': 'Une charmante étendue de sable au bord du golfe du Mexique, idéale pour une escapade familiale. Avec ses eaux calmes, ses aires de pique-nique et son ambiance détendue, c’est un lieu parfait pour profiter du soleil et des activités nautiques.', 'image_url': '/static/images/best_of_cities/rockport/rockport_beach.jpg'},
        #         {'title': 'fresh seafood', 'description': 'Profitez de délicieux fruits de mer et poissons fraichement débarqués des bateaux dans les magasins du port de rockport', 'image_url': '/static/images/best_of_cities/rockport/rockport_shrimp.jpg'},
        #         {'title': 'surf session', 'description': 'Aransas Beach, à quelques minutes de Rockport, séduit par ses vastes étendues de sable et ses vagues parfaites pour le surf. Location et sessions de surf accessibles tous sur des plages interminables.', 'image_url': '/static/images/best_of_cities/rockport/aransas_beach.jpg'},
        #     ],
            # add more cities
        # }

        return JsonResponse({'activities': activities.get(city, [])})

    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
