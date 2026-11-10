# labEserc6_2.py

def prodotto_scalare(a,b):
	if not isinstance(a, list) or not isinstance(b, list):
	    raise TypeError
	if len(a) != len(b):
	    raise ValueError
	if len(a) == 0:
	    raise ValueError
	
	res = 0
	for i in range(len(a)):
	    res += a[i] * b[i]
	return res