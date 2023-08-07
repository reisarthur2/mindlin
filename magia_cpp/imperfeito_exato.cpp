#include <math.h>
#include <fstream>
#include <string>
#include "funcoescpp.h"
#include <iostream>
#include <iomanip> // Para std::setprecision
#include <sstream>
/*
notas:

parece certo

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
    long double beta = stof (argv[5]);
    
    long double precisao_grafico = (superior-inferior)/amostras;

    //declaração de funcoes do caso, favor nao tocar no resto
    long double ponto_descontinuo = 0.25;
    auto funcao_a = [](double x) -> double{
        long double y_real = x - floor(x);
        return y_real<=.25 ? (5) : (y_real>=.75 ? 5 : 10);
    };
    //aqui ^
    auto funcao_f = [E](double x) -> double{
        return
        1;
    };
    //aqui ^
    //----------------------------------------------------
    auto funcao_F = [E,funcao_f](double x) -> double{
        return integral (funcao_f,x)
        ;
    };
    auto descontinuidades = [ponto_descontinuo,E,beta,funcao_F](long double x,long double c) -> long double {
        long double x_acum = ponto_descontinuo*E;
        long double resultado = 0.0;
        long double passadas = 0.0;
        while (x_acum<x){
            resultado += funcao_F(x_acum);
            passadas += 1.0;
            x_acum += (E*0.5);

        };

        return ((resultado+c*passadas)/beta)*E;};
    //constantes
    long double c0 = -(integral([funcao_F,funcao_a,E](double s) -> double {
        return funcao_F(s)/funcao_a(s/E);
    }) + descontinuidades(1,0))/(integral([funcao_a,E](double s)->double{return 1.0/funcao_a(s/E);})+E*(2/E)/beta) ;
    
    auto ue = [c0,funcao_F,funcao_a,descontinuidades,E](double x)->double{
        return -integral ([funcao_F,funcao_a,c0,E](double s)->double{
            return (funcao_F(s)+c0)/funcao_a(s/E) ;
            },x) - descontinuidades (x,c0);
    };
    float numero_saidab = beta;
    float numero_saidae = E;
    ostringstream stream;
    stream << fixed <<  setprecision(0) << numero_saidab;
    ostringstream stream2;
    stream2 << fixed <<  setprecision(3) << numero_saidae;
    string result = "ue, beta=" + stream.str()+",E=" + stream2.str();
    string auxiliar_saida = "";
    auxiliar_saida += criador_grafico_json (auxiliar_saida,ue,result,superior,inferior,precisao_grafico);
    
    ofstream saida("./magia_cpp/saidas_e_executaveis/imperfeito_exato_saida_dados.txt");
    saida << auxiliar_saida.substr(0,auxiliar_saida.length()-1);
    saida.close();

    return 0;
}
