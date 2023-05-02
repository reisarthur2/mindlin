#include <math.h>
#include <fstream>
#include <string>
#include "funcoescpp.h"
#include <iostream>

/*
notas:

descobrir por que ele tem 2x o periodo do seu
equivalente analitico para um mesmo epsilon

*/


using namespace std;
int main (int argc, char* argv[]) {
    if (argc != 12 or (stoi (argv[argc-1])==0)){
        cerr << "Uso: " << argv[0] << " <epslon> <precisao grafico> <bool> <bool> <bool> <bool> <bool> <bool>\n" << "encontrados " << argc << " parametros";
        return 1;
    }
    //sobre os parametros
    long double E = stof(argv[1]);
    long double amostras = stof(argv[2]);
    long double inferior = stof (argv[3]);
    long double superior = stof (argv[4]);

    long double precisao_grafico = (superior-inferior)/amostras;
    long double precisao_grafico_2 = precisao_grafico*0.5;


    //partes da saida que será dupla
    //[ 
    //  '[ [ [x1],[y1],nome1],[ [x2],[y2],nome2 ] ],' saida_!
    //  "[ [ [x3],[N3],nome3],[ [x4],[N4],nome4 ] ]"  saida_2
    //]
    string saida_1 = "";
    string saida_2 = "";
    //declaração de funcoes do caso, favor nao tocar no resto
    auto funcao_a = [E](long double y) -> long double{
        long double y_real = y/E - floor(y/E);
        return 
        y_real<=.25 ? (2) : (y_real>=.75 ? (2) : (3));
        ;};
    //aqui ^
    auto funcao_f = [](long double x) -> long double{
        return
        -1
        ;};
    auto funcao_F = [funcao_f](long double x) -> long double{
        return
        integral (funcao_f,x)
        ;};
    //constantes----------------------
    long double a_chapeu = 1/(integral([funcao_a](long double y) -> long double {return 1/funcao_a(y);}));
    
    //condicional para botar funcao_a******************
    if  (stoi (argv[10])){saida_2 = criador_grafico_json (saida_2,funcao_a,"a",superior,inferior,precisao_grafico);}
    //condicional para ver se algum u é usado
    if (stoi (argv[5]) or stoi (argv[6]) or stoi (argv[7]) or stoi(argv[9])){
        //sobre u0 ,du2/dx2 , du/dx--------------------------
        auto d2u0dx2 = [a_chapeu,funcao_f](long double x) -> long double {
            return funcao_f(x)/a_chapeu
            ;};
        long double constante_du0dx =  integral (funcao_F);
        auto du0dx = [a_chapeu,funcao_F,constante_du0dx](long double x) -> long double {
            return (funcao_F(x) - constante_du0dx)/a_chapeu
            ;};
        long double constante_u0 = constante_du0dx;
        auto u0 = [a_chapeu,funcao_F,constante_u0](long double x) -> long double{
            return integral ([a_chapeu,funcao_F,constante_u0](long double s) -> long double {
                return funcao_F(s)-constante_u0;}
                ,x)/a_chapeu
            ;};
        //condicional para por u0********************
        if (stoi(argv[5])){saida_1 = criador_grafico_json (saida_1,u0,"u0pn",superior,inferior,precisao_grafico);}
        //condicional para ver se u1 ou u2 é usado
        if (stoi (argv[6]) or stoi (argv[7]) or stoi(argv[9])){
            //sobre N1 e u1--------------------
            auto N1 = [E,a_chapeu,funcao_a](long double y) -> long double {
                long double y_real = y/E - floor(y/E);
                return integral ([a_chapeu,funcao_a](long double s) -> long double {
                    return a_chapeu/funcao_a(s) - 1;
                },y_real);
            };
            
            auto u1 = [N1,E,du0dx,u0](long double x) -> long double{
                return N1(x)*du0dx(x)*E+u0(x)
            ;};
            //condicional para por u1********************
            if (stoi(argv[6])){saida_1 = criador_grafico_json (saida_1,u1,"u1pn",superior,inferior,precisao_grafico);}
            //condicional para por N1********************
            if (stoi(argv[8])){saida_2 = criador_grafico_json (saida_2,N1,"N1pn",superior,inferior,precisao_grafico_2);}
            //condicional para ver se u2 é usado
            if (stoi(argv[7]) or stoi(argv[9])){
                //sobre N2 e u2-------------------
                long double constante_N2 = a_chapeu*integral (N1);
                
                auto N2 = [constante_N2,funcao_a,N1,E](long double y) -> long double {
                    long double y_real = y/E - floor(y/E);
                    return integral ([constante_N2,funcao_a,N1,E](long double s) -> long double {
                        return -N1(s) + constante_N2/funcao_a(s)
                        ;},y_real)
                    ;};

                auto u2 = [d2u0dx2,N2,N1,du0dx,u0,E](long double x) -> long double {
                    return d2u0dx2(x)*N2(x)*E*E+du0dx(x)*N1(x)*E+u0(x)
                    ;};
                
                //condicional para u2*********************
                if (stoi(argv[7])){saida_1 = criador_grafico_json (saida_1,u2,"u2pn",superior,inferior,precisao_grafico);}
                //condicional para N2*********************
                if (stoi(argv[9])){saida_2 = criador_grafico_json (saida_2,N2,"N2pn",superior,inferior,precisao_grafico_2);}
            }
        }
    }
    ofstream saida("./magia_cpp/saidas_e_executaveis/partes_aproximado_saida_dados.txt");
    saida << "[[" << saida_1 << "[[0],[0],\"sucesso\"]],[" << saida_2 << "[[0],[0],\"sucesso\"]]]";
    saida.close();
    return 1;
}
