list = {}
print("Bienvenue dans mon gestionnaire de mot de passe")



while True:
    choix = input("que veux tu faire ?\n1. ajouter un mot de passe\n2. lire un mot de passe\n")
    if choix == "1":
        site = input("quelle est le site ?\n")
        mdp = input("quelle est le mot de passe ?\n")
        list[site] = mdp
        
    if choix == "2":
        see = input("quelle mot de passe veux tu lire\n")
        print("Ton mot de passe est:\n" + list.get(see))