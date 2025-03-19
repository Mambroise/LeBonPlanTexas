# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/templates/lebonplantexas/ajax_activites_view.html
# Author : Morice
# ---------------------------------------------------------------------------

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import FileForImage, Attraction


@csrf_exempt
def get_activities(request):
    if request.method == 'POST':
        try:
            # Charger les données depuis la requête
            data = json.loads(request.body)
            city_id = data.get('city')

            if not city_id:
                return JsonResponse({'error': 'City id is required.'}, status=400)

            # Trouver le fichier associé à la ville
            try:
                file = FileForImage.objects.get(pk=city_id)
            except FileForImage.DoesNotExist:
                return JsonResponse({'error': 'City not found.'}, status=404)

            # Récupérer les attractions associées
            activities = Attraction.objects.filter(file=file)
            for activity in activities:
                print(activity.image_url)
            # Convertir les attractions en liste de dictionnaires
            activities_list = [
                {
                    'id': activity.id,
                    'title': activity.title,
                    'description': activity.description,
                    'image_url': activity.image_url.url if activity.image_url else None, 
                }
                for activity in activities
            ]

            # Retourner les activités sérialisées
            return JsonResponse({'activities': activities_list})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid format.'}, status=400)
        except Exception as e:
            # Log l'erreur pour le débogage
            print(f'Erreur : {e}')
            return JsonResponse({'error': f'Server error. {e}'}, status=500)

    # Si la méthode HTTP n'est pas POST
    return JsonResponse({'error': 'Not authorized method.'}, status=405)
