# labEserc6_3.py

def media(a):
	somma = 0
	for x in a:
		somma += x
	return somma/len(a)

def separa_elementi(a):
	if not isinstance(a, list):
	    raise TypeError
	for x in a:
	    if not isinstance(x, (int, float)):
	        raise TypeError
	
	if len(a) == 0:
	    return [], []
	magg = []
	min_eq = []
	med = media(a)

	for x in a:
	    if x > med:
	        magg.append(x)
	    else:
	        min_eq.append(x)
	return magg, min_eq