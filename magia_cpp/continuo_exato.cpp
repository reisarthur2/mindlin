#include <math.h>
#include <fstream>
#include <string>
#include "funcoescpp.h"
#include <iostream>

/*
notas:

esse arquivo é a base para o resto, ele pode ser modificado
a posteriori, mas por agora está ok


*/


using namespace std;
int main (int argc, char* argv[]) {
    if (argc < 3){
        cerr << "Uso: " << argv[0] << " <epslon> <precisao grafico>\n";
        return 1;
    }

    float E = stof(argv[1]);
    float precisao_grafico = stof(argv[2]);
    float inferior = stof (argv[3]);
    float superior = stof (argv[4]);
    //declaração de funcoes do caso, favor nao tocar no resto
    auto funcao_a = [E](double x) -> double{
        return 
        1+0.25*cos(2*M_PI*x/E);
        };
    //aqui ^
    auto funcao_x = [E](double x) -> double{
        return
        x;
    };
    //aqui ^
    //----------------------------------------------------
    auto funcao_F = [E,funcao_x](double x) -> double{
        return integral (funcao_x,x)
        ;
    };
    //constantes
    double a_chapeu = 1/(integral([funcao_a](double y) -> double {return 1/funcao_a(y);}));
    double parte_constante = a_chapeu*integral([funcao_a,funcao_F](double t) -> double {return funcao_F(t)/funcao_a(t);});
    
    auto ue = [parte_constante,funcao_a,funcao_F](double x) -> double {
        return integral (([parte_constante,funcao_a,funcao_F](double s) -> double {
            return (funcao_F(s)-parte_constante)/funcao_a(s);
            }),x);
        };

    
    ofstream saida("./magia_cpp/continuo_exato_saida_dados.txt");
    saida << "[[";
    for (float i=inferior;i<superior;i+=precisao_grafico){
        saida << to_string(i)+",";
    };
    saida << "0.0],[";
    for (float j=inferior;j<superior;j+=precisao_grafico){
        saida << to_string(ue(j))+",";
    };
    saida << "0.0]]";
    saida.close();

    return 0;
}
