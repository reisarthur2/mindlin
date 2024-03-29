#include <math.h>
#include <fstream>
#include <string>
#include "funcoescpp.h"
#include <iostream>

/*
notas:

pensar em alguma forma de deixar a integral de N2 mais leve para integrais numéricas (possivel implementar a função integral dupla)

*/


using namespace std;
int main (int argc, char* argv[]) {
    if (argc != 13 or (stoi (argv[argc-1])==0)){
        cerr << "Uso: " << argv[0] << " <epslon> <precisao grafico> <bool> <bool> <bool> <bool> <bool> <bool>\n" << "encontrados " << argc << " parametros";
        return 1;
    }
    //sobre os parametros
    long double E = stof(argv[1]);
    long double amostras = stof(argv[2]);
    long double inferior = stof (argv[3]);
    long double superior = stof (argv[4]);
    long double beta = stof (argv[12]);

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
    auto funcao_a = [](long double y) -> long double{
        long double y_real = y - floor(y);
        return 
        y_real<=.25 ? (5) : (y_real>=.75 ? 5 : 10)
        ;};
    //aqui ^
    auto funcao_f = [](long double x) -> long double{
        return
        1
        ;};
    auto funcao_F = [funcao_f](long double x) -> long double{
        return
        x
        ;};
    //constantes----------------------
    long double a_chapeu = 1.0/((integral([funcao_a,E](long double y) -> long double {return 1.0/funcao_a(y);}))+1/beta+1/beta);
    
    //condicional para botar funcao_a******************
    if  (stoi (argv[10])){saida_2 = criador_grafico_json (saida_2,funcao_a,"a_imperfeito",superior/E,inferior/E,precisao_grafico);}
    //condicional para ver se algum u é usado
    if (stoi (argv[5]) or stoi (argv[6]) or stoi (argv[7]) or stoi(argv[9])){
        //sobre u0 ,du2/dx2 , du/dx--------------------------
        auto d2u0dx2 = [a_chapeu,funcao_f](long double x) -> long double {
            return -funcao_f(x)/a_chapeu
            ;};
        long double constante_du0dx =  integral (funcao_F);
        auto du0dx = [a_chapeu,funcao_F,constante_du0dx](long double x) -> long double {
            return (-funcao_F(x) + constante_du0dx)/a_chapeu
            ;};
        long double constante_u0 = constante_du0dx;
        auto u0 = [a_chapeu,funcao_f,constante_u0](long double x) -> long double{
            //original
            return (-integral_dupla(funcao_f,x)+x*constante_u0)/a_chapeu
            //return (-x*x+x*(1.0))/(2.0*a_chapeu)
            ;};
        //condicional para por u0********************
        if (stoi(argv[5])){saida_1 = criador_grafico_json (saida_1,u0,"u0",superior,inferior,precisao_grafico);}
        //condicional para ver se u1 ou u2 é usado
        if (stoi (argv[6]) or stoi (argv[7]) or stoi(argv[9])){
            //sobre N1 e u1--------------------
            auto N1 = [a_chapeu,funcao_a,E,beta](long double y) -> long double {
                long double y_real = y - floor(y);
                //forma de integral genérica que é mais pesada
                //long double adicional= y_real<=.25 ? (0) : (y_real>=.75 ? 2 : 1);
                //return integral ([a_chapeu,funcao_a](long double s) -> long double {
                //    return (a_chapeu/funcao_a(s)-1.0);
                //},y_real)+adicional*a_chapeu/beta;
                //forma de integral resolvida
                return y_real<=.25 ? a_chapeu*y_real/5 -y_real: 
                (y_real<=.75 ? a_chapeu*y_real/10 -y_real + a_chapeu*.25/5 -.25 + a_chapeu/beta: 
                a_chapeu*y_real/5 -y_real+a_chapeu*0.75/10 -0.75 + a_chapeu*.25/5 -.25 + 2*a_chapeu/beta);
            };
            //auto u1 = [N1,u0,E,a_chapeu](long double x) -> long double{
            //    return u0(x)+E*N1(x/E)*(-2*x+1)/(2*a_chapeu); 
            //};
            //original
            auto u1 = [N1,E,du0dx,u0](long double x) -> long double{
                return N1(x/E)*du0dx(x)*E+u0(x)
            ;};
            //condicional para por u1********************
            if (stoi(argv[6])){saida_1 = criador_grafico_json (saida_1,u1,"u1",superior,inferior,precisao_grafico);}
            //condicional para por N1********************
            if (stoi(argv[8])){saida_2 = criador_grafico_json (saida_2,N1,"N1",superior/E,inferior/E,precisao_grafico_2);}
            //condicional para ver se u2 é usado
            if (stoi(argv[7]) or stoi(argv[9])){
                //sobre N2 e u2-------------------
                long double constante_N2 = a_chapeu*integral (N1);
                
                auto N2 = [constante_N2,funcao_a,N1,E](long double y) -> long double {
                    long double y_real = y - floor(y);
                    return integral ([constante_N2,funcao_a,N1,E](long double s) -> long double {
                        return -N1(s) + constante_N2/funcao_a(s)
                        ;},y_real)
                    ;};

                auto u2 = [d2u0dx2,N2,N1,du0dx,u0,E](long double x) -> long double {
                    return d2u0dx2(x)*N2(x/E)*E*E+du0dx(x)*N1(x/E)*E+u0(x)
                    ;};
                
                //condicional para u2*********************
                if (stoi(argv[7])){saida_1 = criador_grafico_json (saida_1,u2,"u2",superior,inferior,precisao_grafico);}
                //condicional para N2*********************
                if (stoi(argv[9])){saida_2 = criador_grafico_json (saida_2,N2,"N2",superior/E,inferior/E,precisao_grafico_2);}
            }
        }
    }
    ofstream saida("./magia_cpp/saidas_e_executaveis/imperfeito_exemplo_saida_dados.txt");
    saida << "[[" << saida_1 << "[[0],[0],\"sucesso\"]],[" << saida_2 << "[[0],[0],\"sucesso\"]]]";
    saida.close();
    return 1;
}
