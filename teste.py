#import os
#import json
#from funcoes import plotar

#def testando ():
#    os.system("g++ ./magia_cpp/testes.cpp -o ./magia_cpp/maluquisse")
#    os.system('.\\magia_cpp\\maluquisse')
#    with open (".\\magia_cpp\\teste_maluco.txt","r") as resultados:
#        saida = json.loads (resultados.read())
#        return saida
#    


def integral2 (funcao,limsup=5,liminf=1,dx=0.0002):
    atualx=liminf
    iterador = (limsup-liminf)/dx + 1 - liminf
    acumulador = 0
    while atualx<=limsup:
        acumulador += iterador*funcao (atualx)
        iterador-=1
        atualx+=dx
    return acumulador*dx*dx

bola = lambda x: x 

print (integral2 (bola))