## Projet Back-end en Python
C'est une application back-end développée en python, qui permet de gérer des users, des activités ainsi que des entreprises.
Un swagger regroupant tous les endpoints implémentés est disponible à l'adresse : http://localhost:8080/docs une fois que toutes les étapes d'installation seront effectuées
Un système de vérification y est implémenté : 
  - Si un user qui n'a pas le rôle de "maintainer" tente de RUD des autres users, une erreur lui sera renvoyée.
  - Si un maintainer d'une entreprise différente de celle à laquelle il appartient tente de modifier une activité, un user, ou même des infos de l'entreprise, une erreur lui sera renvoyée.
Pour pouvoir utiliser cette application, commencez par cloner le répo git, puis suivez les instructions ci-dessous.

## Architecture du projet 
À la racine du projet, on trouve :
  - Les fichiers `.gitignore`, `Dockerfile`, `docker-compose.yml`, `README.md`, `projet-back-python.sql` et `requirements.txt`.
  - Le dossier app contenant tout le code.

Dans le dossier app on retouve plusieurs dossiers et un fichier :
  - auth : contient le fichier auth qui permet l'authentification (login).
  - config : contient le fichier `db.py` qui permet la connexion à la bdd.
  - models : contient 3 fichiers (user, activite, entreprise) qui définissent les classes.
  - routers : contient 3 fichiers (user, activite, entreprise) qui définissent les endpoints de l'application.
  - tables : contient 3 fichiers (users, activites, entreprises) qui définissent les tables de la bdd.
  - fichier `main.py` qui contient `app = FastAPI()` (permet d'initialiser l'application) ainsi que les réponses personnalisées et les différents tags

## Installation / Setup
Utilisation de Docker (voir ci-dessous pour de plus ample informations)
Pour pouvoir exécuter l'application, il faut dans un premier temps installer toutes les dépendances nécessaires : 
  - Avoir installé Docker (Docker Desktop conseillé) ou uvicorn de python.
  - Avoir installé python et pip pour permettre l'installation des dépendances.
  - Posséder un serveur Sql (Xampp, simple d'utilisation et pratique). Une fois installé, le lancer, puis aller à l'adresse suivante : http://localhost/phpmyadmin/index.php. Une fois ceci fait, créer une nouvelle base de données, la renommer en `projet-back-python`. Dès que cela est fait, allez dans importer, puis selectionnez le fichier `projet-back-python.sql`, et cliquez sur exécuter. La base de données est maintenant créée et opérationnelle sur votre poste.
  - Installer les requirements : `pip install -r requirements.txt`

## Run with Docker
`docker-compose up --build `

## Run with Uvicorn (python)
`uvicorn main:app --reload `

## Run the application
Une fois toutes les étapes du dessus effectuées, et l'application lancée, elle sera accessible à l'adresse : http://localhost:8080/docs. 

## Authentification
N'oubliez pas de vous authentifier pour pouvoir accéder aux différentes fonctionnalités de l'app.
Vous pourrez alors tester les différents endpoints implémentés.