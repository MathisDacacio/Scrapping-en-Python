from bs4 import BeautifulSoup
import requests
import pandas as pd

#initialisation des headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
base_url = "https://www.imdb.com"
home_page = requests.get(base_url, headers=headers)
soup = BeautifulSoup(home_page.text, 'html.parser')


def find_actor_page():
    # Recherche la section contenant les acteurs
    actor_section = soup.find_all("a", class_="ipc-title-link-wrapper")
    actor_pages = [a['href'] for a in actor_section if 'href' in a.attrs]
    actor_pages = [base_url + actor_page for actor_page in actor_pages]
    return actor_pages


def find_all_actors_links():
    # Récupère les liens des acteurs
    actor_pages = find_actor_page()
    actors_links = []
    for actor_page in actor_pages:
        actor_page_request = requests.get(actor_page, headers=headers)
        soup_actor_page = BeautifulSoup(actor_page_request.text, 'html.parser')
        film_section = soup_actor_page.find_all("a", class_="ipc-title-link-wrapper")
        for film in film_section:
            actors_links.append(base_url + film['href'])
    return actors_links


def find_all_films_info():
    # Récupère les liens des films
    film_pages = find_all_actors_links()
    films_links = []
    
    for film_page in film_pages:
        try:
            film_page_request = requests.get(film_page, headers=headers)
            soup_film_page = BeautifulSoup(film_page_request.text, 'html.parser')
            
            actor_name_tag = soup_film_page.find("span", class_="hero__primary-text")
            actor_name = actor_name_tag.text.strip() if actor_name_tag else "Unknown Actor"
            
            # Recherche les sections contenant les informations des films
            film_sections = soup_film_page.find_all(
                "li",
                class_="ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click sc-2303066d-3 jLskli"
            )
            
            for section in film_sections:
                # Récupère le titre du film
                film_title_tag = section.find("a", class_="ipc-metadata-list-summary-item__t")
                film_title = film_title_tag.text.strip() if film_title_tag else None
                
                # Récupère l'année du film
                film_year_tag = section.find("span", class_="ipc-metadata-list-summary-item__li")
                film_year = film_year_tag.text.strip() if film_year_tag else None
                
                # Récupère la note
                film_rating_tag = section.find("span", class_="ipc-rating-star--rating")
                film_rating = film_rating_tag.text.strip() if film_rating_tag else None
                
                # Ajoute les informations du film dans la liste sous forme de dictionnaire
                films_links.append({
                    "Actor": actor_name,
                    "Title": film_title,
                    "Year": film_year,
                    "Rating": film_rating
                })
        except Exception as e:
            print(f"Erreur sur la page {film_page} : {e}")
    
    return films_links


def save_to_dataframe():
    film_data = find_all_films_info()
    
    # Convertit les données en DataFrame pandas
    df = pd.DataFrame(film_data)
    
    # Trie les données par acteur
    df = df.sort_values(by=["Actor", "Title"])
    
    print(df)
    
    # Sauvegarde les données dans un fichier CSV
    df.to_csv('DataBase/film_data_sorted_by_actor.csv', index=False)


save_to_dataframe()
