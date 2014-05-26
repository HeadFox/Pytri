####Projet algorithme de tri###
import os, shutil, glob, extliste, platform
from extliste import *  #J'importe pour ensuite avoir mes listes
#Modifier par Lucien

#Un truc stylé ;p
print("Bienvenue sur Pytrie le nouveau programme de Tri entiérement basée sur Python !")
print("")
print("Vous etes actuellement sous "+platform.system()+" "+platform.release())

if platform.system()=='Windows':   #C'est juste parceque les chemins de dossier sont pas écrit pareil sur les systéme Unix 'Linux et Mac' et sur Windows donc en fonction du systéme détecter bah le slash va etre différent
    slash="\\"
else:
    slash="/"
#Fin de modifier par Lucien
###Pour le test
path="C:/Projet/BAC/test"
path2="C:/Projet/BAC/python"
path3="/Users/Lucien/Copy/BAC/python/__pycache__"

os.chdir(path2)   #Aller dans le path entré precedement
print("")
print("Dossier Actuel: " +os.getcwd())
p=0
access=os.access("Musiques"+str(p) or "Documents"+str(p) or "Images"+str(p) or "Videos"+str(p), os.F_OK)
mp=slash+"Musiques"
ip=slash+"Images"
vp=slash+"Videos"
dp=slash+"Documents"
#Ajouter par Lucien
def pytrie (mp,ip,vp,dp,p,access,path,path2):    #Je definie la fonction avec toute les variable qui sont dedans (Crée une fonction va me permettre de relancer le programme en cas d'erreur)
    global option1
    option1=str(input("""Choisissez parmis les options suivantes:

    [1] - Trier par normal type (Musiques, Documents, Images, Vidéos)
    [2] - Trier par le format de votre choix
    [3] - Trier par type avec choix (Musiques ou Documents ou Images ou Vidéos)
    
    Saisissez 1 ou 2 ou 3: """))
    #Fin de Ajouter par Lucien
    #Modifier par Lucien
    if option1=="1":     #En fontion de ce que l'utilisateur à taper (J'ai mis les guillement vu que ce que rentre l'utilisateur c'est une chaine de caractére
        #Faire la boucle for
        while os.access("Musiques"+str(p) or "Documents"+str(p) or "Images"+str(p) or "Videos"+str(p), os.F_OK):
            p=p+1
        if os.access("Musiques"+str(p) or "Documents"+str(p) or "Images"+str(p) or "Vidéos"+str(p), os.F_OK) or os.access("Musiques" or "Documents" or "Images" or "Vidéos", os.F_OK):
            folder=str(input("D'anciens dossiers ont été detectés, en créer de nouveaux ? (O/N) :"))
            if folder=="o" or folder=="O":
                os.mkdir("Musiques"+str(p)) 
                os.mkdir("Images"+str(p))
                os.mkdir("Videos"+str(p))
                os.mkdir("Documents"+str(p))
                mp=slash+"Musiques"+str(p)
                ip=slash+"Images"+str(p)
                vp=slash+"Vidéos"+str(p)
                dp=slash+"Documents"+str(p)
        else:
            os.mkdir("Musiques") 
            os.mkdir("Images")
            os.mkdir("Vidéos")
            os.mkdir("Documents")
        
            
    elif option1=="2":
        info=(str(input("""
        Quel format de fichier voulez vous rassembler ? (ex : mp3 , png , mpeg..etc)

        Merci de les séparer des espaces si il y en a plusieurs

        """)))
        global exten ,extdossier #La fonction global veut juste dire que la variable va etre appliquer et valable dans tout le programme !
        exten=info.split(" ") #On range dans une liste chaque format qu'a entrer l'utilisateur. En gros: Utilisateur tape > mp3 flac     se qui donne > exten=['mp3', 'flac']
        extdossier=info.split(" ")  #On crée une variable qu'on va réutiliser plus tard pour avoir la liste sans *. car on peut pas crée un dossier avec une * et un .
        t=len(exten)
        for k in range(0):
            exten[k]="*."+exten[k]   #On va ajouter *. pour tout les format présent dans la liste crée par l'utilsateur.

    elif option1=="3":
        def suppr(access):
            global option2
            option2=str(input("""Quel type ?

            (1) Documents
            (2) Musiques
            (3) Images
            (4) Vidéos

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
                if not os.access("Vidéos" ,os.F_OK):
                    os.mkdir("Vidéos")

            else:
                print("""

        Merci de saisir une valeur correcte

        """)
        suppr(access) 
                    
    else:   
        print("""

        Merci de saisir une valeur correcte

        """)
        pytrie(mp,ip,vp,dp,p,access,path,path2)    #Si l'utilisateur à taper autre chose que 1,2 ou 3 > 2 il va afficher qu'il y a une erreur et il relance la fonction
       
pytrie(mp,ip,vp,dp,p,access,path,path2) #On execute la fonction
#Fin de modifier par Lucien


os.chdir(path)

                                               ## debut de modifier par Lionel ##

def move(ext,zerop): #Fonction pour deplacer "zerop" va etre remplacer par le deuxiéme terme mis dans la fonction. Par exemple pour musique on a move(ext,mp) >zerop va etre remplacer par mp
    #files=glob.iglob(os.path.join(path, ext))
    files=os.walk(path2)
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, path2+zerop)
                                                ## fin de modifier par Lionel ##
if option1=="1":            
    for ext in mpliste:  #On va parcourir les formats mis dans la liste que est dans le fichier extliste.py
        move(ext,mp)

    for ext in ipliste:
        move(ext,ip)

    for ext in vpliste:
        move(ext,vp)

    for ext in dpliste:
        move(ext,dp)
    print(""" ** Le déplacement des fichiers a été realisés avec succès.
    Merci de votre confiance.
    Bonne nuit.** """)
elif option1=="2":  
    for g in extdossier:  #extdossier c'est la variable qu'on a crée précédemment pour avoir la liste mais sans mes *. devant les éléments
        if not os.access(path2+slash+g ,os.F_OK):# On créé les dossiers si il ne sont pas déjà présents
            os.mkdir(path2+slash+g)   
        g1="*."+g  #On fait g1 pour que chaque élément sois ensuite remi avec *. pour pouvoir les déplacer.
        move(g1, slash+g)
                        
elif option1=="3":  #Ya rien de compliquer a comprendre si tu as compris le reste
    if option2=="1":
      for ext in dpliste:
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

####### SUPPRESSION DU DOSSIER PYCACHE #######
if os.path.exists(path3) == True:
    os.remove(path3)
###### FIN SUPPRESSION DU DOSSIER #######
