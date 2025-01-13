# Projet : Scraping de données IMDb

## Table des Matières

- [Description du projet](#description-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Limitations](#limitations)
- [Contact](#contact)

## Description du projet

Ce projet est un script Python qui effectue le scraping de données sur IMDb. Il récupère les informations des films et des acteurs depuis le site IMDb, les traite et les sauvegarde dans un fichier CSV. Il utilise les bibliothèques **BeautifulSoup** pour l'extraction des données HTML et **pandas** pour la gestion des données.

L'objectif principal est de créer une base de données structurée des films et acteurs, incluant des informations telles que le titre, l'année, la note et le nom des acteurs.

## Fonctionnalités

- **Extraction des données IMDb** : 
  - Récupère les pages d'acteurs et de films.
  - Analyse les informations des films (titre, année, note) et les associe à l'acteur.
- **Traitement des données** : Les informations sont stockées dans un DataFrame pandas pour un tri et une organisation faciles.
- **Export des données** : Les données sont sauvegardées dans un fichier CSV, triées par acteur et titre.

## Prérequis

- **Python** (version 3.7 ou supérieure)
- Bibliothèques Python nécessaires :
  - `beautifulsoup4`
  - `requests`
  - `pandas`

## Installation

1. Clonez le projet ou téléchargez le fichier Python :
    ```bash
    git clone https://github.com/votre-repo/scraping-imdb.git
    cd scraping-imdb
    ```
2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
3. Créez un répertoire pour stocker les données exportées :
    ```bash
    mkdir DataBase
    ```

## Utilisation

1. Exécutez le script pour lancer le scraping :
    ```bash
    python scraping_imdb.py
    ```
2. Une fois le script terminé, les données seront sauvegardées dans le fichier CSV :
    ```
    DataBase/film_data_sorted_by_actor.csv
    ```
3. Ouvrez le fichier CSV pour consulter les informations collectées.

## Limitations

- **Accès limité** : Le site IMDb peut restreindre les requêtes fréquentes, pensez à limiter la fréquence des requêtes pour éviter d'être bloqué.
- **Modifications du site IMDb** : Si IMDb modifie sa structure HTML, certaines parties du script devront être adaptées.
- **Données incomplètes** : Si certaines informations (comme l'année ou la note) ne sont pas disponibles, elles apparaîtront comme `None` dans les résultats.

## Contact

Créé par **Mathis Dacacio**.  
[Mon LinkedIn](https://www.linkedin.com/in/mathis-dacacio-298a25293/)  
Pour toute question, merci de me contacter via le formulaire de la page ou directement sur LinkedIn.
