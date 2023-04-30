#include <math.h>
#include <fstream>
#include <string>
#include "funcoescpp.h"
#include <iostream>

/*
notas:

saida arquivo ok v
adicionar graficos  v
adicionar as condicionais com argv v
descobrir o que rola com N2 x

*/


using namespace std;
int main (int argc, char* argv[]) {
    if (argc != 12 or (stoi (argv[argc-1])==0)){
        cerr << "Uso: " << argv[0] << " <epslon> <precisao grafico> <bool> <bool> <bool> <bool> <bool> <bool>\n" << "encontrados " << argc << " parametros";
        return 1;
    }
    //sobre os parametros
    double E = stof(argv[1]);
    double precisao_grafico = stof(argv[2]);
    double inferior = stof (argv[3]);
    double superior = stof (argv[4]);
    //partes da saida que será dupla
    //[ '[ [ [x1],[y1],nome1],[ [x2],[y2],nome2 ] ],'
    //  "[ [ [x3],[N3],nome3],[ [x4],[N4],nome4 ] ]"
    //]
    string saida_1 = "";
    string saida_2 = "";
    //declaração de funcoes do caso, favor nao tocar no resto
    auto funcao_a = [E](double x) -> double{
        return 
        1+0.25*cos(2*M_PI*x/E)
        ;};
    //aqui ^
    auto funcao_f = [](double x) -> double{
        return
        x
        ;};
    auto funcao_F = [funcao_f](double x) -> double{
        return
        integral (funcao_f,x)
        ;};
    //constantes----------------------
    double a_chapeu = 1/(integral([funcao_a](double y) -> double {return 1/funcao_a(y);}));
    //condicional para botar funcao_a******************
    if  (stoi (argv[10])){saida_2 = criador_grafico_json (saida_2,funcao_a,"a",superior,inferior,precisao_grafico);}
    //condicional para ver se algum u é usado
    if (stoi (argv[5]) or stoi (argv[6]) or stoi (argv[7])){
        //sobre u0 ,du2/dx2 , du/dx--------------------------
        auto d2u0dx2 = [a_chapeu,funcao_f](double x) -> double {
            return funcao_f(x)/a_chapeu
            ;};
        double constante_du0dx =  integral (funcao_F);
        auto du0dx = [a_chapeu,funcao_F,constante_du0dx](double x) -> double {
            return (funcao_F(x) - constante_du0dx)/a_chapeu
            ;};
        double constante_u0 = constante_du0dx;
        auto u0 = [a_chapeu,funcao_F,constante_u0](double x) -> double{
            return integral (funcao_F,x)-x*constante_u0/a_chapeu
            ;};
        //condicional para por u0********************
        if (stoi(argv[5])){saida_1 = criador_grafico_json (saida_1,u0,"u0",superior,inferior,precisao_grafico);}
        //condicional para ver se u1 ou u2 é usado
        if (stoi (argv[6]) or stoi (argv[7])){
            //sobre N1 e u1--------------------
            auto N1 = [a_chapeu,funcao_a](double y) -> double {
                return integral([funcao_a,a_chapeu](double s) -> double {return a_chapeu/funcao_a(s) -1;},y)
            ;};
            
            auto u1 = [N1,E,du0dx,u0](double x) -> double{
                return N1(x/E)*du0dx(x)*E+u0(x)
            ;};
            //condicional para por u1********************
            if (stoi(argv[6])){saida_1 = criador_grafico_json (saida_1,u1,"u1",superior,inferior,precisao_grafico);}
            //condicional para por N1********************
            if (stoi(argv[8])){saida_2 = criador_grafico_json (saida_2,N1,"N1",superior,inferior,precisao_grafico*0.5);}
            //condicional para ver se u2 é usado
            if (stoi(argv[7])){
                //sobre N2 e u2-------------------
                double constante_N2 = a_chapeu*integral (N1);
                
                auto N2 = [constante_N2,funcao_a,N1,E](double y) -> double {
                    return integral ([constante_N2,funcao_a,N1,E](double s) -> double {
                        return -N1(s) + constante_N2/funcao_a(s)
                        ;})
                    ;};

                auto u2 = [d2u0dx2,N2,N1,du0dx,u0,E](double x) -> double {
                    return d2u0dx2(x)*N2(x/E)*E*E+du0dx(x)*N1(x/E)*E+u0(x)
                    ;};
                
                //condicional para u2*********************
                if (stoi(argv[7])){saida_1 = criador_grafico_json (saida_1,u2,"u2",superior,inferior,precisao_grafico);}
                //condicional para N2*********************
                if (stoi(argv[9])){saida_2 = criador_grafico_json (saida_2,N2,"N2",superior,inferior,precisao_grafico*0.5);}
            }
        }
    }
    ofstream saida("./magia_cpp/continuo_aproximado_saida_dados.txt");
    saida << "[[" << saida_1 << "[[0],[0],\"sucesso\"]],[" << saida_2 << "[[0],[0],\"sucesso\"]]]";
    saida.close();
    return 1;
}
