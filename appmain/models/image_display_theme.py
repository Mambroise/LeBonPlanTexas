# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/models/image_display_theme.py
# Author : Morice
# ---------------------------------------------------------------------------


# on index page, this entity allows you to change the title related to the cards and images . 
# defaut = les classiques du texas (texas' classics)
from django.db import models

class ImageDisplayTheme(models.Model):
    theme = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.theme