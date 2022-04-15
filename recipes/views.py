from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', {"name": "Matheus"})


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', {'name': 'Matheus'})
