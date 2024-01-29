# Functions
import string

def encrypt(plaintext, key):
    newString = ''
    for s in str(plaintext):
        if s in string.printable:
            if key in range(95):
                orderS = (ord(s) + key)
                if orderS > 126:
                    wrapS = chr((ord(s) + key) % 95)
                    stringS = str(wrapS)
                    newString = newString + (stringS)
                else:
                    stringS = str(chr(orderS))
                    newString = newString + (stringS)
    
    return newString


def decrypt(ciphertext, key):
    newString = ''
    for s in str(ciphertext):
        if s in string.printable:
            if key in range(95):
                orderS = (ord(s) - key)
                if orderS < 32:
                    wrapS = chr(orderS + 95)
                    stringS = str(wrapS)
                    newString = newString + (stringS)
                else:
                    stringS = str(chr(orderS))
                    newString = newString + (stringS)
        
    return newString


def crack(ciphertext):
    newList = []
    i = 0
    for i in range(95):
        decryptC = [decrypt(ciphertext, i)]
        newList = newList + decryptC
        i = i + 1
    
    return newList

