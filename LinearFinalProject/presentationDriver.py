"""FOR USE DURING PRESENTATION"""
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
"""WITH I/O"""
###publish team 1's encryption matrix
team1encryption = Matrix([[22,23],[28,2]]) ##we give them an encryption matrix
print("TEAM 1: ")
pprint(team1encryption) ###printing out that matrix just for checking

###publish team 2's encryption matrix
print("TEAM 2: ")
ioInput = "start"
while (ioInput != "end"):
	###ask for which team's message
	choice = raw_input("Which team would you like to process (1/2)")
	if choice == 1:
		###if team 1:
		team1plain = raw_input("What is Team 1's plaintext message? ")
		###ask for team 1's original message
		if team1plain.length%2 != 0:
			team1plain = team1plain+"X"
		###test that it is even-length
		if team1plain.length%2 == 0:
			###if yes, ask to run the encryption
			team1ciphertext = encrypt(team1encryption, team1plain, code1) ###this is team 1's encrypted message
			###print the encrypted text
			print("'%s' encodes as '%s'" % (team1plain, team1ciphertext)) ###print check
			print(" using encryption matrix") #### print check
			pprint(team1encryption) ###printing out that matrix just for checking
			###print the decrypted text
			team1decryption = team1encryption.inv_mod(code1.m)
			print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1decryption,team1ciphertext, code1)))
			#print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1encryption.inv_mod(code1.m),team1ciphertext, code1)))
			print("Using decryption matrix:")
			pprint(team1decryption) ###Matrix([[26,20],[13,25]])
			#pprint(team1encryption.inv_mod(code1.m))

			###ask to loop back for another team's message
			forkPoint = raw_input("Do you want to check another team?(yes/no)")
			if forkPoint == "yes":
				pass
			if forkPoint == "no":
				break
				###if no, then ask to quit the program

	if choice == 2:
		pass
		###if team 2:
		###ask for team 2's message
		###test that it is even-length
		###if yes, ask to run the encryption
		###print the encrypted text
		###print the decrypted text
		###ask to loop back for another team's message
		###if no, then ask to quit the program

###BACKUP - NO I/O


###ENCRYPTION SIDE

###TEAM 1
"""
team1plain = "Hello '!" ##team 1 creates this message for team 2 to break
team1encryption = Matrix([[22,23],[28,2]]) ##we give them an encryption matrix
team1ciphertext = encrypt(team1encryption, team1plain, code1) ###this is team 1's encrypted message
print("'%s' encodes as '%s'" % (team1plain, team1ciphertext)) ###print check
print(" using encryption matrix") #### print check
pprint(team1encryption) ###printing out that matrix just for checking
"""
###TEAM 2
"""
team2plain = "Tes ti'ng!" ##team 2 creates this message for team 1 to break
team2encryption = Matrix([[3,9],[27,9]]) ##we give them an encryption matrix
team2ciphertext = encrypt(team2encryption, team2plain, code1) ###this is team 2's encrypted message
print("'%s' encodes as '%s'" % (team2plain, team2ciphertext)) ###print check
print(" using encryption matrix") #### print check
pprint(team2encryption) ###printing out that matrix just for checking

print("-"*50)
"""
###DECRYPTION TIME
###TEAM 1's decoding section - used to check team 2's work
"""
team1decryption = team1encryption.inv_mod(code1.m)
print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1decryption,team1ciphertext, code1)))
#print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1encryption.inv_mod(code1.m),team1ciphertext, code1)))
print("Using decryption matrix:")
pprint(team1decryption) ###Matrix([[26,20],[13,25]])
#pprint(team1encryption.inv_mod(code1.m))
"""
###TEAM 2's decoding section - used to check team 1's work
"""
team2decryption = team2encryption.inv_mod(code1.m)
print("And %s decrypts to %s" % (team2ciphertext, decrypt(team2decryption,team2ciphertext, code1)))
#print("And %s decrypts to %s" % (team1ciphertext, decrypt(team1encryption.inv_mod(code1.m),team1ciphertext, code1)))
print("Using decryption matrix:")
pprint(team2decryption) ###Matrix([[6,23],[11,2]])
"""