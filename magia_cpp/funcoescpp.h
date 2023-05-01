#include <math.h>
#include <type_traits>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
template<typename T>
long double integral(T funcao,  double limite_superior = 1, double limite_inferior = 0, int n = 1000) {
    long double dx = (limite_superior-limite_inferior)/n;
    long double integral = (funcao(limite_inferior) + funcao(limite_superior))/2.0;
    
    for (int i = 1; i < n; i++) {
        long double x = limite_inferior + i*dx;
        integral += funcao(x);
    }
    
    return integral*dx;
}

//template <typename T>
//long double integral(T funcao, double limite_superior = 1, double limite_inferior = 0, int n = 1500) {
//    long double h = (limite_superior - limite_inferior) / n;
//    long double x = limite_inferior + h;
//    long double soma1 = 0, soma2 = 0;
//    
//    for (int i = 1; i < n; i += 2) {
//        soma1 += funcao(x);
//        x += 2 * h;
//    }
//    
//    x = limite_inferior + 2 * h;
//    
//    for (int i = 2; i < n; i += 2) {
//        soma2 += funcao(x);
//        x += 2 * h;
//    }
//    
//    long double integral = h * (funcao(limite_inferior) + 4 * soma1 + 2 * soma2 + funcao(limite_superior)) / 3;
//    return integral;
//}



double derivada (double(*funcao)(double),double x,double dx=0.000001){
    return (funcao(x+dx)-funcao(x))/dx;
}

string num_str(long double num) {
    ostringstream out;
    out.precision(15);
    out << scientific << num;
    return out.str();
}

template<typename T>
string criador_grafico_json (string acumulador,T funcao,string nome,long double limite_superior,long double limite_inferior, long double precisao_grafico){
    acumulador += "[[";
    for (long double i=limite_inferior;i<=limite_superior;i+=precisao_grafico){
        acumulador += num_str(i)+",";
    };
    acumulador = acumulador.substr(0,acumulador.length()-1) + "],[";
    for (long double j=limite_inferior;j<=limite_superior;j+=precisao_grafico){
        acumulador += num_str(funcao(j))+",";
    };
    acumulador = acumulador.substr(0,acumulador.length()-1) + "],\"" +nome +"\"],";
    return acumulador;
}

