from Project2_Functions import *

done = False
while not done: 
    Method = input("(E)ncryption, (D)ecryption, (C)rack, or e(X)it?: ")
    for c in Method:
        if c == 'E' or c == 'e':
            plaintext = input('Enter the message you wish to encrypt: ')
            key = int(input('Enter the key to use for encryption (0-94): '))
            print('The encrypted message is: ' + encrypt(plaintext, key))
        elif c == 'D' or c == 'd':
            ciphertext = input('Enter the message you wish to decrypt: ')
            key = int(input('Enter the key to use for decryption (0-94): '))
            print('The decrypted message is: ' + decrypt(ciphertext, key))
        elif c == 'C' or c == 'c':
            ciphertext = input('Enter the ciphertext you wish to crack: ')
            print('Printing decryption with all possible keys...')
            cipherList = crack(ciphertext)
            for i in range(95):
                print('key: ' + str(i) + ' :: plaintext: ' + cipherList[i])
        elif c == 'X' or c == 'x':
            done = True
            print('End of program.')
        else:
            print(str('Invalid menu selection. Try again.'))


