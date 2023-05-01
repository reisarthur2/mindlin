import matplotlib.pyplot as mp
from typing import Callable,Iterable
from os import system



def plotar (*args:list,**kwargs):
    
    """
    parametros{\n
        args: m listas de pares x,y neste formato:\n
        [[x1,x2,...,xn],[y1,y2,...,yn],"nome da funcao"]\n
        }\n
    kwargs {\n
        escala_x = float (0.1 por padrão)\n
        escala_y = float (0.1 por padrão)\n
        nome_arquivo = str\n
        linha_espessura = float (1 por padrão)\n
        }
    
    exemplo de uso:\n
    par1 = [[1,2,3,4],[2,8,15,17],"nomepar1"]\n
    par2 = [[1,2],[0,0],"nomepar2"]
    
    nome_das_funcoes = ["funcao1","funcao2"]\n
    plotar (par1 , par2)
    
    >> salvo arquivo saida.png ou com nome escolhido (não precisa por extensão .png ou .jpg)
    """
    
    escalax=kwargs.get ('escala_x',0.1)
    escalay=kwargs.get ('escala_y',0.1)

    linha_espessura=kwargs.get ('linha_espessura',1)
    nome_arquivo = kwargs.get ('nome_arquivo','saida_normal')
    
    fig, eixos = mp.subplots(layout='constrained')
    for numero_do_grafico in range(len (args)):
        eixos.plot (args[numero_do_grafico][0][:-1],args[numero_do_grafico][1][:-1],scalex=escalax,scaley=escalay,linewidth=linha_espessura,label=args[numero_do_grafico][2])
    
    eixos.grid()
    eixos.legend()
    
    #mp.show ()
    mp.savefig(nome_arquivo+'.png')


def grafico_duplo (conjunto_1:list,conjunto_2:list,**kwargs):
    
    """
    parametros{\n
        conjunto_1: primeiro conjunto de funções em lista\n
        conjunto_2: segundo conjunto de funções em lista\n
    
        observações:\n
        formato aceito de cada funcao:\n
        funcaoi = [[x1,x2,...,xn],[y1,y2,...,yn],"nome da funcao i"]
    
        formato aceito para cada conjunto:\n
        conjunto_1 ou conjunto_2 = [funcao1,funcao2,...,funcaon]\n
        }\n
    kwargs{\n
    
        escala_x = float\n
        escala_y = float\n
        
        rotulo_eixo_x1 = str\n
        rotulo_eixo_x2 = str\n
        
        nome_arquivo = str\n
        linha_espessura = float (1 por padrão)\n
        
        titulo_1 = str\n
        titulo_2 = str\n
        
        por padrao é salvo um arquivo\n
        se quiser mostrar em tela separada use:\n
        mostrar = 1\n
        \n
        nao precisa mexer nos rotulos do eixoy\n
        }
    """
    escalax=kwargs.get ('escala_x',0.1)
    escalay=kwargs.get ('escala_y',0.1)
    
    linha_espessura=kwargs.get ('linha_espessura',0.5)
    
    titulo1=kwargs.get ('titulo_1','titulo_1')
    titulo2=kwargs.get ('titulo_2','titulo_2')
    
    eixox1=kwargs.get ('rotulo_eixo_x1','rotulo_eixo_x1')
    eixox2=kwargs.get ('rotulo_eixo_x2','rotulo_eixo_x2')
    
    eixoy1=kwargs.get ('rotulo_eixo_y1',r'Aproximações de $U^{ε}$')
    eixoy2=kwargs.get ('rotulo_eixo_y2',r'$N_{x/ε}$')
    
    nome_arquivo = kwargs.get ('nome_arquivo','saida_dupla')
    mostrar = kwargs.get ('mostrar',0)
    
    fig, (eixo1,eixo2) = mp.subplots(ncols=2,layout='constrained')
    
    for iterador_1 in range (len(conjunto_1)):
        eixo1.plot (conjunto_1[iterador_1][0],conjunto_1[iterador_1][1],scalex=escalax,scaley=escalay,linewidth=linha_espessura,label=conjunto_1[iterador_1][2])
    for iterador_2 in range (len(conjunto_2)):
        eixo2.plot (conjunto_2[iterador_2][0],conjunto_2[iterador_2][1],scalex=escalax,scaley=escalay,linewidth=linha_espessura,label=conjunto_2[iterador_2][2])
    eixo1.grid()
    eixo1.legend()
    eixo1.set_title(f"{titulo1}",size=20)
    eixo1.set_xlabel (eixox1)
    eixo1.set_ylabel (eixoy1,size=15)
    
    eixo2.grid()
    eixo2.legend()
    eixo2.set_title(f"{titulo2}",size=20)
    eixo2.set_xlabel (eixox2)
    eixo2.set_ylabel (eixoy2,size=15)
    
    if (mostrar):
        mp.show ()
    else:
        mp.savefig(nome_arquivo+'.png')