from xml.sax.handler import property_interning_dict
from django.shortcuts import render
from usuario.models import Usuario

# Create your views here.
def usuario(request):
    return render(request, "usuario/index.html")

def cadastro(request):
    return render(request, "usuario/cadastro.html")

def criar_usuario(request):
    if request.method=="POST":
        usuario_data=request.POST.dict()
        usuario = usuario_data.get("usuario")
        url_destino = usuario_data.get("url_destino")
        url_erro = usuario_data.get("url_erro")
        tipo_usuario = usuario_data.get("tipo_usuario")
        status = usuario_data.get("status")
        senha1 = usuario_data.get("senha1")
        senha2 = usuario_data.get("senha2")
        tipo_usuario = usuario_data.get("tipo_usuario")
        
        
        novo_usuario = Usuario(usuario=usuario, senha=senha1, ativado=status, permissao=tipo_usuario)
        novo_usuario.save()
    return render(request, "usuario/index.html")

