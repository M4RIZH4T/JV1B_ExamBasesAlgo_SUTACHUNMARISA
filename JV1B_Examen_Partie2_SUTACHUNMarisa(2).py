#Partie 2 : tic tac toe 
#placement des cases 
    #1 2 3 
    #4 5 6 
    #7 8 9 

###################################################################################
#Exercice 1 : affiche la grille de jeu 
print("Exercice 1 :")

def Exercice1 () : 

    print ("BIENVENU SUR LE JEU DU TIC TAC TOE !")
    print ("Grille du morpion :")  
    print (" ") 

    L1 = ["1", "2", "3"] #premier tableau qui représente la première ligne 
    L2 = ["4", "5", "6"] #deuxième tableau qui représente la deuxième ligne 
    L3 = ["7", "8", "9"] #troisième tableau qui représente la dernière ligne 
    print (L1)
    print (L2) 
    print (L3)
    L = [L1, L2, L3] 

Exercice1() 

###################################################################################
#Exercice 2 : demander aux joueurs de choisir soit X soit O 
print(" ")
print("Exercice 2 :")

def Exercice2 () : 

    symbole_joueur1 = input('Choisissez soit X soit O : ')
    print("Le joueur 1 a sélectionné", symbole_joueur1, "!")
    symbole_joueur2 = input('Entrez le choix restant :')
    print("Le joueur 2 utilisera", symbole_joueur2, "!")
    print("LE JOUEUR QUI A CHOISI X COMMENCE LA PARTIE !")
    print (" ")

Exercice2() 

###################################################################################
#Exercice 3 : vérifier si oui ou non le joueur à réussi à aligner 3 symboles sur une même ligne 
