list = []
print("Bienvenue dans mon gestionnaire de mot de passe")

while True:
    a = input("que veux tu faire ?\n1. ajouter un mot de passe\n2. lire un mot de passe\n")
    if a == "1":
        list = input("ajoute ton mot de passe au format site:mdp\n")
        print(list)
    if a == "2":
        print("quelle mot de passe veux tu lire")
    