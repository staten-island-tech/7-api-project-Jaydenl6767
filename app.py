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

import tkinter as tk
import requests

def getPotter(potter):
    response = requests.get(f"https://hp-api.onrender.com/api/characters/house/{potter.lower()}")
    if response.status_code != 200:
        print("What type of Harry Potter house is that!?")
        return None
    
    data = response.json()
    for i in data:
        print(i["name"])
        print(i["gender"])
        print(i["species"])
        print(i["actor"])

potter = getPotter("Gryffindor")
print(potter)




 
window = tk.Tk()
window.title("Harry Potter House") 
window.geometry("400x250")
window.resizable(False, False)
prompt = tk.Label(window, text="What is your favorite Harry Potter house?",
font=("Times New Roman", 15))
prompt.pack(pady=10)
entry = tk.Entry(window, font=("Times New Roman", 15), width=30)
entry.pack(pady=5)
result_label = tk.Label(window, text="", font=("Times New Roman", 15, "bold"),
fg="blue")
result_label.pack(pady=15)




def reverse_message():
    text = entry.get() 
    reversed_text = text[::-1]
    result_label.config(text=f"Backwards: {reversed_text}")
reverse_button = tk.Button(window, text="Check Students",
font=("Arial", 15),

command=reverse_message)
reverse_button.pack(pady=10)
window.mainloop()
