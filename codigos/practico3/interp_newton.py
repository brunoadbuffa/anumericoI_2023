def inewton(x, y, z):
    c = dif_divididas(x, y)
    n = len(c)
	w = []  # Generamos una lista vacía donde almacenamos p(z_k)
    for k in z:
    	suma = c[0]
    	for i in range(1, n):
    		prod = 1
    		for j in range(i):
    			prod *= k - x[j]
    		suma += c[i] * prod    		
    	w.append(suma)
    
    return w
    
def test_inewton():
	x = [-2, 0, 2]
	y = [4, 0, 4]
	z = [-5, 1, 3]

	print(inewton(x, y, z))
	

    

