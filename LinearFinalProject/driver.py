"""Hannah Github ID: hhkim99"""
from sympy import *
from MatrixAlgebra import *
from Cryptography import *

print("-"*50)
print("Welcome to Hannah, Niharika, and Swetha's Linear Project")
print()
print("This program can handle the following characters: ")
print()
code1 = Cryptography("ABCDEFGHIJKLMNOPQRSTUVWXYZ!' ")
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ!' ")
print()

print("-"*50)

plaintext = "Hello Niharika"#"Don't Mine at Night!"
E = Matrix([[4,19],[13,10]])
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
print("-"*50)