import os
import json
from funcoes import plotar

def testando ():
    os.system("g++ ./magia_cpp/testes.cpp -o ./magia_cpp/maluquisse")
    os.system('.\\magia_cpp\\maluquisse')
    with open (".\\magia_cpp\\teste_maluco.txt","r") as resultados:
        saida = json.loads (resultados.read())
        return saida