def dif_divididas(x, y):
    n = len(x)
    coefs = []
    # Genero filas de coefs
    for i in range(n):
        coefs.append(y[:n - i].copy())
    
    # Calculo coeficientes de diferencias divididas
    for i in range(1, n):
        for j in range(n - i):
            (coefs[i])[j] = ((coefs[i-1])[j+1] - (coefs[i-1])[j])
            (coefs[i])[j] = (coefs[i])[j] / (x[j + i] - x[j])
    

    # Genero vector de coeficientes del polinomio
    c = [x[0] for x in coefs]
    return c, coefs #Nos guardamos el los vectores de coefs de diferencias divididas solo para chequear!

def test_dif_divididas():
    # Este es el conjunto de datos del teórico, debería darnos lo mismo.
    x = [3, 1, 5, 6]
    y = [1, -3, 2, 4]
    print(dif_divididas(x, y))

# Para poder terminar el ejercicio, es necesario generar la función
# inewton que calcule diferencias divididas y luego evalúe el polinomio
# con el esquema del teórico.

    
    
def inewton(x, y, z):
    c = dif_divididas(x, y)
    n = len(c)
	w = []  # Generamos una lista vacía donde almacenamos p(z_k)
    for k in z:
    	suma = c[0] # -> PENSAR: cómo sería si partimos de "suma = 0"
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

# Ejecutar test_inewton debería devolvernos la lista [25, 1, 9]
# test_inewton()
    
