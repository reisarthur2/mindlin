from os import system
import json

"""
em resumo esse codigo ta pronto, nao precisa mexer
modelo para outros
"""

def exato_partes_ue (*args, **kwargs):
    
    """
    parametros:\n
    l_pequeno = float (0.01 padrao)\n
    l_grande = float (1 padrao)\n
    epsilon = float (padrao l/L)\n
    precisao_grafico = float (padrao 50 minimo 20)\n
    nome_custom = str (padrao "ue")\n
    Retorna:\n
    
    [[[x],[ue(x)]],"nome_custom"]
        
    """
    #parametros
    l = kwargs.get ('l_pequeno',0.01)
    L = kwargs.get ('l_grande',1)
    e = kwargs.get ('epsilon',l/L)
    nome = kwargs.get ('nome_custom','ue')
    precisao_grafico = kwargs.get ('precisao_grafico',50)
    limite_superior = kwargs.get ('limite_superior',1)
    limite_inferior = kwargs.get ('limite_inferior',0)
    
    if (precisao_grafico>=20):
        system('g++ ./magia_cpp/partes_exato.cpp -o ./magia_cpp/saidas_e_executaveis/partes_exato')
        system(f'.\magia_cpp\saidas_e_executaveis\partes_exato {e} {precisao_grafico} {limite_inferior} {limite_superior}')

        with open ("./magia_cpp/saidas_e_executaveis/partes_exato_saida_dados.txt","r") as resultados:
            saida = json.loads (resultados.read())
            saida.append (nome)
            return saida
    else:
        print ("verificar o valor de precisao minimo 20")
        return 0