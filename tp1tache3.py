# Tache 3 :  Le chiffre de Merkle-Hellman

import random

def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)

def key_generator(n):
    # generer une liste super croissante aleatoirement 
    private_key = [0] * n
    max1 = pow(2,n)
    min1 = pow(2,n-1)
    private_key[0] = random.randint(min1,max1)
    print(private_key[0])
    i = 1
    min = 0
    ai = private_key[0]
    
    while i < n:
        max = pow(2,n+i-1)
        min = min+ai
        private_key[i]=random.randint(min,max)
        ai = private_key[i]
        i = i+1
    print ("La liste super croissante  ")
    print(private_key)
    N = random.randint(min1,pow(2,2*n))
    print("le valeur de N est  ")
    print(N)
    u = random.randint(1,n-1)
    while pgcd(u,N) != 1:
        u = random.randint(1,n-1)

    print("le valeur de u est  ")
    print(u)
    #generer une suite non super croissante
    public_key = [0]*n
    cpt = 0
    for i in private_key:
        public_key[cpt] = (u*i)%N
        cpt=cpt+1
    print("la cle public est  ")
    print(public_key)
    return public_key ,private_key,N,u


def chiffrement(message,public_key):
    cipher = 0
    for i in range(len(message)):
        cipher = cipher+(int(message[i])*int(public_key[i]))
    return cipher


def main():
    print()
    n = int(input())
    print(key_generator(n))
    cles = key_generator(n)
    text = input("inserer le message a chiffrer : ")
    message = []
    for i in text:
        message.append(i)
    print("le resultat est  : ")
    print(chiffrement(message,cles[0]))

main()
