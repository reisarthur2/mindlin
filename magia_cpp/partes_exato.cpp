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

    long double E = stof(argv[1]);
    long double amostras = stof(argv[2]);
    long double inferior = stof (argv[3]);
    long double superior = stof (argv[4]);

    long double precisao_grafico = (superior-inferior)/amostras;


    //declaração de funcoes do caso, favor nao tocar no resto
    auto funcao_a = [E](double y) -> double{
        long double y_real = y/E - floor(y/E);
        return y_real<=.25 ? (2) : (y_real>=.75 ? (2) : (3));
    };
    //aqui ^
    auto funcao_x = [E](double x) -> double{
        return
        -1;
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
    string auxiliar_saida = "";
    auxiliar_saida += criador_grafico_json (auxiliar_saida,ue,"ue",superior,inferior,precisao_grafico);
    
    ofstream saida("./magia_cpp/partes_exato_saida_dados.txt");
    saida << auxiliar_saida.substr(0,auxiliar_saida.length()-1);
    saida.close();

    return 0;
}
