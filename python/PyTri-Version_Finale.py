# -*- coding: utf-8 -*-
####Projet algorithme de tri###
import os, shutil, glob, extliste, platform
from extliste import *  #J'importe pour ensuite avoir mes listes

#Un truc stylé ;p
print("""Bienvenue sur Pytrie le nouveau programme de Tri entierement basé sur Python !
Ce programme vous permet de trier vos fichiers en vrac dans un dossiers gràce à seulement quelques clics !
Let's play ! """)
print("")
print("                 ## Vous êtes actuellement sous "+platform.system()+" "+platform.release()+ " ## " )

##### ETAPE 1 : INITIALISATION DES VARIABLES + DEFINITION DES CHEMINS #####

path="C:/Projet/BAC/test"
path2="C:/Projet/BAC/python"
os.chdir(path)   #Aller dans le path entré precedement
print("")
print("Dossier Actuel: "+os.getcwd())
p=0
mp="/Musiques"
ip="/Images"
vp="/Videos"
dp="/Documents"

##### ETAPE 2 : PRISE D'INFORMATION AUPRES DE L'UTILISATEUR #####

def pytrie (p,path,path2):    #Je definie la fonction avec toute les variable qui sont dedans (Crée une fonction va me permettre de relancer le programme en cas d'erreur)
    os.chdir(path2)
    global option1  #On définit la variable dans tout le programme et pas seulement dans la fonction locale
    option1=str(input("""Choisissez parmis les options suivantes:

    [1] - Trier par normal type (Musiques, Documents, Images, Vidéos)
    [2] - Trier par le format de votre choix
    [3] - Trier par type avec choix (Musiques ou Documents ou Images ou Vidéos)
    
    Saisissez 1 ou 2 ou 3: """))
   

   
##### ETAPE 2.2 : TRAITEMENT DES INFORMATIONS DEBUT DU TRI ######

    if option1=="1":     #En fontion de ce que l'utilisateur a tapé (J'ai mis les guillement vu que ce que rentre l'utilisateur c'est une chaine de caractère
        print("")
        print("Vous avez choisi l'option de tri 1")     
        while os.access("Musiques"+str(p) or "Documents"+str(p) or "Images"+str(p) or "Videos"+str(p), os.F_OK):
            p=p+1

        if os.access("Musiques"+str(p) or "Documents"+str(p) or "Images"+str(p) or "Videos"+str(p), os.F_OK) or os.access("Musiques" or "Documents" or "Images" or "Videos", os.F_OK):
            folder=str(input("D'anciens dossiers ont été detectés, en créer de nouveaux ? (O/N) :"))

            if folder == "o" or folder == "O":
                global mp,vp,ip,dp
                os.mkdir("Musiques"+str(p)) 
                os.mkdir("Images"+str(p))
                os.mkdir("Videos"+str(p))
                os.mkdir("Documents"+str(p))
                mp="/Musiques"+str(p)
                ip="/Images"+str(p)
                vp="/Videos"+str(p)
                dp="/Documents"+str(p)
            else:
                p1=p-1
                mp="/Musiques"+str(p1)
                ip="/Images"+str(p1)
                vp="/Videos"+str(p1)
                dp="/Documents"+str(p1)
                
        else:
            os.mkdir("Musiques") 
            os.mkdir("Images")
            os.mkdir("Videos")
            os.mkdir("Documents")
        
##### ETAPE 2.3 : TRAITEMENT DES INFORMATIONS DEBUT DU TRI ######            

    elif option1=="2":
        print("Vous avez choisi l'option de tri 2")
        info=(str(input("""
        Quel format de fichier voulez vous rassembler ? (ex : mp3 , png , mpeg..etc)

        (NB : Merci de les séparer des espaces si il y en a plusieurs)

        """)))

        global extdossier #La fonction global veut juste dire que la variable va etre appliquer et valable dans tout le programme !
        extdossier=info.split(" ") #On range dans une liste chaque format qu'a entrer l'utilisateur. En gros: Utilisateur tape > mp3 flac  se qui donne > extendossier=['mp3', 'flac']

##### ETAPE 2.4 : TRAITEMENT DES INFORMATIONS DEBUT DU TRI ######

    elif option1=="3":
        print("Vous avez choisi l'option de tri 3")
        def suppr():
            global option2
            option2=str(input("""Quel type ?

            [1] - Documents
            [2] - Musiques
            [3] - Images
            [4] - Videos

            """))

            if option2=="1":
                if not os.access("Documents" ,os.F_OK):          
                    os.mkdir("Documents")    

            elif option2=="2":
                if not os.access("Musiques" ,os.F_OK):
                    os.mkdir("Musiques")

            elif option2=="3":
                if not os.access("Images" ,os.F_OK):
                    os.mkdir("Images")

            elif option2=="4":
                if not os.access("Videos" ,os.F_OK):
                    os.mkdir("Videos")

            else:
                print("""

        Merci de saisir une valeur correcte

        """)
        suppr() 
                    
    else:   
        print("""

        Merci de saisir une valeur correcte

        """)
        pytrie(p,path,path2)    #Si l'utilisateur à taper autre chose que 1,2 ou 3 > 2 il va afficher qu'il y a une erreur et il relance la fonction
       
pytrie(p,path,path2) #On execute la fonction



os.chdir(path)

##### ETAPE 3 : TRIAGE DES FICHIERS (MODULE GLOB)

#Fonction pour deplacer "zerop" va etre remplacer par le deuxième terme mis dans la fonction. Par exemple pour musique on a move(ext,mp) >zerop va etre remplacer par mp          

def move(ext,zerop):
    for dirpath, dirnames, files in os.walk(path):   #On parcours avec plusieurs éléments l'arborescence des fichiers donné par os.walk
        for name in files:                           #On parcours l'élément files qui a lui meme parcouru os.walk
            if name.lower().endswith(ext):			 #Si la fin de l'élément élément relever se termine par l'extension contenu dans la liste correspondant au format du fichier
                shutil.copy2(os.path.join(dirpath, name), path2+zerop)  #On copy l'élément relever (os.path.join est pour lier le fichier relever à son chemin)
                print("Déplacement en cours... "+name)


#### TRI POUR L'OPTION 1 (tri global) ####
 
if option1=="1":
    confirm=str(input("Vos fichier vont être déplacés. Voulez-vous continuer ?(O/N) :"))
    
    if confirm=="O" or confirm=="o":

        for ext in mpliste:  #On va parcourir les formats mis dans la liste que est dans le fichier extliste.py
            move(ext,mp)

        for ext in ipliste:
            move(ext,ip)

        for ext in vpliste:
            move(ext,vp)

        for ext in dpliste:
            move(ext,dp)
            
        print("""
        ** Le déplacement des fichiers a été realisés avec succés.
           Merci de votre confiance.** """)
        

    else:
        print("Annulation en cours...")
        print("Fin du programme, Veuillez quitter l'IDLE.")
        exit
    

#### TRI POUR L'OPTION 2 (tri par extension) ####
        
elif option1=="2":
    confirm=str(input("Vos fichier vont être déplacés. Voulez-vous continuer ? (O/N): "))

    if confirm=="O" or confirm=="o":

        for g in extdossier:  #extdossier c'est la variable qu'on a crée précédemment pour avoir la liste mais sans mes *. devant les éléments

            if not os.access(path2+"/"+g ,os.F_OK):# On crée les dossiers si il ne sont pas déjà présents
                os.mkdir(path2+"/"+g)   
            move(g,"/"+g)

            print("""
        ** Le déplacement des fichiers a été realisés avec succés.
           Merci de votre confiance.** """)
    else:
        print("Annulation en cours...")
        print("Fin du programme, Veuillez quitter l'IDLE.")
    
#### TRI POUR L'OPTION 3 (tri par type de fichier) ####
                        
elif option1=="3":
    confirm=str(input("Vos fichier vont être déplacés. Voulez-vous continuer ?(O/N): "))#Ya rien de compliquer a comprendre si tu as compris le reste

    if confirm=="O" or confirm=="o":

        if option2=="1":
            for ext in dpliste:
                move(ext,dp)
                
        elif option2=="2": 
            for ext in mpliste:
                move(ext,mp)

        elif option2=="3":
            for ext in ipliste:
                move(ext,ip)

        elif option2=="4":
            for ext in vpliste:
                move(ext,vp)

        print("""
        ** Le déplacement des fichiers a été realisés avec succés.
           Merci de votre confiance.** """)

    
    else:
        print("Annulation en cours...")
        print("Fin du programme, Veuillez quitter l'IDLE.")
        
    
