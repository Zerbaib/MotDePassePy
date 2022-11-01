import json

def addMDP():
    site = input("quelle est le site ?\n")
    mdp = input("quelle est le mot de passe ?\n")
    list[site] = mdp
    with open('listMDP.txt', 'w') as file:
        list = json.load(list, file)
    print("Mot de passe sauvegarder")

def seeMDP():
    see = input("quelle mot de passe veux tu lire\n")
    print("Ton mot de passe est:\n" + list.get(see))


list = {}
print("Bienvenue dans mon gestionnaire de mot de passe")

while True:
    choix = input("que veux tu faire ?\n1. ajouter un mot de passe\n2. lire un mot de passe\n")
    if choix == "1":
        addMDP()

    if choix == "2":
        seeMDP()

    if choix == "3":
        with open('listMDP.txt', 'w') as file:
            list = json.load(list, file)
        print("Mot de passe sauvegarder")