## Projet Back-end en Python
C'est une application back-end développée en python, qui permet de gérer des users, des plannings ainsi que des entreprises

## Documentation
La documentation est automatiquement disponible sur FQDN:port/docs/ ou /redoc
Le FQDN par défaut est localhost et le port par défaut est 80.

## Run the application
Deux modes possibles pour lancer l'application, celui recommandé est le mode Docker.
Une fois lancée, l'application sera accessible à http://localhost sauf si vous avez changé le port 80 en autre chose.

## Docker mode
requirements: docker and docker-compose installés
Pour le lancer, votre terminal doit être dans le dossier racine de ce répo. Tapez ensuite :
docker-compose up --build

## Mode Uvicorne
exigences : python3.10 ou supérieur installé
Tout d'abord, installez les dépendances
pip install -r requirements.txt
Ensuite, lancez l'application :
uvicorn app.main:app --host 0.0.0.0 --port 80
