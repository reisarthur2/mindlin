#include <math.h>
#include <type_traits>
#include <fstream>
#include <string>

using namespace std;
template<typename T>
double integral(T funcao,  double limite_superior = 1, double limite_inferior = 0, int n = 1000) {
    double dx = (limite_superior-limite_inferior)/n;
    double integral = (funcao(limite_inferior) + funcao(limite_superior))/2.0;
    
    for (int i = 1; i < n; i++) {
        double x = limite_inferior + i*dx;
        integral += funcao(x);
    }
    
    return integral*dx;
}

double derivada (double(*funcao)(double),double x,double dx=0.000001){
    return (funcao(x+dx)-funcao(x))/dx;
}

