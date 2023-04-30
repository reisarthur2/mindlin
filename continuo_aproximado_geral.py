from os import system
import json
from funcoes import plotar

def aproximado_un (*args, **kwargs):
    
    """
    sobre os argumentos args com exemplo de uso {\n
    
    
    aproximado_un ('N1','N2','u0','u1','u2','a'...)\n
    
    retorna [ [ [x1,x2,...,xm] , [un1,un2,...,unm] , 'nome da funcao u'] , [outros u] ], \n
              [ [x1,x2,...,xq] , [Np1,Np2,...,Npq] , 'nome da funcao N'] , [outras N] ] ]\n
    obs: conforme é posto os argumentos, DEVE-SE TER EM CONTA\n
         QUE OS N1,N2 OU a são inseridos no segundo argumento\n
    
    
    }\n
    parametros kwargs:\n
    aproximacao = int (0 padrao)
    l_pequeno = float (0.01 padrao)\n
    l_grande = float (1 padrao)\n
    epsilon = float (padrao l/L)\n
    precisao_grafico = float (padrao 0.01)\n
    nome_custom = str (padrao "ue")\n
    
        
    """
    #parametros
    l = kwargs.get ('l_pequeno',0.01)
    L = kwargs.get ('l_grande',1)
    e = kwargs.get ('epsilon',l/L)
    precisao_grafico = kwargs.get ('precisao_grafico',0.01)
    limite_superior = kwargs.get ('limite_superior',1)
    limite_inferior = kwargs.get ('limite_inferior',0)
    
    
    comparador =     ['u0','u1','u2','n1','n2','a','se ha funcoes']
    parametros_cpp = [ 0  , 0  , 0  , 0  , 0  , 0 ,    0]
    for comparado in args:
        if (comparado  in comparador) or ((comparado:=comparado[0].lower() + comparado[1:]) in comparador):
            parametros_cpp[6] = 1
            parametros_cpp[comparador.index(comparado)] = 1
    
    parametro_final = str (parametros_cpp[0])
    for iterador in parametros_cpp[1:]:
        parametro_final=parametro_final+" "+str (iterador)
    
    if (type(precisao_grafico) is float):
        system('g++ ./magia_cpp/continuo_aproximado.cpp -o ./magia_cpp/continuo_aproximado')
        system(f'.\magia_cpp\continuo_aproximado {e} {precisao_grafico} {limite_inferior} {limite_superior} {parametro_final}')

        with open ("./magia_cpp/continuo_aproximado_saida_dados.txt","r") as resultados:
            #print (resultados.read())
            saida = json.loads (resultados.read())
            return saida[0][:-1],saida[1][:-1]
    else:
        print ("verificar o valor de precisao")