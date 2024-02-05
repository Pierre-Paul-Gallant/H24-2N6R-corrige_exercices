import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv

import csv

# Dans le fichier "Ex5 Stages.csv", vous avez une liste de stages en programmation et en TI
# Vous voulez extraire les stages de TI et les mettres dans un nouveau fichier spécifique aux stages de TI

 

# Regardez le contenu du fichier "Ex5 Stages.csv"
# 
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                  Compagnie|Ville|Voie de sortie
#          La valeur de la Voie de sortie est soit 'Prog', soit 'TI'
#          
#          Il vous faudra créer un autre fichier appelé "Ex5 Stages TI.csv" dans lequel vous écrirez les stages en TI seulement
# 
#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas


ficher_a_lire = os.path.join("csvs", "Ex5 Stages.csv")

# SOLUTION 1 - En un bloc imbriqué
with open("csvs/Ex5_stages_TI_uniquement.csv", "w",encoding="utf-8") as fichier_TI :
    csv_writer = csv.writer(fichier_TI, delimiter='|', lineterminator='\n')

    with open(ficher_a_lire,"r",encoding="utf-8") as fichier_stages:
        csv_reader = csv.reader(fichier_stages,delimiter='|')
        en_tete = next(csv_reader)
        csv_writer.writerow(en_tete)
        for stage in csv_reader:
            if stage[-1] == 'TI' :
                csv_writer.writerow(stage)


# SOLUTION 2 - Deux blocs. Plus facile à lire mais ne pourrait pas traiter des csv de 100 000 lignes et plus.
stage_TI = []

with open(ficher_a_lire,"r",encoding="utf-8") as fichier_stages:
        csv_reader = csv.reader(fichier_stages,delimiter='|')
        en_tete = next(csv_reader)
        for stage in csv_reader:
            if stage[-1] == 'TI' :
                stage_TI.append(stage)

with open("csvs/Ex5_stages_TI_uniquement.csv", "w",encoding="utf-8") as fichier_TI :
    csv_writer = csv.writer(fichier_TI, delimiter='|', lineterminator='\n')
    csv_writer.writerow(en_tete)
    for stage in stage_TI :
         csv_writer.writerow(stage)


# SOLUTION 3 - Avec fonctions, facilement lisible et capable de traiter des fichiers de n'importe quel taille.

def initier_csv(fichier:str,en_tete:list):
    with open(fichier, "w",encoding="utf8") as fichier_csv :
         csv_writer = csv.writer(fichier_csv,delimiter="|",lineterminator="\n")
         csv_writer.writerow(en_tete)

def ajouter_stage(fichier:str,stage:list):
    with open(fichier, "a",encoding="utf8") as fichier_csv :
         csv_writer = csv.writer(fichier_csv,delimiter="|",lineterminator="\n")
         csv_writer.writerow(stage)

fichier_a_ecrire = "csvs/Ex5_stages_TI_uniquement.csv"

with open(ficher_a_lire,"r",encoding="utf-8") as fichier_stages:
        csv_reader = csv.reader(fichier_stages,delimiter='|')
        en_tete = next(csv_reader)
        initier_csv(fichier_a_ecrire,en_tete)
        for stage in csv_reader:
            if stage[-1] == 'TI' :
                ajouter_stage(fichier_a_ecrire,stage)










# INSTRUCTIONS DÉTAILLÉES
# Ouvrez en lecture le fichier "Ex5 Stages.csv", en utilisant l'encoding utf-8   
    # Crée un csv.reader() avec le delimiter='|'  

    # Ouvrez en écriture le fichier "Ex5 Stages TI.csv" , en utilisant l'encoding utf-8
        # Créez un csv.writer avec l'encoding utf-8 et le delimiter '\n'

        # Écrivez dans le fichier Ex5 Stages TI.csv les entêtes du premier fichier ( avec writerow() et next())  

        # Dans votre boucle qui passera à travers les lignes du fichier de stages
        #      Faites un test pour voir si la valeur de la voie de sortie est TI
        #      Si oui, écrivez cette ligne dans le fichier des stages en TI.



