import os
os.chdir(os.path.dirname(__file__))

# Q1  imprimez le répertoire courant
print(f"Q1{'_'*60}")
print(os.getcwd())


# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2{'_'*60}")
userprofile = os.environ.get("USERPROFILE")
print(userprofile)


# Q3 Déplacez-vous sur le répertoire 'Documents'
# Et imprimez le répertoire courant
print(f"Q3{'_'*60}")

os.chdir(f"{userprofile}/Documents")

# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'
print(f"Q4{'_'*60}")


print(os.listdir())


# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
print(f"Q5{'_'*60}")

if "OS-ExercQ5" not in os.listdir(): #permet d'éviter les messages d'erreurs si le répertoire existe déja
    os.mkdir("OS-ExercQ5")

print(os.listdir())


# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")

os.makedirs("OS-ExercQ5/Subdir1",exist_ok=True)     # Ce paramètre permet d'éviter les messages d'erreurs si le répertoire existe déja


#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire
print(f"Q6{'_'*60}")


os.rename("OS-ExercQ5/Subdir1","OS-ExercQ5/Sous-repertoire")


# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")

os.removedirs("OS-ExercQ5/Subdir1")




