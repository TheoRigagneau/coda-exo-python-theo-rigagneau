def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2(): 
    nom=input("Quel est votre nom ?")
    print("Bonjour",nom)

def exercice3() :
    print("Première ligne \n Deuxième ligne \n Troisième ligne")
def exercice4() :
    année_naissance=int(input("En quelle année est tu né")) ##Donner l'age d'une personne avec son année de naissance
    année_actuelle = 2025
    age=année_actuelle - année_naissance
    print ("tu as",age,"ans")
def exercice5() : ##somme
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" ))
    print("la somme des deux nombres est ",nb1+nb2)
def exercice6() : ##différence
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" ))
    print("la différence des deux nombres est ",nb1-nb2)
def exercice7() : ##produit
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" ))
    print("le produit des deux nombres est ",nb1*nb2)
def exercice8(): ##division
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" ))
    print("le resultat de la division des deux nombres est ",nb1/nb2)
def exercice9(): 
    nb=int(input("Donner un nombre que vous voulez mettre au carré"))
    print("le nombre au carré est", nb**2)
def exercice10():
    nb=int(input("Donner un nombre dont vous voulez le double"))
    print("le double de votre nombre est",nb*2)
def exercice11():
    nb=int(input("Donenr un nombre dont vous voulez la moitié"))
    print("le nombre réduit de moitié est", nb/2)
def exercice12():
    for i in range(5):
        print("Ce message doit sortir 5 fois")
def exercice13(): ##compter de 1 à 5
    for i in range(5):
        print(i+1)
def exercice14(): ##table de 2 allant de 2*1 a 2*5
    for i in range(1,6):
        print ("2 *",i,"=",2*i)
def exercice15(): ##
    longueur_coté=int(input("Quel est la tailel de la longueur ?"))
    print("Périmètre = ",longueur_coté*4)
def exercice16():
    longueur_coté=int(input("Quel est la taille de la longueur ?"))
    print("Aire = ",longueur_coté**2)
def exercie17():
    nb_euros=int(input("Quelle somme en € voulez vous transformer en $"))
    print(nb_euros,"€ = ",nb_euros*1.1,"$")
def exercice18():
    nb_minutes=int(input("combien de minutes voulez vous transformer en seconde)) ?"))
    print(nb_minutes,"minutes =",nb_minutes*60,"secondes")
def exercice19():
    prix_HT("quel est le prix HT ?")
    print("Prix TTC =", prix_HT*1.2)
def exercice20():
    nom=input("Quel et ton nom ?")
    age=int(input("Quel est ton age ?"))
    print("Bonjour",nom,"tu as",age,"age")
def exercice21():
    nb=int(input("Donne moi un nombre"))
    if nb>0 :
        print("ce nombre est positif")
    elif nb==0 :
        print("ce nombre est nul")
    else:
        print("ce nombre est négatif")
def exercice22():
    age=int(input("Quel est ton age ?"))
    if age>17:
        print("Majeur")
    else:
        print("Mineur")
def exercice23():
    note=int(input("Quelle est ta note ?)"))
    if note>=10:
        print("Validé")
    else:
        print("Non validé")
def exercice24():
    nb1=int(input("Donne un premier nb"))
    nb2=int(input("Donne un second nb"))
    if nb1>nb2 :
        print(nb1,"est plus grand")
    else:
        print(nb2,"est plus grand")
def exercice25():
    nb1=int(input("Donne un premier nb"))
    nb2=int(input("Donne un second nb"))
    if nb1<nb2:
        print("Ordre croissant : OUI")
    else :
        print("Ordre croissant : NON")
def exercice26() :
    nb= int ( input ( "Donne un nb" ) )
    if nb % 5 == 0 :
        print( "Divisible par 5" )
    else :
        print ( "Non divisible par 5" )
def exercice27() :
    age=int ( input ("Donne ton age" ) )
    if age < 12 :
        print ( "Enfant" )
    if 12< age < 17:
        print ( "Adolescent" )
    else :
        print ( "Adulte" )
def exercice28() :
    temp_eau= int( input ( "Quelle est la température de l'eau ?" ) )
    if temp_eau < 0 :
        print ( "Glace" )
    elif 0 < temp_eau < 100 :
        print ( "liquide" )
    else :
        print ( "Gazeux" ) 
def exercice29() :
    mention = float ( input ( "Quelle moyenne as tu eus au bac ?" ) )
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
    fin_compte = int ( input("Quel est la valeur de n" ) )
    for i in range(0,fin_compte) :
        print(i+1)
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


        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")
main()
        
            
