# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier


import os

os.chdir(os.path.dirname(__file__))

os.chdir("csvs")

for fichier in os.listdir():
    nom_fichier, ext = os.path.splitext(fichier)
    titre, cours, num = nom_fichier.split()
    titre = titre.strip()
    cours = cours.strip()

    num = num.strip()
    num = num[1:]   # retire le dièse juste avant le numéro de cours
    num = num.zfill(2) # rajoute des 0 avec le numéro de cours pour obtenir un num de 2 caractères

    nouveau_nom = f"{num} {cours} {titre}{ext}"
    os.rename(fichier, nouveau_nom)