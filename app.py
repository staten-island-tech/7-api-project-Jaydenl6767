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
        print(i["gender"])
        print(i["species"])
        print(i["actor"])

potter = getPotter("Gryffindor")
print(potter)

input = ("What is your favorite Harry Potter character of this house?")

import tkinter as tk 
window = tk.Tk()
window.title("Message Reverser") 
window.geometry("400x250")
window.resizable(False, False)
prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10)
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)




def reverse_message():
    text = entry.get() 
    reversed_text = text[::-1]
    result_label.config(text=f"Backwards: {reversed_text}")
reverse_button = tk.Button(window, text="Reverse Message!",
font=("Arial", 14),

command=reverse_message)
reverse_button.pack(pady=10)
window.mainloop()
