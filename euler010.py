import sympy
#Prime number below number n
#primeSummation(2001) should return 277050

def primeSummation(number):
	np = list(sympy.primerange(0, number))
	resultat = sum(np)
	return resultat

print(primeSummation(2001))