MySQL-Python-CRUD-Example

Description

Ce projet démontre l'utilisation du connecteur MySQL en Python pour effectuer des opérations CRUD (Create, Read, Update, Delete) sur une base de données. Le script Python inclut des fonctions pour créer une table, insérer des données, sélectionner et afficher des données, mettre à jour des données, supprimer des données, et rechercher des données par mot-clé.

Prérequis
Python 3.11
Bibliothèque MySQL pour Python (mysql-connector-python-rf) 2.2.9

Installation

Accédez au répertoire du projet : cd MySQL-Python-CRUD-Example
Installez les dépendances : pip install -r requirements.txt
Configuration

Assurez-vous de configurer les informations de connexion à la base de données dans le script (main.py). Modifiez les variables user, password, host, et database selon votre configuration.

# Exemple de configuration de connexion dans main.py

user = 'votre_nom_utilisateur'
password = 'votre_mot_de_passe'
host = 'localhost'
database = 'votre_base_de_donnees'

Utilisation

Exécutez le script main.py : python main.py
Suivez les instructions pour voir les résultats des opérations CRUD.

Fonctionnalités

Création de la table 'employee' si elle n'existe pas déjà.
Insertion d'exemples de données dans la table 'employee'.
Sélection et affichage de toutes les données de la table 'employee'.
Mise à jour des données dans la table 'employee'.
Suppression d'une entrée de la table 'employee'.
Recherche de données par mot-clé dans la table 'employee'.

Auteur

Bienvenu MAMPOUYA, Olivier POLYNICE & Hassad Kevin AKEDJOU
