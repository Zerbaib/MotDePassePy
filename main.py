import json

def addMDP():
    site = input("quelle est le site ?\n")
    mdp = input("quelle est le mot de passe ?\n")
    list[site] = mdp

def seeMDP():
    see = input("quelle mot de passe veux tu lire\n")
    print("Ton mot de passe est:\n" + list.get(see))

def delMDP():
    suppr = input("quelle mot de passe veux tu supprimer\n")
    if list.__contains__(suppr):
        del list[suppr]
        print("mot de passe supprimer")
    else:
        print("le site du mot de passe n'est pas trouver")

def saveMDP():
    with open('listMDP.txt', 'w') as file:
        json.dump(list, file)

with open('listMDP.txt', 'r') as file:
    list = json.load(file)
print("Bienvenue dans mon gestionnaire de mot de passe")

while True:
    saveMDP()
    choix = input("que veux tu faire ?\n1. ajouter un mot de passe\n2. lire un mot de passe\n3. supprimer un mot de passe\n4. quitter le gestionnaire de mdp\n")
    if choix == "1":
        addMDP()

    if choix == "2":
        seeMDP()

    if choix == "3":
        delMDP()

    if choix == "4":
        saveMDP()
        print("Tout a ete sauvegarder vous allez quitter en toute securite")
        exit()