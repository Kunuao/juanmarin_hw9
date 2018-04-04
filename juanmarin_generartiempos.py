import numpy as np 
import time 
#declaracion de la funcion recursiva de fibonacci
def fibonacci(N): 
	if (N == 1 or N == 0): 
		return  1 
	else: 
		return fibonacci(N-1) + fibonacci(N-2) 
#funcion que calcula el tiempo para un N 
def get_time(N): 
	t0= time.time()
	r = fibonacci(N)
	t1 = time.time() - t0
	return t1 

#imprime la funcion
def imprime(N):
	i = 0;  
	while (i<N):
		print fibonacci(N), get_time(N)
		i = i+1


imprime(35)

