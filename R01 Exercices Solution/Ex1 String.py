# RAPPEL
# groupe = "1020"    
# print(dir(groupe))  #montre toutes les méthodes disponibles pour la variable groupe#
# #help#
# print(help(str)) #montre ce que fait chacune des méthodes de la classe str#
# print(help(str.find)) #montre ce que fait la méthode find de la classe str# 



# Q1 Créez 3 amies (amie1, amie2, amie3) et donnez leur des prénoms différents #
amie1 = 'Sophie'
amie2 = 'Laurence'
amie3 = 'Wissale'


# Q2 Pour l'amie1, affichez dans la console les 3 premières lettres de son prénom #
print(f"\nQ2{'_'*60}")
print(amie1[0:3])

# Q3 Pour l'amie2, affichez dans la console le nombre de lettres qu'il y a dans son nom #
print(f"\nQ3{'_'*60}")
print(len(amie2))




# Q4 Affichez dans la console la dernière lettre du prénom de votre troisième amie' #
print(f"\nQ4{'_'*60}")
print(amie3[-1])

# Q4 Créez une variable appelée salutation avec la valeur 'Bonne année'  #
salutation = 'Bonne année'



# Q5 Affichez dans la console un message pour souhaiter 'Bonne année' à vos trois amies.
#       Vous devez utilisé un f'string (un string formaté)
#       Vous devez utilisé les variables salutation, amie1, amie2, et amie3
print(f"\nQ5{'_'*60}")
message1 = f'{salutation} {amie1}, {amie2} et {amie3}!'
print(message1)







