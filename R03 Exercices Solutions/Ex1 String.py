#Q1
#  Voici une chaine de caractères qui ressemble à une ligne de données que vous auriez extraite d'un fichier text
ligne_donnees = " AMD Ryzen 9 5900X ;  AMD Ryzen 7 5800X3 ;  Intel Core i9 12900 K    " 
#  Vous devez dans un premier temps séparer les données sur le caractère qui les séparent ( le ';' ici ) avec la méthode .split
#  Vous voulez ensuite avoir nouvelle une liste contennant chacun des processeurs MAIS sans les espaces avant et après chaque processeur
#  Imprimez cette nouvelle liste
print(f"Q1{'_'*60}")

processeurs = ligne_donnees.split(';')
processeurs_clean = []

for process in processeurs :
    process_clean = process.strip()
    processeurs_clean.append(process_clean)

print(processeurs_clean)




# Q2
# Voici un nom de fichier dont chaque partie est séparée par un _
nom_fichier_et_extension = "Python_Rencontre 3_Approfondissement str.docx"
# Séparez nom_fichier_et_extension sur le '.' et gardez les parties dans des sous-chaines séparées
# Séparez le nom de fichier de façon à récupérer le nom du cours, la rencontre et le sujet de la rencontre
# Imprimez le nom du cours, la rencontre et le sujet de la rencontre 
print(f"Q2{'_'*60}")

nom_fichier, ext = nom_fichier_et_extension.split('.')
nom_cours, rencontre, sujet = nom_fichier.split('_')

print(f"Cours : {nom_cours}\n   {rencontre}\n   {sujet}")






#Q3
# Remplir un string pour qu'il fasse 2 caractères de long avec .zfill()
# Au départ, vous avez une chaine qui contient des nombres
str_nombres = "1,5,10,15,20,25"
# transformez cette chaine en une liste de str mettez la en ordre avec .sort()
# Imprimez la liste. Qu'est-ce qui est étonnant? (Cela devrait vous donnez ['1', '10', '15', '20', '25', '5'] )

# Pour pouvoir avoir la liste de string dans un ordre croissant numérique il faut remplacer les valeurs pour qu'ils soient tous 2 charactères de long
# faites une boucle sur les valeurs de la liste et utilisez la méthode zfill()
print(f"Q3{'_'*60}")

nombres_separer = str_nombres.split(',')
nombres_separer.sort()
print(nombres_separer)

new_nombres = []
for nombre in nombres_separer:
    new_nombre = nombre.zfill(2)
    new_nombres.append(new_nombre)

new_nombres.sort()
print(new_nombres)
print("\n")