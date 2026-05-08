# Guide de Configuration Django - Radianit

Ce guide détaille les étapes nécessaires pour initialiser un projet Django dans ce répertoire.

## 1. Environnement Virtuel (Déjà fait)
L'environnement virtuel est déjà créé et activé.
```powershell
python -m venv .venv
.venv\Scripts\activate
```

## 2. Installation de Django
Installez la dernière version de Django :
```powershell
pip install django
```

## 3. Création du Projet
Créez le projet Django dans le dossier courant (le `.` à la fin est important pour éviter un sous-dossier supplémentaire) :
```powershell
django-admin startproject config .
```

## 4. Création d'une Application
Créez votre première application (remplacez `app_name` par le nom souhaité) :
```powershell
python manage.py startapp core
```

## 5. Migration Initiale
Appliquez les migrations de base pour configurer la base de données SQLite par défaut :
```powershell
python manage.py migrate
```

## 6. Lancement du Serveur de Développement
Démarrez le serveur pour vérifier que tout fonctionne :
```powershell
python manage.py runserver
```
Accédez ensuite à l'adresse `http://127.0.0.1:8000/`.

---
**Note :** N'oubliez pas d'ajouter les nouvelles applications dans le fichier `config/settings.py` sous la liste `INSTALLED_APPS`.
