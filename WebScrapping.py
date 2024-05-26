import requests
from bs4 import BeautifulSoup

def get_filmography(actor_name):
    #Wikipedia URL
    url = f"https://en.wikipedia.org/wiki/{actor_name}"
    
    # GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    beautifulSoup = BeautifulSoup(response.content, "html.parser")
    
    # filmography section
    filmographySection = beautifulSoup.find("span", {"id": "Filmography"})
    if not filmographySection:
        return [0]
    
    # the table containing the filmography
    filmographyTable = filmographySection.find_next("table")
    if not filmographyTable:
        return [0]
    
    # film titles from the table
    films = []
    for row in filmographyTable.find_all("tr")[1:]:
        cells = row.find_all("td")
        if cells:
            film_title = cells[0].get_text().strip()
            films.append(film_title)
    
    # list of filmography in descending order
    films.reverse()
    
    return films

actor_name = input("Enter the name of the actor: ")
filmography = get_filmography(actor_name)

print(f"Filmography of {actor_name}:")
for film in filmography:
    print(film)