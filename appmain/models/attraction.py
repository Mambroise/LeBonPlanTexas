# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/attraction.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db import models
from .file_for_image import FileForImage 
from ..services.attraction_service import upload_to_file_for_image 

class Attraction(models.Model):
    file = models.ForeignKey(FileForImage, on_delete=models.CASCADE, related_name='attractions')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to_file_for_image)  # Utilisation de la fonction externe
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


