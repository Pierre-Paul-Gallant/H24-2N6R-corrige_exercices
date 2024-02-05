# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 

# Q1                                                                                                                   #
# Créez une liste de 3 modèles de cartes graphiques. Voici une liste de cartes graphiques. Vous pouvez construire votre liste en choisissant parmi les suivantes:
#          GeForce RTX 3090Ti, GeForce RTX 3080Ti, GeForce RTX 3070Ti, Radeon RX 6950 XT, Radeon RX 6900 XT, Radeon RX 6800 XT             
# Vous pouvez aussi mettre un autre modèle de carte graphique si vous voulez.#
# imprimez la liste                                                                                                    #
print(f"Q1{u'_'*60}")
cartes = ["GeForce RTX 3080Ti", "Radeon RX 6900 XT", "GeForce RTX 3090Ti"]
print(f"Voici la liste : {cartes}")



#Q2                                                                                                                   #
#  Obtenez la carte graphique à l'index 1 de la liste de vos cartes graphiques                                        #
#  Enlevez-la de la liste                                                                                             #
#  Imprimez la liste en spécifiant l'item enlevé                                                                      #
print(f"Q2{u'_'*60}")
carte_retirer = cartes.pop(1)
print(f'La carte "{carte_retirer}" a été retiré. Voici la liste : {cartes}')





# Q3                                                                                                                   #
# Ajoutez un nouvel item à la fin de la liste                                                                          #
# et affichez la dernière carte graphique que vous avez maintenant dans la liste                                       #
print(f"Q3{u'_'*60}")
cartes.append("Radeon RX 6800")
print(f"La nouvelle carte en fin de liste est : {cartes[-1]}")





#  

# Q4                                                                                                                 #
# Inversez les items de votre liste                                                                                  #
print(f"Q4{u'_'*60}")
cartes.reverse()
print(f"La liste inversé : {cartes}")



# Q5                                                                                                                 #
# Créez une petite liste de deux nouvelles cartes graphiques                                                         #
# Imprimez cette nouvelle petite liste                                                                               #
# Ajoutez cette nouvelle petite liste à la fin de votre première liste                                               #
# Imprimez votre liste initale telle qu'elle est rendue                                                              #
print(f"Q5{u'_'*60}")
cartes_add = ["Radeon M470X", "Nvidia Kepler"]
print(f"Nouvelle liste : {cartes_add}")
cartes.extend(cartes_add)
print(f"Les deux listes fusionnées : {cartes}")




# Q6                                                                                                                  #
# Ordonnez la liste en ordre croissant de façon à créer une nouvelle liste                                            #
# et imprimez cette nouvelle liste                                                                                    #
print(f"Q6{u'_'*60}")
cartes_en_ordre = sorted(cartes)
print(f"Les cartes en ordre : {cartes_en_ordre}")





