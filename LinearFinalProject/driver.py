"""Hannah Github ID: hhkim99"""
"""Niharika Github: niharikavattikonda"""
from sympy import *
from MatrixAlgebra import *
from Cryptography import *

print("*"*75)
print("Welcome to Hannah, Niharika, and Swetha's Linear Project")
print()
print("This program can handle the following characters: ")
print()
code1 = Cryptography("ABCDEFGHIJKLMNOPQRSTUVWXYZ!' ")
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ!' ")
print()

print("*"*50)

"""FOR USE DURING PRESENTATION"""
"""ENCRYPTION SIDE"""

"""TEAM 1"""
team1plain = "Hello '!" ##team 1 creates this message for team 2 to break
team1encryption = Matrix([[22,23],[28,2]]) ##we give them an encryption matrix
team1ciphertext = encrypt(team1encryption, team1plain, code1) ###this is team 1's encrypted message
print("'%s' encodes as '%s'" % (team1plain, team1ciphertext)) ###print check
print(" using encryption matrix") #### print check
pprint(team1encryption) ###printing out that matrix just for checking

"""TEAM 2"""
team2plain = "Tes ti'ng!" ##team 2 creates this message for team 1 to break
team2encryption = Matrix([[3,9],[27,9]]) ##we give them an encryption matrix
team2ciphertext = encrypt(team2encryption, team2plain, code1) ###this is team 2's encrypted message
print("'%s' encodes as '%s'" % (team2plain, team2ciphertext)) ###print check
print(" using encryption matrix") #### print check
pprint(team2encryption) ###printing out that matrix just for checking

print("-"*50)

"""DECRYPTION TIME"""
"""TEAM 1's decoding section - used to check team 2's work"""
team1decryption = team1encryption.inv_mod(code1.m)
print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1decryption,team1ciphertext, code1)))
#print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1encryption.inv_mod(code1.m),team1ciphertext, code1)))
print("Using decryption matrix:")
pprint(team1decryption) ###Matrix([[26,20],[13,25]])
#pprint(team1encryption.inv_mod(code1.m))

"""TEAM 2's decoding section - used to check team 1's work"""
team2decryption = team2encryption.inv_mod(code1.m)
print("And %s decrypts to %s" % (team2ciphertext, decrypt(team2decryption,team2ciphertext, code1)))
#print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1encryption.inv_mod(code1.m),team1ciphertext, code1)))
print("Using decryption matrix:")
pprint(team2decryption) ###Matrix([[6,23],[11,2]])


"""*****************************************"""
"""Created Ahead of Time for Class:"""

"""ENCRYPTION EXAMPLE:"""
"""
encryptionMessage = "OHHSUGAR"
encryptMatrix = Matrix([[7,12],[9,13]])
cryptedText = encrypt(encryptMatrix, encryptionMessage, code1)
print("'%s' encodes as '%s'" % (encryptionMessage, cryptedText))
print("  using encryption matrix")
pprint(encryptMatrix)
print("And %s decrypts to %s" % (cryptedText, decrypt(encryptMatrix.inv_mod(code1.m),cryptedText, code1)))

print("-"*50)
"""
"""DECRYPTION EXAMPLE WALKTHROUGH"""
"""Encryption Matrix used: ([21,13],[9,14]) """
"""Decryption Matrix used: ([24,15],[26,7]) """
"""Encrypted Text yielded: KPSW!LVJ'NXZZDPD'CJU """
"""
messageForClass = "BRING BACK THE FLUX!"
encryptionMatrix = Matrix([[21,13],[9,14]])
print("Encryption Matrix")
pprint(encryptionMatrix)
encryptedText = encrypt(encryptionMatrix, messageForClass, code1)
print("Encrypted Text: '%s'" % (encryptedText))

print("-"*20)

decryptionMatrix = encryptionMatrix.inv_mod(code1.m)
print("Decryption Matrix")
pprint(decryptionMatrix)
decryptedText = decrypt(encryptionMatrix.inv_mod(code1.m),encryptedText, code1)
print("Decrypted Text: '%s'" % (decryptedText))
"""


"""*****************************************"""
"""TEST PROGRAM
plaintext = "Hello Niharika"
E = Matrix([[7,12],[9,13]])
ciphertext = encrypt(E, plaintext, code1)
print("'%s' encodes as '%s'" % (plaintext, ciphertext))
print("  using encryption matrix")
pprint(E)
print("And %s decrypts to %s" % (ciphertext, decrypt(E.inv_mod(code1.m),ciphertext, code1)))

newEncryptMe = "Hannah is cool"
encryptM = get_random_invertible_matrix(len(code1.alphabet))
encryptedText = encrypt(encryptM, newEncryptMe, code1)
print("'%s' encodes as '%s'" % (newEncryptMe, encryptedText))
print(" using encryption matrix")
pprint(encryptM)
print("And %s decrypts to %s" % (encryptedText, decrypt(encryptM.inv_mod(code1.m),encryptedText, code1)))
print("Using decryption matrix:")
pprint(encryptM.inv_mod(code1.m))
print("-"*50)
"""