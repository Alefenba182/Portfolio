from django.shortcuts import render
from .models import  Categoria, Certificado, Inicio, Perfil, Projeto, Sobre,Contato

def index(request):

    # Home
    inicio = Inicio.objects.latest('updated')

    # About
    sobre = Sobre.objects.latest('updated')
    perfis = Perfil.objects.filter(sobre=sobre)

    # Skills
    categorias = Categoria.objects.all()

    # Portfolio
    projetos = Projeto.objects.all()
    
    #Certificados
    certificados = Certificado.objects.all()
    
    #Contato
    contato = Contato.objects.first()

    context = {
        'inicio': inicio,
        'sobre': sobre,
        'perfis': perfis,
        'categorias': categorias,
        'projetos': projetos,
        'certificados': certificados,
        'contato':contato,
    }


    return render(request, 'index.html', context)
