# Tache 2 : Le chiffre Playfair

import traceback, sys

#------CHIFFREMENT--------------------------------#

def verifW(secretKey):
    if ("W" in secretKey):
        secretKey = secretKey.replace("W", "") 
    return secretKey

def concatenat(secretKey):
    tmp = secretKey + "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    t = ''.join(sorted(set(tmp), key=tmp.index))
    return t

def verifDouble(secretKey):
	i = 0
	j = 1

	while j != len(secretKey): # j different du dernier caractere
		if(secretKey[i] == secretKey[j]) :
			tmp = secretKey[j:] 
			secretKey = secretKey[:j]
			secretKey = secretKey +"X"+ tmp
		i = i + 2 # incremmentation de 2
		j = j + 2
	if (len(secretKey) % 2) !=0:
		secretKey = secretKey + "X"
	return secretKey

def blocDeux(msg, tmp):
    i = 0
    j = 2
    while i <= len(msg)-1:
        tmp.append(msg[i:j])
        i = i + 2
        j = j + 2
    return tmp

def chiffrement(x, y, z):
		for i in range(0,5):
			for j in range(0,5):
				if (z[i][j] == x):
					i1 = i
					j1 = j
					print(i1,j1)
				if (z[i][j] == y):
					i2 = i 
					j2 = j
					print(i2,j2)
		if (i1 == i2): #Ligne
			j1 = (j1+1) % 5 # décalage à droite sur la meme ligne
			j2 = (j2+1) % 5
			print("Meme ligne: ",z[i1][j1] ,"",z[i2][j2])
			tmp1.append(z[i1][j1])
			return tmp1.append(z[i2][j2])
		elif (j1 == j2):#Colonne
			i1 = (i1+1) % 5
			i2 = (i2+1) % 5
			print("Meme colonne: ",z[i1][j1] ,"",z[i2][j2])
			tmp1.append(z[i1][j1])
			return tmp1.append(z[i2][j2])
		else: 
			print("En desordre dans le rectangle: ",z[i1][j2] ,"",z[i2][j1]) # prem ligne et deux colon et deux lign premiere col
			tmp1.append(z[i1][j2])
			return tmp1.append(z[i2][j1])



secretKey =  input('Entrer la clé (EN MAJUSCULE) : ')
secretKey = verifW(secretKey)#Recherche la presence de W
print("La clé devient : ",secretKey) # Suppression de W

#Suppression des chaines qui se repetent
secretKey = concatenat(secretKey)

#Creation de la matrice
nbr_columns = 5
l = [list(secretKey[i:i+nbr_columns]) for i in range(0, len(secretKey), nbr_columns)]
matrix = [s if len(s) == nbr_columns else s+[None]*(nbr_columns-len(s)) for s in l]        
print(matrix)


#-----------------------------------------------------------------------
tmp = [] 
msg =  input(' Entrer le message à chiffrer (meme nombre caractere que la clé) : ')
msg = verifDouble(msg)
print("Le message transformé est:  ",msg)

#Division du message clair en pair
tmp = blocDeux(msg, tmp)
print(tmp)


tmp1 = []
for i in range(0,len(tmp)):
        chiffrement(tmp[i][0],tmp[i][1],matrix)

#Conversion du vecteur en string
msg_chiff = ''.join(tmp1)
print("Le message chiffré est:  ",msg_chiff)

