#Caesar Encrytion Function
def caesarEncry(a , plainText ,out):
    f = open(out, "w")
    
    cipherText = ""
    for i in range(len(plainText)):
        alpha = plainText[i]
        #Encrypt uppercase characters 
        if(alpha.isupper()):
            if(alpha != ' '):
                alpha = chr(int(ord(alpha) + int(a) - ord('A')) % 26 + ord('A'))
                cipherText += alpha
            else:
                cipherText += alpha
        #Encrypt lowercase characters        
        else:
            if(alpha != ' '):
                alpha = chr(int(ord(alpha) + int(a) - ord('a')) % 26 + ord('a'))
                cipherText += alpha
            else:
                cipherText += alpha
    #print("\nCipher Text by Caesar: " + cipherText + "\n")
    f.write("Cipher Text by Caesar: " + cipherText + "\n")
    f.close()

#Caesar Decryption Function
def caesarDecry(a , cipherText , out):
    f = open(out, "w")
    
    plainText = ""
    for i in range(len(cipherText)):
        alpha = cipherText[i]
        #Decrypt uppercase characters
        if(alpha.isupper()):
            if(alpha != ' '):
                alpha = chr(int(ord(alpha) - int(a) - ord('A')) % 26 + ord('A'))
                plainText += alpha
            else:
                plainText += alpha
        #Decrypt lowercase characters
        else:
            if(alpha != ' '):
                alpha = chr(int(ord(alpha) - int(a) - ord('a') + 26) % 26 + ord('a'))
                plainText += alpha
            else:
                plainText += alpha
    #print("\nDecrypted Text by Caesar: " + plainText + "\n")
    f.write("Decrypted Text by Caesar: " + plainText + "\n")
    f.close()

#Affine Encryption Function
def affineEncry(a , b , plainText , out):
    f = open(out, "w")
    
    cipherText = ""
    for i in range(len(plainText)):
        alpha = plainText[i]
        #Encrypt uppercase characters
        if(alpha.isupper()):
            if(alpha != ' '):
                alpha = chr(((int(a) * (ord(alpha) - ord('A'))) + int(b)) % 26 + ord('A'))
                cipherText += alpha
            else:
                cipherText += alpha
        #Encrypt lowercase characters
        else:
            if(alpha != ' '):
                alpha = chr(((int(a) * (ord(alpha) - ord('a'))) + int(b)) % 26 + ord('a'))
                cipherText += alpha
            else:
                cipherText += alpha
    #print("\nCipher Text by Affine: " + cipherText + "\n")
    f.write("Cipher Text by Affine: " + cipherText + "\n")
    f.close()

#Affine Decryption Function
def affineDecry(a , b , cipherText , out):
    f = open(out, "w")
    
    plainText = ""
    a_inv = 0
    flag = 0
    #Finding multiplicative inverse of a
    for j in range(26):
        flag = (a * j) % 26
        if(flag == 1):
            a_inv = j

    for i in range(len(cipherText)):
        alpha = cipherText[i]
        #Decrypt uppercase letters
        if(alpha.isupper()):
            if(alpha != ' '):
                alpha = chr((int(a_inv) * (ord(alpha) + ord('A') - int(b))) % 26 + ord('A'))
                plainText += alpha
            else:
                plainText += alpha
        else:
            if(alpha != ' '):
                alpha = chr((int(a_inv) * (ord(alpha) - ord('a') - int(b) + 26)) % 26 + ord('a'))
                plainText += alpha
            else:
                plainText += alpha
    #print("\nDecrypted Text by Affine: " + plainText + "\n")
    f.write("Decrypted Text by Affine: " + plainText + "\n")
    f.close()

#Key generation in  a cyclic manner Function
def generateKey(key , text):
    key = list(key) 
    if len(text) == len(key):
        key =  map(str.upper,key)
        return(key) 
    else: 
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    key =  map(str.upper,key)
    return("" . join(key))

#Vigenere Encryption Function with the help of the key generated
def vigenereEncry(key , plainText , out):
    f = open(out, "w")
    
    cipherText = ""
    for i in range(len(plainText)):
        alpha = plainText[i]
        #Encrypt uppercase characters
        if(alpha.isupper()):
            if(alpha != ' '):
                alpha = chr((ord(plainText[i]) + ord(key[i])) % 26 + ord('A'))
                cipherText += alpha
            else:
                cipherText += alpha
        #Encrypt lowercase characters
        else:
            if(alpha != ' '):
                #alpha = chr(((ord(plainText[i]) + ord(key[i % len(key)]))) % 26 + ord('a'))
                base = ord('a')
                index = ((ord(key[i % len(key)].lower()) - base) + (ord(plainText[i]) - base)) % 26
                alpha = chr(base + index)
                cipherText += alpha
               # p = ord(plainText[i])- ord('a')
               # k = ord(key[i % len(key)]) - ord('a')
               # c = (p + k) % 26 
               # cipherText = cipherText + chr(c + ord('a'))
            else:
                cipherText += alpha
                
    #print("\nCipher Text by Vigenere: " + cipherText + "\n")
    f.write("Cipher Text by Vigenere: " + cipherText + "\n")
    f.close()
    

#Vigenere Decryption Function
def vigenereDecry(key , cipherText , out):
    f = open(out, "w")
    
    plainText = ""
    for i in range(len(cipherText)):
        alpha = cipherText[i]
        #Decrypt uppercase characters
        if(alpha.isupper()):
            if(alpha != ' '):
                alpha = chr((ord(cipherText[i]) - ord(key[i]) + 26) % 26 + ord('A'))
                plainText += alpha
            else:
                plainText += alpha
        else:
            if(alpha != ' '):
                #alpha = chr((ord(cipherText[i]) - ord(key[i])) % 26 + ord('a'))
                base = ord('a')
                index = ((ord(key[i % len(key)].lower()) - base) - (ord(cipherText[i]) - base)) % 26
                alpha = chr(base + index)
                plainText += alpha
            else:
                plainText += alpha
    #print("\nDecrypted Text by Vigenere: " + plainText + "\n")
    f.write("Decrypted Text by Vigenere: " + plainText + "\n")
    f.close()

import sys

#Cipher Function
def cipher(cipherType , enc_dec , inputFile , outputFile , listKeys):
    f = open(inputFile , 'r')
    text = f.read()
    f.close()
    #If operation type is Encryption
    if(enc_dec == "enc"):

        #if cipher type is Caesar "Shift" cipher
        if(cipherType == "shift"):
            A = map(int, listKeys.strip('[]').split(','))
            caesarEncry(A[0] , text , outputFile)

        #if cipher type is Affine cipher
        elif(cipherType == "affine"):
            A = map(int, listKeys.strip('[]').split(','))
            affineEncry(A[0] , A[1] , text , outputFile)

        #if cipher type is Vigenere cipher
        elif(cipherType == "vigenere"):
            key = generateKey(listKeys , text)
            vigenereEncry(key , text , outputFile)
        else:
            print("Invalid Cipher!\n")

    #if operation type is Decryption        
    elif(enc_dec == "dec"):

        #if cipher type is Caesar "Shift" cipher
        if(cipherType == "shift"):
            A = map(int, listKeys.strip('[]').split(','))
            caesarDecry(A[0] , text , outputFile)

        #if cipher type is Affine cipher
        elif(cipherType == "affine"):
            A = map(int, listKeys.strip('[]').split(','))
            affineDecry(A[0], A[1] , text , outputFile)

        #if cipher type is Vigenere cipher
        elif(cipherType == "vigenere"):
            key = generateKey(listKeys , text)
            vigenereDecry(key , text , outputFile)
        else:
            print("Invalid Cipher!\n")
    else:
        print("Invalid Operation!\n")

if __name__ == "__main__":
    cipher(*sys.argv[1:])
                
            
