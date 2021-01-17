from tkinter import Tk, Button, Label, StringVar, Canvas, PhotoImage, NW, Entry, mainloop
import math, random
from random import randint
from math import sqrt 
from tkinter import messagebox



"""
Objectif du fichier : faire en sorte que l'utilisateur puisse jouer au Space Invaders ! 
Le jeu a été commencé pour la première fois le 17 Décembre à 8h09. Ce fichier précisément a été créé le 16 Janvier 2021 à 16h05 car nous avons changé de fichier d'origine.
Auteurs: Julien Falgayrettes, Adrien Moreira Da Silva
"""


Mafenetre = Tk()
Mafenetre.title('Space Invaders')


widthCanevas = 550
heightCanevas = 510
Canevas = Canvas(Mafenetre, width = widthCanevas , height = heightCanevas)
Canevas.grid()

Txt = "Détruit tous les vaisseaux pour gagner la partie et pour devenir le meilleur !                    Utilise les touches q et d pour te déplacer, et la touche l pour tirer des missiles. Attention, tu as l'Alien dangereux au centre qui doit etre touché 3 fois. Et aussi, les Aliens seront encore plus rapide quand ils seront moins de 4 ! "
    
listeScore = [0]


def main():

    """ Voici la fonction principale. Elle contient plusieurs sous fonctions (fonctions définition des variables, des boutons et des images, fonctions de tir des Aliens etc...) qui permettent le bon fonctionnement du programme. """
    
    global ViesRestantes, Ilot1, Ilot2, Ilot3, ilot1Touchés, ilot2Touchés, ilot3Touchés, vieIlot, ViesRestantes, Nbtouche_AlienDangereux, eviteBug, Largeur, Hauteur, X, Y, DX, DY
    variables()
    boutons_images()
    images()
    tirAlien()
    finPartie()
    DetruireVaisseau()
    deplacement()



def remain():

    """ La fonction remain permet de rejouer. On nettoie pour cela le Canvas et on redéfinie les variables avant de réappliquer la fonction main() vue précédemment. """
    
    global Canevas
    Canevas.destroy()
    widthCanevas = 550
    heightCanevas = 510
    Canevas = Canvas(Mafenetre, width = widthCanevas , height = heightCanevas)
    

    Canevas.focus_set()


    Canevas.bind('q', Clavier)
    Canevas.bind('d', Clavier)
    Canevas.bind('l', Clavier)

    Canevas.grid(row = 0)

    main()
    

    
def Regle():

    """ Cette fonction définie les règles du jeu en affichant un message quand on clique sur le bouton 'Regles' définie dans la fonction boutons. """ 
    
    messagebox.showinfo("Règle du jeu" , Txt)


    
def boutons_images():

    """ Cette fonction définie tous les boutons, Labels et quelques images nécessaires au bon fonctionnement du jeu. """
    """ Les variables définies passent en global pour communiquer avec les autres programmes. """
    
    global YouWin, finpartie, Score_Utilisateur, gameOver, bg, background, Score, nombreVies, nombreViesUtilisateur, Démarrer, HighScore, meilleurScore, Regles, optionUtilisateur, BoutonQuitter



    #Création du bouton de Score
    
    Score = StringVar()
    scoreUtilisateur = Label( Mafenetre, textvariable = Score)
    scoreUtilisateur.grid(row = 1)
    Score.set('Score : 0')


    # On gère le score de l'utilisateur avec cette variable que l'on initialise à 0.
    
    Score_Utilisateur = 0


    # Image quand l'utilisateur gagne.
    
    YouWin = PhotoImage(file = "youWin.gif")
    Youwin = Canevas.create_image( 0, 0, image = YouWin, anchor = "nw")


    # Image quand l'utilisateur perd.
    
    gameOver = PhotoImage(file = 'gameover.gif')
    finpartie = Canevas.create_image( 0, 0, image = gameOver, anchor = "nw")
    bg = PhotoImage(file = "bg.gif")
    background = Canevas.create_image( 0, 0, image = bg, anchor = "nw")

    # Gestion du nombre de vies de l'utilisateur.
    
    nombreVies = StringVar()
    nombreViesUtilisateur = Label( Mafenetre, textvariable = nombreVies)
    nombreViesUtilisateur.grid(row = 2)
    nombreVies.set('Vies restantes : 3' )

    # On peut aussi recommencer une partie quand on veut quand on clique sur 'New Game' ! L'appuie sur ce bouton va en fait lancer la fonction remain().
    
    Démarrer = Button(Mafenetre, text = "New Game",command = remain)
    Démarrer.grid(row = 3)


    # La fonction afficheScore() se lance à l'appuie de ce bouton.
    
    HighScore = StringVar()
    meilleurScore = Button( Mafenetre, textvariable = HighScore, command = afficheScore)
    meilleurScore.grid(row = 4)
    HighScore.set('Highscore')


    # La fonction Regle() se lance à l'appuie de ce bouton.
    
    Regles = StringVar()
    optionUtilisateur = Button( Mafenetre, textvariable = Regles , command = Regle)
    optionUtilisateur.grid(row = 5)
    Regles.set('Règles du jeu')


    # Pour quitter proprement le jeu on utilise ce bouton.
    
    BoutonQuitter = Button(Mafenetre,text='Quitter',command = Mafenetre.destroy)
    BoutonQuitter.grid(row = 6)





def images():
    
    """ Voici les images restantes qui sont créées ici ! """
    """ Les variables définies passent en global pour communiquer avec les autres programmes. """

    global AlienDangereux, missile, listeIlots, Laser, AlienQuiTir, AlienQuiTir2, AlienQuiTir3, AlienQuiTir4, infoAliens, infoAlienDangereux, infoAliensInnocents, InfoGeneralAliens, Ilot1, Ilot2, Ilot3, AbscissesAliens, AlienQuiTir, AlienQuiTir2missile, missileVaisseau, alienquitir, blocdeprotec, Vaisseau, Vaisseau2, AlienDangereux2, AlienInnocentimage, AlienInnocent1, AlienInnocent2, AlienInnocent3


    #Leur nom étant assez explicit, il n'est pas nécessaire ici de rajouter des commentaires explicatifs.
    

    missile = PhotoImage(file = 'tirALien.gif')
    missileVaisseau = PhotoImage(file = 'Missile.gif')

    alienquitir= PhotoImage(file = 'alienquitir.gif')
    blocdeprotec=PhotoImage(file = 'protection.gif')
    Vaisseau2 = PhotoImage(file = 'vaisseau.gif')
    AlienDangereux2=PhotoImage(file = 'aliendangereux.gif')
    AlienInnocentimage=PhotoImage(file = 'alieninnocent.gif')


    Vaisseau = Canevas.create_image(AbscisseVaisseau,OrdonneesVaisseau,image = Vaisseau2)


    # On espace les Aliens et les Ilots de manière régulière avant de mettre ces images dans des listes que l'on va utiliser dans d'autres programmes.
    # Ces listes vont servir notamment à connaitre si l'élément (par exemple le Laser) est toujours présent ou non en vérifiant la taille de la liste. 
    
    AlienInnocent1 = Canevas.create_image(abscissesAlien + 50, ordonneesAlien  + 135, image = AlienInnocentimage)
    AlienInnocent2 = Canevas.create_image(abscissesAlien + 150, ordonneesAlien  + 135, image = AlienInnocentimage)
    AlienInnocent3 = Canevas.create_image(abscissesAlien + 250, ordonneesAlien  + 135, image = AlienInnocentimage)

    AlienDangereux = Canevas.create_image(abscissesAlien + 150, ordonneesAlien + 60, image = AlienDangereux2)


    AlienQuiTir = Canevas.create_image(abscissesAlien, ordonneesAlien  , image = alienquitir)
    AlienQuiTir2 = Canevas.create_image(abscissesAlien + 100, ordonneesAlien, image = alienquitir)
    AlienQuiTir3 = Canevas.create_image(abscissesAlien + 200, ordonneesAlien , image = alienquitir)
    AlienQuiTir4 = Canevas.create_image(abscissesAlien + 300, ordonneesAlien , image = alienquitir)

    infoAliens = [AlienQuiTir,AlienQuiTir2,AlienQuiTir3,AlienQuiTir4]    
    infoAlienDangereux = [AlienDangereux]
    infoAliensInnocents = [AlienInnocent1,AlienInnocent2,AlienInnocent3]

    InfoGeneralAliens = infoAliens + infoAlienDangereux + infoAliensInnocents


    Ilot1 = Canevas.create_image(40, OrdonneesVaisseau - 80, image = blocdeprotec)
    Ilot2 = Canevas.create_image(widthCanevas / 2, OrdonneesVaisseau - 80, image = blocdeprotec)
    Ilot3 = Canevas.create_image(widthCanevas - 40 , OrdonneesVaisseau - 80, image = blocdeprotec)

    listeIlots=[Ilot1,Ilot2,Ilot3]



def variables():
    
    global ViesRestantes, Ilot1, Ilot2, Ilot3, ilot1Touchés, ilot2Touchés, ilot3Touchés, vieIlot, ViesRestantes, Nbtouche_AlienDangereux, eviteBug, Largeur, Hauteur ,vitesse, abscissesAlien, ordonneesAlien, DX, DY, widthCanevas, heightCanevas, PremierPassage3, PremierPassage2, premierPassage, AbscisseVaisseau, OrdonneesVaisseau

    """ Cette fonction initialises toutes les variables nécessaires au jeu. """

    Nbtouche_AlienDangereux = 3

    # eviteBug permet en fait d'éviter un problème que l'on avait, sans cela les lasers d'Aliens restaient parfois bloquer sur le Canvas et ne se déplaçaient pas.
    
    eviteBug = 0

    Largeur = 30
    Hauteur = 30

    vitesse = 10
    angle = 0

    DX = vitesse 
    DY = 0

    abscissesAlien = 15
    ordonneesAlien = 30

    premierPassage = 0
    PremierPassage2 = 0
    
    DXtir = vitesse 
    DYtir = 0

    AbscissesAliens = [0,100,200,300]

    ViesRestantes = 3

    ilot1Touchés = 2
    ilot2Touchés = 2
    ilot3Touchés = 2
    
    vieIlot = [ilot1Touchés,ilot2Touchés,ilot3Touchés]
    
    widthCanevas = 550
    heightCanevas = 510

    AbscisseVaisseau = 285
    OrdonneesVaisseau = 470



    
def deplacement():
    
    global abscissesAlien, ordonneesAlien, DX, DY, Largeur, Hauteur, widthCanevas, heightCanevas

    """La fonction deplacement() fait se déplacer les Aliens. Ils se déplacent tous ensemble à la meme vitesse. """


    # Si l'Alien de droite dépasse le bord droit du Canvas alors on fait faire un 'demi-tour' aux Aliens en les faisant descendre de 10px en ordonnées. On fait de meme pour l'Alien de gauche avec le bord gauche. 
    
    if abscissesAlien + 300 + DX > widthCanevas - 15 :
        
        abscissesAlien = abscissesAlien - DX
        DX = -DX
        ordonneesAlien = ordonneesAlien + 10

    if abscissesAlien + DX < 15:
        
        abscissesAlien = abscissesAlien + DX
        DX = -DX
        ordonneesAlien = ordonneesAlien + 10


    # Les Aliens se déplacent avec ces deux lignes ci-dessous ! Selon si DX est positif ou négatif, l'alien se déplacera vers la droite ou la gauche. 
    abscissesAlien = abscissesAlien + DX

    

    Canevas.coords(AlienQuiTir, abscissesAlien, ordonneesAlien)
    Canevas.coords(AlienQuiTir2, abscissesAlien + 100, ordonneesAlien )
    Canevas.coords(AlienQuiTir3, abscissesAlien + 200, ordonneesAlien )
    Canevas.coords(AlienQuiTir4, abscissesAlien + 300, ordonneesAlien )

    Canevas.coords(AlienDangereux, abscissesAlien + 150, ordonneesAlien + 60)
    
    Canevas.coords(AlienInnocent1, abscissesAlien + 50, ordonneesAlien + 135)
    Canevas.coords(AlienInnocent2, abscissesAlien + 150, ordonneesAlien + 135)
    Canevas.coords(AlienInnocent3, abscissesAlien + 250, ordonneesAlien + 135)


    if len(InfoGeneralAliens) > 4:
        Canevas.after(80, deplacement)
        
    elif len(InfoGeneralAliens) <= 4:
        Canevas.after(40, deplacement)

    
    if len(Canevas.coords(Vaisseau)) == 0:
        DX = 0
        DY = 0




def creationTir():
    
    global AbscisseVaisseau,OrdonneesVaisseau,Laser

    """ La fonction creationTir créer l'image du missile du vaisseau seulement si le vaisseau est présent sur le Canvas. """

    
    XLaser = AbscisseVaisseau
    YLaser = OrdonneesVaisseau
    
    if len(Canevas.coords(Vaisseau)) == 2:
        
        Laser = Canevas.create_image(XLaser, YLaser, image = missileVaisseau)



def tirAlien():

    global listeLasers, premierPassage, XlaserAliens, YlaserAliens, eviteBug


    XlaserAliens = abscissesAlien
    YlaserAliens = ordonneesAlien 
    
    """ tirAlien() gère le tir des Aliens envoyé par les Aliens en haut du Canvas et l'Alien dangereux (au centre).""" 

    tirAleatoire = randint(1,2)
    listeLasers = []

    if len(Canevas.coords(Vaisseau)) == 2:
        
        if len(infoAliens) >= 1:

            # On choisit un nombre au hasard entre 1 et 2 si et seulement s'il y a toujours le Vaisseau et au moins un Alien sur le Canvas.
            
            choixVaisseau = randint(0,len(infoAliens) - 1)


            # Si ce nombre aléatoire vaut 1 alors un Alien du fond tir, sinon rien ne se passe.

            
            if tirAleatoire == 1 and eviteBug > 0 and len(Canevas.coords(infoAliens[choixVaisseau])) == 2:
                
                abscissesLaserAlien=Canevas.coords(infoAliens[choixVaisseau])[0]
                laserAliens = Canevas.create_image(abscissesLaserAlien, YlaserAliens ,image = missile)
                premierPassage += 1

                listeLasers.append(laserAliens)
                
            eviteBug += 1           


        # L'Alien dangereux est tellement dangereux qu'il tir tout le temps (toutes les 1,5secondes) ! Gare à lui ! 
            
        if len(infoAlienDangereux) == 1:
                        
            laserAlienDangereux = Canevas.create_image(abscissesAlien + 150 , ordonneesAlien + 67.5 ,image = missile)
            premierPassage += 1
            listeLasers.append(laserAlienDangereux)


                
    deplacemenTirAliens(premierPassage)


            
    Canevas.after(1500, tirAlien)



def Clavier(event):

    """ La fonction Clavier détecte la touche sur laquelle l'utilisateur appuie grace à 'event' qui est pris en entrée de cette fonction. En sortie de cette fonction on va faire déplacer le vaisseau. """
    
    global AbscisseVaisseau, OrdonneesVaisseau, widthCanevas, Xtir, Ytir, Laser, DXtir, DYtir, PremierPassage2 

    touche = event.keysym


    # Si l'utilisateur appuie sur 'd' ou 'q' alors il se déplacera respectivement à droite ou à gauche.
    
    if touche == "d":
        AbscisseVaisseau += 20
        
    if touche == "q":
        AbscisseVaisseau -= 20


    # Grace à ces deux conditions ci-dessous il ne peut pas sortir du Canevas.
    
    if AbscisseVaisseau > widthCanevas :
        AbscisseVaisseau = widthCanevas - 10

    if AbscisseVaisseau < 0:
        AbscisseVaisseau = 14      


    # S'il appuie sur 'l', un missile partant du vaisseau en direction des Aliens s'envoie.
    
    if touche == "l":

        PremierPassage2 += 1
        Xtir = AbscisseVaisseau
        Ytir = OrdonneesVaisseau
        creationTir()
        deplacemenTir(PremierPassage2)
      
   
    
    Canevas.coords(Vaisseau,AbscisseVaisseau,OrdonneesVaisseau)




def deplacemenTir(PremierPassage2):
    
    global AbscisseVaisseau, OrdonneesVaisseau, widthCanevas, Xtir, Ytir, abscissesAlien, ordonneesAlien, touche, Laser, infoAliens, Nbtouche_AlienDangereux, Score_Utilisateur,abscissesAliens,ordonneesAliens
    """deplacemenTir prend en entrée PremierPassage2 (décrite juste en dessous avec le #). Cette fonction permet de faire se déplacer le laser/missile du Vaisseau. """

    
    Canevas.unbind('l')

    # Les PremierPassage(1,2,3)... permettent en fait de créer un compteur qui fait que le programme se déclenche seulement s'ils valent 0.
    # Ils ont permis de corriger un problème qui faisait que qu'à chaque fois qu'on entrait dans la boucle les lasers allaient de plus en plus vite à chaque fois qu'ils étaient envoyés car les programmes se lancent en parallèle plusieurs fois lorsque l'on appuie sur la touche d'envoie du laser.  

    PremierPassage3 = 0


    if PremierPassage2 == 1:
        Ytir = Ytir - 35


    if len(Canevas.coords(Vaisseau)) == 2:
        
        for k in range(len(InfoGeneralAliens)):

            if PremierPassage3 == 0 and Canevas.coords(Laser) != [] and Canevas.coords(InfoGeneralAliens[k]) != []:

                abscisseslaserVaisseau=Canevas.coords(Laser)[0]
                ordonneeslaserVaisseau=Canevas.coords(Laser)[1]
                abscissesAliens=Canevas.coords(InfoGeneralAliens[k])[0]
                ordonneesAliens=Canevas.coords(InfoGeneralAliens[k])[1]


                # On gère la collision en passant par la distance euclidienne entre les deux objets.
                
                if sqrt((abscissesAliens-abscisseslaserVaisseau) ** 2 + (ordonneesAliens-ordonneeslaserVaisseau) ** 2) <= 40:
        
                    PremierPassage3 += 1

                    # On a 3 types d'Aliens donc on se renseigne pour savoir avec quel type d'Alien la collision du laser du Vaisseau se fait.
                    # Une fois qu'on connait le type d'Alien, on le supprime. Il existe une exception, c'est l'Alien dangereux : il a besoin d'etre touché 3 fois avant d'etre tué.
                    # A chaque fois qu'un Alien est tué le score est actualisé. +10 pour un alien innocent, +25 pour un alien "classique" et +150 pour le Boss !
                    

                    if InfoGeneralAliens[k] in infoAliensInnocents:
                    
                        Score_Utilisateur += 10
                        Score.set('Score :' + str(Score_Utilisateur))
                        Canevas.delete(InfoGeneralAliens[k])
                        del InfoGeneralAliens[k]

                    elif InfoGeneralAliens[k] in infoAliens:
                        
                        Score_Utilisateur += 25
                        Score.set('Score :' + str(Score_Utilisateur))
                        Canevas.delete(InfoGeneralAliens[k])
                        del InfoGeneralAliens[k]


                    elif InfoGeneralAliens[k] in infoAlienDangereux:
                        
                        Nbtouche_AlienDangereux -= 1
                        
                        if Nbtouche_AlienDangereux == 0:
                            
                            Score_Utilisateur += 150
                            Score.set('Score :' + str(Score_Utilisateur))

                            Canevas.delete(InfoGeneralAliens[k])
                            del InfoGeneralAliens[k]
                            del infoAlienDangereux[0]


                    Canevas.delete(Laser)


        # On supprime le laser du vaisseau s'il arrive au delà la hauteur maximale du Canvas pour ne pas prendre de l'espace mémoire inutile. 
        
        if Ytir < 10:
            
            Canevas.bind('l',Clavier)
            Canevas.delete(Laser)


        # On actualise les coordonées du Laser et le programme toutes les 70ms. 
        
        Canevas.coords(Laser, Xtir, Ytir)
        Canevas.after(70, lambda: deplacemenTir(PremierPassage2))






def deplacemenTirAliens(premierPassage):

    """ deplacemenTir prend en entrée PremierPassage (décrite juste en dessous avec le #). Cette fonction permet de faire se déplacer le laser/missile des Aliens. """
    """ On a en global la liste de lasers que les aliens envoient, le nombre de vies restantes à l'utilisateur et les coordonnées du vaisseau. Cela sert à intéragir avec les autres programmes. """ 
    

    global listeLasers, ViesRestantes 

    # Les PremierPassage(1,2,3)... permettent en fait de créer un compteur qui fait que le programme se déclenche seulement s'ils valent 0.
    # Ils ont permis de corriger un problème qui faisait que qu'à chaque fois qu'on entrait dans la boucle les lasers allaient de plus en plus vite à chaque fois qu'ils étaient envoyés car les programmes se lancent en parallèle plusieurs fois lorsque l'on appuie sur la touche d'envoie du laser.  


    if premierPassage == 1:

        for k in range(len(listeLasers)):

            # On entre dans la boucle seulement si un Laser est présent dans le Canvas 
            if  len(Canevas.coords(listeLasers[k])) == 2 and Canevas.coords(listeLasers[k])[1] < heightCanevas  :

                
                Canevas.move(listeLasers[k],0,35)
                IlotsDeProtection(listeLasers[k])

                #IlotsProtection ayant été testé on doit revoir s'il y a toujours un laser et voir s'il y a un vaisseau présent sur le Canvas.
                
                if len(Canevas.coords(listeLasers[k])) == 2 and len(Canevas.coords(Vaisseau)) == 2:
                    
                    abscisseslaserAliens = Canevas.coords(listeLasers[k])[0]
                    ordonnéeslaserAliens = Canevas.coords(listeLasers[k])[1]
                    abscissesVaisseau=Canevas.coords(Vaisseau)[0]
                    ordonnéesVaisseau=Canevas.coords(Vaisseau)[1]

                
                    # On gère la collision en passant par la distance euclidienne entre les deux objets.
                    
                    if sqrt((abscissesVaisseau - abscisseslaserAliens) ** 2 + ( ordonnéesVaisseau - ordonnéeslaserAliens) ** 2) <= 50:

                        Canevas.delete(listeLasers[k])
                        
                        ViesRestantes -= 1
                        nombreVies.set('Vies restantes : ' + str(ViesRestantes))
                        
                        if ViesRestantes == 0:
                            
                            Canevas.delete(Vaisseau)
                            Canevas.delete(background)
                            listeScore.append(Score_Utilisateur)
                            

                
                
            # On supprime le laser d'Alien s'il ne touche pas le vaisseau pour ne pas prendre de l'espace mémoire inutile. 
            
            elif len(Canevas.coords(listeLasers[k])) == 2 and Canevas.coords(listeLasers[k])[1] > OrdonneesVaisseau :

                Canevas.delete(listeLasers[k])

    

        
    Canevas.after(70, lambda: deplacemenTirAliens(premierPassage))



def afficheScore():
        scoreMax = max(listeScore)
        messagebox.showinfo("meilleur score", f"{scoreMax}")




def IlotsDeProtection(laserAliens):

    """ La fonction IlotsDeProtection prend en entrée les lasers envoyés par les Aliens et gère la collision entre ces lasers et les blocs de protection. """
    """ On passe en global les 3 ilots pour informer leur état pour que les autres programmes puissent s'adapter. """ 
    
    global ilot1Touchés, ilot2Touchés, ilot3Touchés, Laser

 


    for k in range(len(listeIlots)):


        # Pour rentré dans le programme on vérifie que sur le Canvas il y a bien au moins un laser d'Alien et un bloc de protection présent.
        
        if len(Canevas.coords(laserAliens)) == 2 and len(Canevas.coords(listeIlots[k])) == 2:
            
            abscisseslaserAliens=Canevas.coords(laserAliens)[0]
            ordonnéeslaserAliens=Canevas.coords(laserAliens)[1]
            abscissesIlot=Canevas.coords(listeIlots[k])[0]
            ordonnéesIlot=Canevas.coords(listeIlots[k])[1]


            
            # On gère la collision en passant par la distance euclidienne entre les deux objets. 
            
            if sqrt((abscissesIlot - abscisseslaserAliens) ** 2 + (ordonnéesIlot - ordonnéeslaserAliens) ** 2) <= 50:

                vieIlot[k] -= 1
                Canevas.delete(laserAliens)
                    
                if vieIlot[k] == 0:
                        
                    Canevas.delete(listeIlots[k])               
        

    Canevas.after(70, lambda: IlotsDeProtection(laserAliens))



        
def DetruireVaisseau():

    """ La fonction DetruireVaisseau() fait que le vaisseau se détruit si un Alien le touche. """
    """ On a en global les ordonnées et abscisses respectives du Vaisseau et de l'Alien car on prend ces variables d'autres programmes. """ 

    
    global OrdonneesVaisseau,AbscisseVaisseau,abscissesAlien, ordonneesAlien


    for Alien in InfoGeneralAliens:
        
        if len(Canevas.coords(Alien)) == 2 and len(Canevas.coords(Vaisseau)) == 2:

            
            if sqrt((AbscisseVaisseau - abscissesAlien) ** 2 + (OrdonneesVaisseau - ordonneesAlien) ** 2) <= 50:
                
                Canevas.delete(Vaisseau)
                Canevas.delete(background)
                

                print('La partie est perdue !')
                 
        
    Mafenetre.after(70, DetruireVaisseau)




def finPartie():

    """ finPartie() fait que la partie se termine si il n'y a plus d'Aliens dans le Canvas. """

    if len(InfoGeneralAliens) == 0:
        
        Canevas.delete(background)
        Canevas.delete(finpartie)
        listeScore.append(Score_Utilisateur)
      
        
    Mafenetre.after(100, finPartie)

#On lance ici la fonction principale et on demande à lancer la fonction Clavier() quand on appuie sur 'q', 'l' ou 'd'.
    
main()

Canevas.focus_set()

Canevas.bind('q', Clavier)
Canevas.bind('d', Clavier)
Canevas.bind('l', Clavier)

Canevas.grid()




mainloop()



