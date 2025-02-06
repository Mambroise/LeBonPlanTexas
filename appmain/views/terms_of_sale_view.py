# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/views/terms_of_sale_view.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.shortcuts import render

def terms_of_sale(request):
    lang = request.META.get('HTTP_ACCEPT_LANGUAGE', 'en').split(',')[0]
    print('langue du naviv=gateur : ', lang)
    if lang.startswith('fr'):
        return render(request, 'lebonplantexas/legal_terms/terms_of_sale_fr.html')
    elif lang.startswith('es'):
        return render(request, 'lebonplantexas/legal_terms/terms_of_sale_es.html')
    else:
        return render(request, 'lebonplantexas/legal_terms/terms_of_sale_us.html')
