from os import system
import json
from funcoes import plotar


#parametros
l = 1
L = 500
precisao_grafico = 0.01
nome_do_arquivo = 'augusto'
nome_funcao = ['ue']

e = str (l/L)


if (type(precisao_grafico) is float):
    system('g++ ./magia_cpp/continuo_exato.cpp -o ./magia_cpp/continuo_exato')
    system(f'.\magia_cpp\continuo_exato {e} {precisao_grafico}')

    with open ("./magia_cpp/continuo_exato_saida_dados.txt","r") as resultados:
        #print (resultados.read())
        a = json.loads (resultados.read())

        plotar (a,nome_funcoes=nome_funcao,nome_arquivo = nome_do_arquivo)
else:
    print ("verificar o valor de precisao")