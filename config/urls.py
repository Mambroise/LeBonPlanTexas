
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# Routes principales
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appmain.urls')),
]

# Ajout du support des langues
urlpatterns = i18n_patterns(*urlpatterns)

# Ajout du support des fichiers media en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
