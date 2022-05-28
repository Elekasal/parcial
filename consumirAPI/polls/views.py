import requests

from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'home.html')


def home(request):
    url = 'https://www.cultura.gob.ar/api/v2.0/?format=json'
    response = requests.get(url)
    data = response.json()

    convocatorias = data['convocatorias']
    institutos = data['institutos']
    museos = data['museos']
    organismos = data['organismos']
    programas = data['programas']
    tramites = data['tramites']

    context = {
        'convocatorias': convocatorias,
        'institutos': institutos,
        'museos': museos,
        'organismos': organismos,
        'programas': programas,
        'tramites': tramites,
    }

    return render(request, 'consumirAPI/home.html', context)

def organismos(request):
    url = 'https://www.cultura.gob.ar/api/v2.0/organismos/?format=json'  
    response_organismos = requests.get(url)
    data_org = response_organismos.json()


    context = {
        'resultado': data_org
    }

    return render(request, 'organismos.html', context)

def programas(request):
    url = 'https://www.cultura.gob.ar/api/v2.0/programas/?format=json'
    response_programas = requests.get(url)
    data_pro = response_programas.json()

    context = {
        'resultado': data_pro
    }

    return render(request, 'programas.html', context)

def museos(request):
    url = 'https://www.cultura.gob.ar/api/v2.0/museos/?format=json'
    response_museos = requests.get(url)
    data_mus = response_museos.json()

    context = {
        'resultado': data_mus
    }

    return render(request, 'museos.html', context)

def institutos(request):
    url = 'https://www.cultura.gob.ar/api/v2.0/institutos/?format=json'
    response_institutos = requests.get(url)
    data_inst = response_institutos.json()

    context = {
        'resultado': data_inst
    }

    return render(request, 'institutos.html', context)

def tramites(request):
    url = 'https://www.cultura.gob.ar/api/v2.0/tramites/?format=json'
    response_tramites = requests.get(url)
    data_tramites = response_tramites.json()

    context = {
        'resultado': data_tramites
    }

    return render(request, 'tramites.html', context)

def convocatorias(request):
    url = 'https://www.cultura.gob.ar/api/v2.0/convocatorias/?format=json'
    response_convocatorias = requests.get(url)
    data_con = response_convocatorias.json()

    context = {
        'resultado': data_con
    }

    return render(request, 'convocatorias.html', context)
