def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    nom=input("Quel est votre nom ?")
    print("Bonjour",nom)

def exercice3() :
    print("Première ligne \n Deuxième ligne \n Troisième ligne")
def exercice4() :
    année_naissance=int(input("En quelle année est tu né"))
    année_actuelle = 2025
    age=année_actuelle - année_naissance
    print (age)
def exercice5() :
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" )
    print("la somme des deux nombres est ",nb1+nb2)
def exercice6() :
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" )
    print("la différence des deux nombres est ",nb1-nb2)
def exercice7() :
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" )
    print("le produit des deux nombres est ",nb1*nb2)
def exercice8():
    nb1=int(input("Donner un premier nombre"))
    nb2=int(input("Donner un second nombre" )
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
def exercice13():
    for i in range(5):
        print(i+1)
def exercice14():
    for i in range(1,6):
        print "2 *",i,"=",2*i
def exercice15():
    longueur_coté=int(input("Quel est la tailel de la longueur ?")
    print("Périmètre = ",longueur_coté*4)
def exercice16():
    longueur_coté=int(input("Quel est la taille de la longueur ?")
    print("Aire = ",longueur_coté**2)
def exercie17():
    nb_euros=int(input("Quelle somme en € voulez vous transformer en $")
    print(nb_euros,"€ = ",nb_euros*1.1,"$")
def exercice18():
    nb_minutes=int(input("combien de minutes voulez vous transformer en seconde ?"))
    print(nb_minutes,"minutes =",nb_minutes*60,"secondes")
def exercice19():
    prix_HT("quel est le prix HT ?")
    print("Prix TTC =", prix_HT*1.2)
def exercice20():
    nom=input("Quel et ton nom ?")
    age=int(input("Quel est ton age ?"))
    print("Bonjour",nom,"tu as",age,"age")
def exercice21():
    nb=(int(input("Donne moi un nombre")
    if nb>0 :
        print("ce nombre est positif")
    elif nb==0 :
        print("ce nombre est nul")
    else:
        print("ce nombre est négatif")
def exercice22():
def main():
    while True:
        print("\n=== Menu des exercices ===")
        print("q - Quitter")
        choix = input("Entrez le numéro de l'exercice à exécuter : ").strip().lower()

        if choix == "1":
            exercice1()
        elif choix == "2":
            exercice2()
        elif choix == "3":
            exercice3()
