from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def counter(request):
    # On récupère le texte envoyé par le formulaire
    text = request.POST['text']
    # On compte le nombre de mots
    amount_of_words = len(text.split())
    # On renvoie le résultat à une nouvelle page
    return render(request, 'counter.html', {'amount': amount_of_words})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Fonction d'inscription
def register(request):
    if request.method == 'POST':
        user = request.POST['username']
        # ... récupération des autres champs ...
        if User.objects.filter(username=user).exists():
            messages.info(request, "L'utilisateur existe déjà")
            return redirect('register')
        else:
            # Création de l'utilisateur
            new_user = User.objects.create_user(username=user, password=request.POST['password'], email=request.POST['email'])
            new_user.save()
            return redirect('login')
    return render(request, 'register.html')

# Fonction de connexion
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Identifiants invalides")
            return redirect('login')
    return render(request, 'login.html')
