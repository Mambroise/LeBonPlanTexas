# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/translation.py
# Author : Morice
# ---------------------------------------------------------------------------


from modeltranslation.translator import register, TranslationOptions
from .models import Attraction,ImageDisplayTheme,Category

@register(Attraction)
class AttractionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ImageDisplayTheme)
class ImageDisplayThemeTranslation(TranslationOptions):
    fields = ('theme',)

@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)
