# labEserc6.1.py

def somma_liste(a,b):
	if  not isinstance(a, list) or not isinstance(b, list):
	    raise TypeError
	if len(a) != len(b):
	    raise ValueError
	for x in a:
	    if not isinstance(x, int):
	        raise TypeError
	for x in b:
	    if not isinstance(x, int):
	        raise TypeError
	res = []
	for i in range(len(a)):
	    res.append(a[i] + b[i])
	return res