#include <math.h>
#include <type_traits>
#include <fstream>
#include <string>

using namespace std;
template<typename T>
double integral(T funcao,  double limite_superior = 1, double limite_inferior = 0, int n = 1000) {
    long double dx = (limite_superior-limite_inferior)/n;
    long double integral = (funcao(limite_inferior) + funcao(limite_superior))/2.0;
    
    for (int i = 1; i < n; i++) {
        long double x = limite_inferior + i*dx;
        integral += funcao(x);
    }
    
    return static_cast<double>(integral*dx);
}

double derivada (double(*funcao)(double),double x,double dx=0.000001){
    return (funcao(x+dx)-funcao(x))/dx;
}
template<typename T>
string criador_grafico_json (string acumulador,T funcao,string nome,double limite_superior,double limite_inferior, double precisao_grafico){
    acumulador += "[[";
    for (double i=limite_inferior;i<limite_superior;i+=precisao_grafico){
        acumulador += to_string(i)+",";
    };
    acumulador = acumulador.substr(0,acumulador.length()-1) + "],[";
    for (double j=limite_inferior;j<limite_superior;j+=precisao_grafico){
        acumulador += to_string(funcao(j))+",";
    };
    acumulador = acumulador.substr(0,acumulador.length()-1) + "],\"" +nome +"\"],";
    return acumulador;
}