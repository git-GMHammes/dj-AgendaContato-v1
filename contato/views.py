from django.shortcuts import render
# Importado do models
from .models import ContatoDj
# Create your views here.

def index(request):
    # recebeDbContatos - Variável que recebe os dados do DB
    # HtmlContatos - Variável que recebe o a variável em um dicionário {'':''}
    # Para exibir no arquivo [APP]/templates/index.html
    
    recebeDbContatos = ContatoDj.objects.all()
    return render(request, 'contato/index.html', {
        'HtmlContatos' : recebeDbContatos
    })

def exibeContato(request, contato_id):
    # var - descricao
    
    recebeDbContato = ContatoDj.objects.get(id=contato_id)
    return render(request, 'contato/exibeContato.html', {
        'HtmlContato' : recebeDbContato
    })