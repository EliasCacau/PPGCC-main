from django.http import HttpResponse
from django.shortcuts import redirect, render

from secao.models import Arquivo

def secao(request):

    arquivos = Arquivo.objects.all()

    return render(request,'secao/index.html',{'arquivos':arquivos})

def salvar_arquivo(request):

    arquivo = str(request.FILES['arquivo'])
    arquivo = str(request.FILES['arquivo']).split('.')
    nomeArquivo = arquivo[0]
    extensaoArquivo = arquivo[1]

    newdoc = Arquivo(nome = nomeArquivo,url = str(request.FILES['arquivo']).split('.'),extensao = extensaoArquivo)
    newdoc.save(committed= True)

    return render(request,'secao/index.html')
