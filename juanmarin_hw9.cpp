#include <iostream>
#include <ctime>


//declaracion de funciones
float fibonacci(float N); 
float get_time(float N);
//codigo de funcion recursiva para fibonacci
float fibonacci(float N){
	if (N == 0 || N == 1){
		return 1;
} 
	else{
		return fibonacci(N-1) + fibonacci(N-2);
		
}

}
// funcion que calcula el tiempo para un N
float get_time(float N){
	
	clock_t t;
	t = clock();
	float Fun = fibonacci(N);
	t = clock() - t ;
	float time = ((float)t)/CLOCKS_PER_SEC;
	return time;
	
}
// ejecucion del codigo metodo main para un N de 45
int main(){

int N= 45; 
int i = 0; 
while (i<N){
	std::cout << fibonacci(i) << "," << get_time(i)<< "\n"; 

	i = i + 1;

}




}
