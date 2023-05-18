#include <math.h>
#include <type_traits>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
/*

esse header pode ser modificado depois para outras
implementações gerais q serão usadas por outros codigos.

debates sobre integrais é aceito

talvez implementação usando ponteiros seja uma
saida válida para o futuro, caso seja necessário
maior eficiência, mas por agora não será feito por
dois motivos:

-não sei como usar ponteiros
-não há necessidade extrema no momento
-extra: já tentei otimizar esse código de mais e estou
        um pouco cansado, vou reservar minhas energias
        para as prioridades, tempo é finito e não sou
        (ainda) de ferro
        
*/



using namespace std;

//alguns tipos de integrais
//trapézios - perfeita para tudo
template<typename T>
long double integral(T funcao,  double limite_superior = 1, double limite_inferior = 0, int n = 1500) {
    long double dx = (limite_superior-limite_inferior)/n;
    long double integral = (funcao(limite_inferior) + funcao(limite_superior))/2.0;
    
    for (int i = 1; i < n; i++) {
        long double x = limite_inferior + i*dx;
        integral += funcao(x);
    }
    
    return integral*dx;
}

//quadratura de gauss - tem problemas serios com integrais duplas
//template<typename T>
//long double integral(T funcao, double limite_superior = 1, double limite_inferior = 0, int quadratura = 100) {
//    // Vetores de pesos e raízes de Legendre
//    double pesos[quadratura] = {0};
//    double raizes[quadratura] = {0};
//
//    // Inicialização dos pesos e raízes
//    for (int i = 1; i <= quadratura; i++) {
//        double xi = cos(M_PI * (i - 0.25) / (quadratura + 0.5));
//        double p1 = 1, p2 = xi;
//        for (int j = 2; j <= quadratura; j++) {
//            double p3 = ((2 * j - 1) * xi * p2 - (j - 1) * p1) / j;
//            p1 = p2;
//            p2 = p3;
//        }
//        double pd = quadratura * (xi * p2 - p1) / (xi * xi - 1);
//        raizes[i - 1] = xi;
//        pesos[i - 1] = 1 / ((1 - xi * xi) * pd * pd);
//    }
//
//    // Cálculo da integral
//    long double soma = 0;
//    for (int i = 0; i < quadratura; i++) {
//        double xi = raizes[i];
//        double peso = pesos[i];
//        double x = 0.5 * (limite_superior - limite_inferior) * xi + 0.5 * (limite_superior + limite_inferior);
//        soma += peso * funcao(x);
//    }
//    return soma * 0.5 * (limite_superior - limite_inferior);
//}

//de simpsoms - lentinha
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

template<typename T>
long double integral_dupla(T funcao,  double limite_superior = 1, double limite_inferior = 0, double dx = 0.0001) {
    double atualx = limite_inferior;
    double iterador = (limite_superior-limite_inferior)/dx + 1.0;
    double acumulador = 0;
    while (atualx<=limite_superior){
        acumulador += iterador*funcao (atualx);
        iterador-=1;
        atualx+=dx;
    }
    return acumulador*dx*dx;

}
template<typename T>
double derivada (T funcao,double x,double dx=0.000001){
    return (funcao(x+dx)-funcao(x))/dx>1000 ;
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
    for (long double i=limite_inferior;i<=limite_superior+precisao_grafico;i+=precisao_grafico){
        acumulador += num_str(i)+",";
    };
    acumulador = acumulador.substr(0,acumulador.length()-1) + "],[";
    for (long double j=limite_inferior;j<=limite_superior+precisao_grafico;j+=precisao_grafico){
        acumulador += num_str(funcao(j))+",";
    };
    acumulador = acumulador.substr(0,acumulador.length()-1) + "],\"" +nome +"\"],";
    return acumulador;
}
template<typename T>
pair<vector<long double>, vector<long double>> fourier_coeficientes(T funcao_imitada, int numero_senoides = 100) {
    vector<long double> indice(numero_senoides + 1);
    for (int i = 0; i <= numero_senoides; i++) {
        indice[i] = i;
    }
    vector<long double> coeficientes_cos(numero_senoides + 1);
    vector<long double> coeficientes_sin(numero_senoides + 1);
    for (int i = 0; i <= numero_senoides; i++) {
        long double x = indice[i];
        coeficientes_cos[i] = 2 * integral([&](long double y){ return funcao_imitada(y) * cos(2 * M_PI * y * x); });
        coeficientes_sin[i] = 2 * integral([&](long double y){ return funcao_imitada(y) * sin(2 * M_PI * y * x); });
    }
    return {coeficientes_cos, coeficientes_sin};
};

double transformada_fourier(pair<vector<long double>, vector<long double>> coeficientes, double ponto) {
    int tamanho = coeficientes.first.size();
    vector<double> indice(tamanho + 1);
    for (int i = 0; i <= tamanho; i++) {
        indice[i] = i;
    }
    double an = coeficientes.first[0] / 2;
    for (int i = 1; i < tamanho; i++) {
        double bn = coeficientes.second[i];
        double n = indice[i];
        an += (coeficientes.first[i] * cos(n * 2 * M_PI * ponto) + bn * sin(n * 2 * M_PI * ponto));
    }
    return an;
}