from Cryptography import *
from sympy import *
from random import randint 

def encrypt(E,p,a): ###matrix E is encryption matrix,string p is plaintext, mod 26.Return an encrypted string, alphabet A
	return a.MtoS(matrix_mod(E*a.StoM(p), len(a.alphabet)))
def decrypt(D,c,a): ###matrix D is decryption matrix, string c is ciphertext, mod 26. Return decrypted string, alphabet A
	return a.MtoS(matrix_mod(D*a.StoM(c),len(a.alphabet)))
def get_decryption_matrix(P,C,a): ###Knowing two digraphs in string P are encoded as string C, determine a unique decryption matrix, alphabet a
	pdione = P[:2] #first plain digraph - letters string
	pditwo = P[2:] #second plain digraph - letters string
	cdione = C[:2] #first cipher digraph - letters string
	cditwo = C[2:] #second cipher digraph - letters string
	pdioneN = a.stoa(pdione) #make letters into numbers list
	pditwoN = a.stoa(pditwo) #make letters into numbers list
	cdioneN = a.stoa(cdione) #make letters into numbers list
	cditwoN = a.stoa(cditwo) #make letters into numbers list

	plainmatrixnums = Matrix([[pdioneN[0],pditwoN[0]],[pdioneN[1],pditwoN[1]]]) #plaintext number matrix P
	ciphermatrixnums = Matrix([[cdioneN[0],cditwoN[0]],[cdioneN[1],cditwoN[1]]])#ciphertext number matrix C
	cipherinverse = ciphermatrixnums.inv_mod(len(a.alphabet)) #find inverse of the cipher matrix
	d = plainmatrixnums*cipherinverse #multiply plain with the cipher inverse to get d
	dModed = Matrix([
		[(d[0,0]%len(a.alphabet)), (d[0,1]%len(a.alphabet))],
		[(d[1,0]%len(a.alphabet)), (d[1,1]%len(a.alphabet))]
	])
	return dModed

def get_random_invertible_matrix(m): ###return a random 2x2 matrix M with gcd(det(M),m) = 1
	d = 2
	M = Matrix([[0,0],[0,0]])
	while d>1:
		M = Matrix([[randint(0,m),randint(0,m)],[randint(0,m),randint(0,m)]]) #make a random 2x2 matrix, M, and let d = gcd(M, m)
		d = gcd(det(M),m) #range is 1 to m-1 -> your modulus value is the top
		#if the gcd is not 1- no invertible matrix
	return M