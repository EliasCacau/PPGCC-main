from django.urls import path
from upload.views import *;
from django.conf import settings
from django.conf.urls.static import static

app_name = "upload"

urlpatterns = [
    
    path('upload/',upload, name="upload"),
    path('salvar_arquivo',salvar_arquivo),

]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )