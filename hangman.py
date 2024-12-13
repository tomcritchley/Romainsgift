import sys

# Codes de couleur ANSI
ROUGE = "\033[31m"
VERT = "\033[32m"
JAUNE = "\033[33m"
BLEU = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

mot_secret = "salon"
lettres_devinees = []
tentatives_restantes = 8

def afficher_mot():
    affichage = ""
    for lettre in mot_secret:
        if lettre in lettres_devinees:
            affichage += VERT + lettre + RESET + " "
        else:
            affichage += "_ "
    return affichage.strip()

print(BLEU + "Bienvenue au jeu du Pendu !" + RESET)
print("Le mot secret contient", len(mot_secret), "lettres.")
print("Vous avez", tentatives_restantes, "tentatives pour deviner le mot correctement.\n")

while tentatives_restantes > 0:
    print("Mot :", afficher_mot())
    guess = input(JAUNE + "Devinez une lettre : " + RESET).lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print(ROUGE + "Veuillez deviner une seule lettre !" + RESET)
        continue

    if guess in lettres_devinees:
        print(CYAN + "Vous avez déjà deviné cette lettre. Essayez-en une autre." + RESET)
        continue

    lettres_devinees.append(guess)

    if guess in mot_secret:
        print(VERT + "Bonne pioche !" + RESET)
    else:
        tentatives_restantes -= 1
        print(ROUGE + "Mauvaise pioche !" + RESET, "Tentatives restantes :", tentatives_restantes)

    # Vérifier si toutes les lettres ont été devinées
    if all(lettre in lettres_devinees for lettre in mot_secret):
        print("\n" + VERT + "Félicitations ! Vous avez deviné le mot :" + RESET, afficher_mot())
        print(VERT + "Maintenant, retourne au fichier puzzle.py pour découvrir ta surprise !" + RESET)
        sys.exit(0)

if tentatives_restantes == 0:
    print("\n" + ROUGE + "Vous n'avez plus de tentatives !" + RESET)
    print("Le mot secret était :", mot_secret)
