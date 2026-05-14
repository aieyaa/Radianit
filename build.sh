#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Peupler la base de données
echo "Peuplement de la base de données..."
python seed_data.py

# Créer un superutilisateur
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    echo "Tentative de création du superutilisateur ($DJANGO_SUPERUSER_USERNAME)..."
    python manage.py createsuperuser --no-input || echo "Le superutilisateur existe déjà ou une erreur est survenue."
fi