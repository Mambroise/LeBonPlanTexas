# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/translation.py
# Author : Morice
# ---------------------------------------------------------------------------


from modeltranslation.translator import register, TranslationOptions
from .models import Attraction,ImageDisplayTheme,Category,CompanyInfo,Price

@register(Attraction)
class AttractionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ImageDisplayTheme)
class ImageDisplayThemeTranslation(TranslationOptions):
    fields = ('theme',)

@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)

@register(CompanyInfo)
class CompanyInfoTranslation(TranslationOptions):
    fields = ('name','legal_structure','tax_info','tax_math','phone','instagram',)

@register(Price)
class PricesTranslation(TranslationOptions):
    fields = ('service_name',
               'price_excl_tax',
               'main_tax_info','main_tax_math',
               'main_tax_name','second_tax_info',
               'second_tax_math','second_tax_name')