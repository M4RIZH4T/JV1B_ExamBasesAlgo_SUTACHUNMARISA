#Partie 1 : Tri à bulles 

###################################################################################
#Exercice1 : permuter deux valeurs d'un tableau à partir des indices. 
print("Exercice 1")
myTable1 = [1,2,3,4,5]

def Exercice1() : #Programme qui permute l'élément du premier indice et l'élément du dernier indice 

    print ("Tableau de départ :", myTable1)
    myTable1.insert(0,5) #permet d'insérer l'élément en position 0 à la position 5
    myTable1.pop() #permet de supprimer le dernier élément de la liste
    print ("Tableau avec une permutation :", myTable1)
    print("Nous avons permuté le premier et le dernier élément")

Exercice1() 

###################################################################################
#Exercice2 : mettre l'élément le plus grand à la fin du tableau lors de l'itération (NE MARCHE PAS COMPLETEMENT)
print("Exercice 2")
myTable2 = [9,7,8,10,6]

def Exercice2() : 

    print("Tableau de départ :", myTable2) 
    plusPetitElement = myTable2[0]
    for i in range (0, len(myTable2)) : 
        if (myTable2[i] > plusPetitElement):
            plusGrandElement = myTable2[i]
            indice = i
            myTable2.insert(5,plusGrandElement) #insère l'élément le plus grand à la fin de la liste 


    print("Plus grand élément :",plusGrandElement)
    print("Indice  :", i)
    print(myTable2)
            

Exercice2() 

###################################################################################
#Exercice 3 : tri à bulles complet (NE MARCHE PAS COMPLETEMENT)
print("Exercice 3")
myTable3 = [14,11,13,12,15]

def Exercice3() : 
    
    print("Tableau de départ :", myTable3)
    plusPetitElement = myTable3[0]
    for i in range(0,len(myTable3)):
        if(myTable3[i] < plusPetitElement):
            plusPetitElement = myTable3[i] 
            indicePlusPetitElement = i
            save = myTable3.pop(indicePlusPetitElement) #le .pop supprime l'indice du plus petit élément
            myTable3.insert(0, save)

    print("Le plus petit élément est", plusPetitElement)
    print("L'indice du plus petit élément est", indicePlusPetitElement) 
    print (myTable3)

Exercice3() 
###################################################################################
#Exercice 4 : pourquoi le tri à bulle est-il lent ? 

#Réponse : il est lent car il doit effectuer des itérations donc parcourir plusieurs fois le tableau, et si le tableau est très long, cela prendra encore plus de temps. Son ordre de grandeur est en ms pour des tableaux courts (5 éléments)
