# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 


# Q1                                                                                                                   #
# Créez une liste de 3 barrettes de RAM parmis les suivantes:                                                          #
#          G.SKILL Trident Z5, CORSAIR Dominator, CORSAIR Vengeance, G.SKILL Ripjaws V, G.SKILL Ripjaws X              #
# imprimez la liste                                                                                                    #
print(f"Q1{'_'*60}")
barrettes = ["G.SKILL Trident Z5", "CORSAIR Dominator", "G.SKILL Ripjaws V"]
print(f"Voici la liste : {barrettes}")





# Q2                                                                                                                   #
# Ajoutez un item à la fin de la liste avec append                                                                     #
# et affichez la dernière barrette RAM que vous avez dans la liste                                                     #
print(f"Q2{'_'*60}")
barrettes.append("CORSAIR Vengeance")
print(f'La barrette "{barrettes[-1]}" a été ajouté.')






#  Q3                                                                                                               #
#  Observez quelle est la deuxième barrette de RAM de votre liste                                                   #
#  Enlevez-la de la liste avec remove                                                                               #
#  Imprimez la liste en spécifiant la barrette de RAM enlevée                                                       #
print(f"Q3{'_'*60}")
print(f"La deuxième barrete est {barrettes[1]}.")
barrettes.remove("CORSAIR Dominator")
print(f"Elle a été retiré. La liste est maintenant : {barrettes}")





# Q4                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
print(f"Q4{'_'*60}")
barrettes.sort()
print(f"La liste en ordre alphabétique est : {barrettes}")





# Q5                                                                                                             #
# Crée une nouvelle liste en ordre décroissant avec la fonction sorted (qui prend la liste originel en paramètre)                    #
# et imprimez-la                                                                                                 
print(f"Q5{'_'*60}")
new_barrettes = sorted(barrettes,reverse=True)
print(f'Nouvelle liste en ordre alphabétique inversé : {new_barrettes}')




# Q6                                                                                                                 #
# Imprimez le nombre d'éléments qu'il y a dans votre liste présentement                                              #
print(f"Q6{u'_'*60}")
print(f"il y a {len(barrettes)} barrettes")





# Q7                                                                                                                 #
# Imprimez une sous-liste des deux dernières barrettes RAMS de votre liste, en utilisant le slicing                  #
print(f"Q7{u'_'*60}")
print(f"Les deux dernières sont : {barrettes[-2:]}")





