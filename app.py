"""import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("graveler")
print(pokemon)"""

import requests

def getPotter(potter):
    response = requests.get(f"https://vlaurencena.github.io/harry-potter-openapi-swagger-ui/#/")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "characters": data["characters"],
        "house": data["house"],
        "spells": data["spells"],
        "types": [t["type"]["characters"] for t in data["types"]]
    }

potter = getPotter("Harry Potter")
print(potter)