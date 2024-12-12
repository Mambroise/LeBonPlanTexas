#!/bin/bash

# Récupère le nom de la branche actuelle
commit_branch=$(git symbolic-ref --short HEAD)

# Demande un message de commit à l'utilisateur
read -p "Entrez un message de commit : " commit_message

# Ajoute tous les fichiers modifiés à l'index
git add -A

# Effectue le commit avec le message spécifié
git commit -m "$commit_message"

# Pousse les modifications vers le dépôt distant
git push origin "$commit_branch"