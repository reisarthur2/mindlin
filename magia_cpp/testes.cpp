#include "funcoescpp.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <string>

int main (){
    auto funcao = [](double x) -> double {return x;};

    auto teste = fourier_coeficientes (funcao,1);
    auto funcao2 = [teste](double x) -> double {
        return transformada_fourier(teste,x);
        };
    

    string saida_1 = "";

    saida_1 = criador_grafico_json (saida_1,funcao2,"carlos",1,0,0.05);
    
    ofstream saida("./magia_cpp/teste_maluco.txt");
    saida << saida_1.substr(0,saida_1.length()-1);
    saida.close();
    return 0;
}