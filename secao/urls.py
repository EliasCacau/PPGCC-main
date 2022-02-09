from django.urls import path
from secao.views import *;
from django.conf import settings
from django.conf.urls.static import static

app_name = "secao"

urlpatterns = [
    
    path('salvar_arquivo',salvar_arquivo),
    path('secao/',secao, name="secao"),

]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )