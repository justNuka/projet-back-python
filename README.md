## Projet Back-end en Python
C'est une application back-end développée en python, qui permet de gérer des users, des activités ainsi que des entreprises.
Un système de vérification y est implémenté : 
  - Si un user qui n'a pas le rôle de "maintainer" tente de RUD des autres users, une erreur lui sera renvoyée.
  - Si un maintainer d'une entreprise différente de celle à laquelle il appartient tente de modifier une activité, un user, ou même des infos de l'entreprise, une erreur lui sera renvoyée.

## Run the application
Utilisation de Docker.
Une fois lancée, l'application sera accessible à http://localhost:8080/docs.

## Docker mode
Pour pouvoir exécuter l'application, il faut dans un premier temps installer toutes les dépendances nécessaires : 
  - Avoir installé Docker (Docker Desktop conseillé) et docker-compose installés
  - Avoir installé pip pour permettre l'installation des dépendances
  - Posséder un serveur Sql (Xampp, simple d'utilisation et pratique). Une fois installé, le lancer, puis aller à l'adresse suivante : http://localhost/phpmyadmin/index.php. Une fois ceci fait, créer une nouvelle base de données, la renommer en `projet-back-python`. Dès que cela est fait, allez dans importer, puis selectionnez le fichier `projet-back-python.sql`, et cliquez sur exécuter. La base de données est maintenant créée et opérationnelle sur votre poste.
  - Installer les requirements : 
        - `pip install requirements.txt`
Une fois que tout cela est fait, pour lancer l'application, votre terminal doit être dans le dossier racine de ce répo. Tapez ensuite :
`docker-compose up --build`
