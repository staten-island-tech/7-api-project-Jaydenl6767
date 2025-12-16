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
    response = requests.get(f"https://hp-api.onrender.com/api/characters/house/{potter.lower()}")
    if response.status_code != 200:
        print("What type of Harry Potter house is that!?")
        return None
    
    data = response.json()
    for i in data:
        print(i["name"])

potter = getPotter("Gryffindor")
print(potter)






