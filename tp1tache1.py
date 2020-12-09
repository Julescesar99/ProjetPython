from itertools import starmap, cycle 
import collections 


# Tache 1 : codage de Vigenère

##fonction decal_droite
def decal_droite(valeur):
    n = input('Entrer le nombre de décalage à droite = ')
    n = int(n)
    print("le message decalé est:")
    return  valeur[-n:] + valeur[:-n]

##fonction decal_gauche
def decal_gauche(valeur):
    n = input('Entrer le nombre de décalage à gauche :')
    n = int(n)
    print("le message decalé est:" )
    return valeur[n:] + valeur[:n]

# ---Chiffrement
def chiffre(msg, clé):
    msg = filter(str.isalpha, msg.upper())
    def encrypt(m, c):
        # cryptage par lettre 
        return chr((((ord(c) + ord(m)) - 130) % 26) + ord('A'))        
    return ''.join(starmap(encrypt, zip(msg, cycle(clé))))

# ---Déchiffrement 
def dechiffre(msg, clé):
    def dec(c, k):
        # décryptage par lettre  
        return chr((((ord(c) - ord(k)) - 130) % 26) + ord('A'))
    return ''.join(starmap(dec, zip(msg, cycle(clé))))

## fonction apparitions(texte) 
def apparitions(texte):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    listeNumberApparition = []
    for i in range(26):
    	# count() méthode renvoie le nombre d'éléments avec la valeur spécifiée(i).
        cpt = texte.count(alphabets[i])
        listeNumberApparition.append(alphabets[i]) 	# ajouter l'alphabet
        listeNumberApparition.append(cpt)	   		# ajouter nombre d'apparition à la liste
    return listeNumberApparition


def pos_to_char(pos):
    return chr(pos + 65) # décalage ascii

def trouVerCle(text,taille):
    cles = []
    for i in range(0,taille):
        tmp = text[i::taille] # divise le texte chiffré selon la clé
        # trouver la lettre qui se repete le plus pour chaque partie et le considerer comme la lettre E
        tmp2 = collections.Counter(tmp).most_common(1)[0]
        print (tmp2)
        # trouver la distance entre la lettre qui se repete le plus et E
        tmp3 = ord(tmp2[0]) - ord('E')
        print(pos_to_char(tmp3)) # trouver la lettre selon la distance
        cles.append(pos_to_char(tmp3)) # ajouter 1 er cara clé apres 2, 3 ...
    return cles



def main():
    choice = int(input("1. Décalage à droite:\n2. Décalage à gauche\n3. Chiffrement\n4. Déchiffrement\n5. Apparition des caractères\n6. Trouver la clé\nChoisir(1,2,3,4,5,6): "))

    if choice == 1:
        text = input("Decalage à droite: \n  Entrer le message à decaler: ")
        print (decal_droite(text))
    elif choice == 2:
        text = input("Decalage à gauche: \n  Entrer le message à decaler: ")
        print (decal_gauche(text))

    elif choice == 3 :
        text = input("Chiffrement: \n  Entrer le message à chiffrer: ")
        clé = input("  Entrer la clé: ")
        encryptr = chiffre(text, clé)
        print("----------------- Texte en clair ------------------ \n") 
        print(text,"\n")
        print("----------------- Texte chiffré ------------------- \n") 
        print(encryptr,"\n")
    elif choice == 4:
        encryptr = input("Dechiffrement: \n  Entrer le message chiffré: ")
        clé = input("  Entrer la clé: ")
        decr = dechiffre(encryptr, clé)
        print("----------------- Texte en clair ------------------ \n") 
        print(encryptr,"\n")
        print("----------------- Texte dechiffré ----------------- \n") 
        print(decr,"\n")

    elif choice == 5:
        text = input("Entrer le texte:")       
        print("----------------- Liste d'apparition des carecteres ----------------- \n")
        print(apparitions(text),"\n")

    elif choice == 6:
        encryptr = input("Entrer le message crypté: ")
        clé = input("Entrer la clé: ")
        tailleCle = len(clé)
        key_find = ''.join(trouVerCle(encryptr,tailleCle)) # convertion de la clé en chaine de caractere
        print("La clé est:  ", key_find)


    else:
        print("Mauvais choix.")

if __name__ == "__main__":
    main()
