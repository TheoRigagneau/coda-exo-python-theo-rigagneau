from random import randint
def garde_fou(a, minimum=None, maximum=None):
    if minimum is None:
        minimum = -float("inf")
    if maximum is None:
        maximum = float("inf")
    verif=0
    while verif==0:
        try :
            a=float(a)
            if a < minimum  or a > maximum:
                print("Ce nombre n'est pas toléré dans cet exerice")
                a=input("Donnez un nombre correspondant aux règles")
            else:
                verif=1
        except :
            print("Ce n'est pas un nombre")
            a=input("Donnez un nombre correspondant aux règles")
    return a


def garde_fou_carac(a):
    verif = 0
    while verif== 0 :
        try :
            float(a)
            print("Ce n'est pas une chaine de caractère")
            a=input("Saississez une vraie réponse")
        except :
            if a.replace(" ","")=="":
                print("Il n'y a pas de vrai texte")
                a=input("Saississez une vraie réponse")
            else:
                verif=1
    return a

def liste():
    valeur=""
    liste=[]
    somme=0
    while valeur !="0":
        valeur=garde_fou(input("Saississez un nombre ou insérer '0' pour demander si un nombre est dans la liste"),0,float("inf"))
        if valeur != 0 :
            liste.append(valeur)
        elif liste==[] and valeur==0 :
            valeur=1
        else:
            break
    return liste


def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2() :
    nom =garde_fou_carac(input("Quel est votre nom ?" ))
    print("Bonjour",nom)

def exercice3() :
    print("Première ligne \n Deuxième ligne \n Troisième ligne")
def exercice4() :
    année_naissance = int ( input ("En quelle année est tu né" ) ) ##Donner l'age d'une personne avec son année de naissance
    année_actuelle = 2025
    age=année_actuelle - année_naissance
    print ("tu as",age,"ans")
def exercice5() : ##somme
    nb1 = garde_fou ( input ("Donner un premier nombre" ) )
    nb2= garde_fou (input("Donner un second nombre" ) )
    print ("la somme des deux nombres est ",nb1+nb2)
def exercice6() : ##différence
    nb1 = garde_fou (input("Donner un premier nombre") )
    nb2 = garde_fou (input("Donner un second nombre" ) )
    print ("la différence des deux nombres est ",nb1-nb2)
def exercice7() : ##produit
    nb1 = garde_fou (input("Donner un premier nombre") )
    nb2 = garde_fou (input("Donner un second nombre" ) )
    print ("le produit des deux nombres est ",nb1*nb2)
def exercice8() : ##division
    nb1 = garde_fou (input("Donner un premier nombre") )
    nb2 = garde_fou (input("Donner un second nombre" ) ,0.0000001,float ('inf') )
    print("le resultat de la division des deux nombres est ",nb1/nb2)
def exercice9() : 
    nb= garde_fou(input("Donner un nombre que vous voulez mettre au carré") )
    print ("le nombre au carré est", nb**2)
def exercice10() :
    nb= garde_fou(input("Donner un nombre dont vous voulez le double") )
    print("le double de votre nombre est",nb*2)
def exercice11():
    nb = garde_fou(input("Donenr un nombre dont vous voulez la moitié"),0,float("inf") )
    print ("le nombre réduit de moitié est", nb/2)
def exercice12() :
    for i in range(5) :
        print("Ce message doit sortir 5 fois")
def exercice13() : ##compter de 1 à 5
    for i in range(5) :
        print(i+1)
def exercice14() : ##table de 2 allant de 2*1 a 2*5
    for i in range(1,6) :
        print ("2 *",i,"=",2*i)
def exercice15() : ##
    longueur_coté = garde_fou(input("Quel est la tailel de la longueur ?"),0.00001,float("inf") )
    print("Périmètre = ",longueur_coté * 4 )
def exercice16():
    longueur_coté=garde_fou(input("Quel est la taille de la longueur ?"),0.0001,float('inf') )
    print("Aire = ",longueur_coté**2)
def exercie17() :
    nb_euros = garde_fou(input("Quelle somme en € voulez vous transformer en $"),0,float('inf'))
    print(nb_euros,"€ = ",nb_euros*1.1,"$")
def exercice18() :
    nb_minutes=garde_fou(input("combien de minutes voulez vous transformer en seconde?"),1,float('inf'))
    print(nb_minutes,"minutes =",nb_minutes*60,"secondes")
def exercice19() :
    prix_HT = garde_fou(input("quel est le prix HT ?"),0,float('inf'))
    print("Prix TTC =", prix_HT*1.2)
def exercice20():
    nom = garde_fou_carac(input("Quel et ton nom ?"))
    age = garde_fou(input("Quel est ton age ?"),0,130)
    print("Bonjour",nom,"tu as",age,"age")
def exercice21() :
    nb = garde_fou(input("Donne moi un nombre"))
    if nb>0 :
        print("ce nombre est positif")
    elif nb==0 :
        print("ce nombre est nul")
    else:
        print("ce nombre est négatif")
def exercice22():
    age=garde_fou(input("Quel est ton age ?"),0,150)
    if age>17:
        print("Majeur")
    else:
        print("Mineur")
def exercice23():
    note=garde_fou(input("Quelle est ta note ?"),0,20)
    if note>=10:
        print("Validé")
    else:
        print("Non validé")
def exercice24():
    nb1=garde_fou(input("Donne un premier nb"))
    nb2=garde_fou(input("Donne un second nb"))
    if nb1>nb2 :
        print(nb1,"est plus grand")
    else:
        print(nb2,"est plus grand")
def exercice25():
    nb1=garde_fou(input("Donne un premier nb"))
    nb2=garde_fou(input("Donne un second nb"))
    if nb1<nb2:
        print("Ordre croissant : OUI")
    else :
        print("Ordre croissant : NON")
def exercice26() :
    nb= garde_fou( input ( "Donne un nb" ) , 0,float("inf"))
    if nb % 5 == 0 :
        print( "Divisible par 5" )
    else :
        print ( "Non divisible par 5" )
def exercice27() :
    age = garde_fou ( input ("Donne ton age" ) ,0,130)
    if age < 12 :
        print ( "Enfant" )
    if 12< age < 17:
        print ( "Adolescent" )
    else :
        print ( "Adulte" )
def exercice28() :
    temp_eau = garde_fou( input ( "Quelle est la température de l'eau ?" ) )
    if temp_eau < 0 :
        print ( "Glace" )
    elif 0 < temp_eau < 100 :
        print ( "liquide" )
    else :
        print ( "Gazeux" ) 
def exercice29() :
    mention =garde_fou( input ( "Quelle moyenne as tu eus au bac ?" ) ,0,20)
    if mention < 10:
        print("Recalé")
    elif 10 <= mention< 12 :
        print( "Passable" )
    elif 12 <= mention <14 :
        print( "Assez bien" )
    elif 14 <= mention < 16 :
        print( "Bien" )
    else :
        print ( "Très bien " )
def exercice30() :
    fin_compte =garde_fou( input("Quel est la valeur de n" ),0,float("inf"))
    for i in range(0 , fin_compte) :
        print(i+1)
def exercice31() : ##compte a rebourd
    début_compte =garde_fou ( input("Quel est la valeur de n" ),0,float("inf"))
    for i in range(0 , (début_compte+1)) :
        print(début_compte-i)
def exercice32() : #somme jusqu'a N
    numero_fin = garde_fou (input("Quel est la valeur du numéro final ? "  ),0,float("inf"))
    somme=0
    for i in range(0,numero_fin):
        somme+=(i+1)
    print(somme)
def exercice33(): #donner la table de multi du numéro
    numéro=garde_fou(input("Saississez un numéro"))
    for i in range(11):
        print(numéro*i)
def exercice34(): #######################################################
    numéro=int(garde_fou(input("Saississez un numéro"),0,1000))
    for i in range(numéro+1):
        if i%2==0:
            print(i)
def exercice35() :
    numéro=garde_fou(input("Saississez un numéro"),0,1000000)
    for i in range(numéro):
        if i**2<numéro:
            print(i**2)
def exercice36():
    nb_de_fois=garde_fou(input("Nombre de fois que vous voulez répeter le mot"),0,100)
    mot=garde_fou_carac(input("Quel mot voulez vous répeter ?"))
    for i in range(nb_de_fois):
        print(mot)
def exercice37():
    print("***\n**\n*")
def exercice38():
    opérateur=input("quel opérateur voulez vous utiliser(+ - * / )")
    if opérateur == "+" :
        exercice5()
    elif opérateur == "-" :
        exercice6()
    elif opérateur == "*" :
        exercice7()
    elif opérateur =="/" :
        exercice8()
    else:
        print("tape ce qui est demandé")
def exercice39():
    verrif=0
    nb_secret=randint(0,1000)
    while verrif ==0:
        verrif=1
        réponse=input("pensez vous que le nb est pair ou impair ?")
        if réponse=="pair":
            if nb_secret%2==0:
                print("Gagné !")
            else:
                print("Perdu :/")
        elif réponse=="impair":
            if nb_secret%2==0:
                print("Perdu :/")
            else:
                print("Gagné !")
        else:
            verrif=0
def exercice40():
    mdp=garde_fou_carac(input("saissir un mdp"))
    if len(mdp)<5:
        print("trop court")
    else :
        print("validé")
def exercice41():
    somme=0
    for i in range(5):
        valeur=garde_fou(int(input("Saississez une valeur entre 0 et 20")),0,20)
        somme+=valeur
    print('la valeur finale est',somme/5)
def exercice42():
    nb_mini=float("inf")
    nb_max=-float("inf")
    for i in range(5):
        nombre=int(input("Saississez un nombre"))
        if nombre <nb_mini:
            nb_mini=nombre
        elif nombre > nb_max:
            nb_max=nombre
    print("le nombre le plus petit est",nb_mini,"et le nombre le plus grand est",nb_max)
def exercice43():
    mot=garde_fou_carac(input("saississez un mot"))
    nb_voyelle=0
    voyelle="aeiouy"
    for lettre in mot:
        if lettre in voyelle:
            nb_voyelle+=1
    print("il y a",nb_voyelle)
def exercice44():
    mot = garde_fou_carac(input("Saisissez un mot à inverser : "))
    mot_inverse = mot[::-1]
    print("Le mot inversé est :", mot_inverse)

def exercice45():
    somme=0
    liste_nb=liste()
    for i in liste_nb:
        somme+=i
    print(somme)

def exercice46():
    liste_nb=liste()
    check=garde_fou(input("Choississez un nombre"))
    for i in liste_nb:
        if check==i:
            print("Oui !")
            break
    if check!=i:
        print("Non")
def exercice47():
    liste_nb=liste()
    check=garde_fou(input("Choississe un nombre"))
    nb_valeur=0
    for i in liste_nb:
        if check==i:
            nb_valeur+=1
    print(nb_valeur,"fois !")
def exercice48():
    nb=int(garde_fou(input("Donnez un nombre dont vous voulez les diviseurs entre 0 et 100000"),0,100000))
    for i in range (1,(nb+1)):
        if nb%i==0:
                 print(i)
def exercice49():
    verif=0
    nb=int(garde_fou(input("Donnez un nombre dont vous voulez savoir s'il est premier"),0,100000))
    for i in range(1,nb+1):
        if nb%i==0:
            verif+=1
    if verif==2:
        print(nb,"est premier")
    else:
        print(nb,"n'est pas premier")
def exercice50():
    nb=int(garde_fou(input("Donner un nombre pour savoir la suite de Fibonacci jusqu'a ce nombre"),0,100))
    l=[0]
    for i in range(nb):
        if l==[0]:
            l.append(1)
        else:
            print(l,i)
            l.append((l[i]+l[i-1]))
    print(l)
def exercice51(): #pascal
    triangle=[]
    for i in range(5):
        if i==0:
            ligne=[1]
        else:
            ligne_precedante=triangle[-1]
            ligne=[1]
            for j in range (len(ligne_precedante)-1):
                somme = ligne_precedante[j]+ligne_precedante[j+1]
                ligne.append(somme)
            ligne.append(1)
        triangle.append(ligne)
    for rangee in triangle:
        print(rangee)
def exercice52():
    l1,l2,l3=[],[],[]
    for i in range(9):
        nb=garde_fou(input("Saississez un nombre"))
        if 0<=len(l1)<3:
            l1.append(nb)
        elif 0<=len(l2)<3:
            l2.append(nb)            
        else:
            l3.append(nb)
    if sum(l1) == sum(l2) and sum(l3) == sum(l2) :
        if l1[0]+l2[0]+l3[0]== sum(l1) and l1[1]+l2[1]+l3[1] == sum(l1) and l1[2]+l2[2]+l3[2] == sum(l1):
            if l1[0]+l2[1]+l3[2] == sum(l1) and l1[2]+l2[1]+l1[0]:
                print ('Carré magique')
            else :
                print("Ce n'est pas un carré magique")
        else:
            print("Ce n'est pas un carré magique")
    else:
        print("Ce n'est pas un carré magique")
    
        
def main() :
    while True:
        print("\n=== Menu des exercices ===")
        print("q - Quitter")
        choix = input("Entrez le numéro de l'exercice à exécuter : ").strip().lower()

        if choix == "1" :
            exercice1()
        elif choix == "2" :
            exercice2()
        elif choix == "3" :
            exercice3()
        elif choix == "4" :
            exercice4()
        elif choix == "5" :
            exercice5()
        elif choix == "6" :
            exercice6()
        elif choix == "7" :
            exercice7()
        elif choix == "8" :
            exercice8()
        elif choix == "9" :
            exercice9()
        elif choix == "10" :
            exercice10()
        elif choix == "11" :
            exercice11()
        elif choix == "12" :
            exercice12()
        elif choix == "13" :
            exercice13()
        elif choix == "14" :
            exercice14()
        elif choix == "15" :
            exercice15()
        elif choix == "16" :
            exercice16()
        elif choix == "17" :
            exercice17()
        elif choix == "18" :
            exercice18()
        elif choix == "19" :
            exercice19()
        elif choix == "20" :
            exercice20()
        elif choix == "21" :
            exercice21()
        elif choix== "22" :
            exercice22()
        elif choix== "23" :
            exercice23()
        elif choix== "24" :
            exercice24()
        elif choix== "25" :
            exercice25()
        elif choix== "26" :
            exercice26()
        elif choix == "27" :
            exercice27()
        elif choix == "28" :
            exercice28()
        elif choix == "29" :
            exercice29()
        elif choix == "30" :
            exercice30()
        elif choix == "31" :
            exercice31()
        elif choix == "32" :
            exercice32()
        elif choix == "33" :
            exercice33()
        elif choix == "34" :
            exercice34()
        elif choix == "35" :
            exercice35()
        elif choix == "36" :
            exercice36()
        elif choix == "37" :
            exercice37()
        elif choix == "38" :
            exercice38()
        elif choix == "39" :
            exercice39()
        elif choix =="40" :
            exercice40()
        elif choix == "41" :
            exercice41()
        elif choix == "42" :
            exercice42()
        elif choix == "43" :
            exercice43()
        elif choix == "44" :
            exercice44()
        elif choix == "45" :
            exercice45()
        elif choix == "46" :
            exercice46()
        elif choix == "47" :
            exercice47()
        elif choix =="48" :
            exercice48()
        elif choix == "49" :
            exercice49()
        elif choix == "50" :
            exercice50()
        elif choix== "51" :
            exercice51()
        elif choix=="52" :
            exercice52()


        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")
main()
        
            
