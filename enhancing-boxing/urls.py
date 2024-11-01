from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from theme.views import *

router = DefaultRouter()
if settings.DEBUG:
    urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Inizializza urlpatterns
urlpatterns += [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='theme.index'),
    path('<path:resource>', TemplateView.as_view(template_name='index.html'), name='catch_all'),
]

# Aggiungi static e media URL solo se DEBUG è True


# Aggiungi eventuali rotte del router qui, se necessario
urlpatterns += router.urls
