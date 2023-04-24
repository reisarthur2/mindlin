from numpy import linspace,trapz, zeros_like , vectorize, polynomial
import matplotlib.pyplot as mp
from typing import Callable,Iterable

#funcoes basicas para fazer analise
#def integral (funcao: Callable,lim_sup:float=1,lim_inf:float=0):
#    precisao_por_unidade=200
#    intervalo=linspace(lim_inf,lim_sup,precisao_por_unidade)
#    y2=vectorize(funcao)
#    return trapz(y2(intervalo),intervalo)

def integral (funcao: Callable,lim_sup:float=1,lim_inf:float=0):
    precisao_por_unidade=200
    intervalo=linspace(lim_inf,lim_sup,precisao_por_unidade)
    try:
        return trapz(funcao(intervalo),intervalo)
    except:
        return trapz (vectorize(funcao)(intervalo),intervalo)

def derivada (funcao:Callable,x:float) -> float:
    return (funcao(x+0.00001)-funcao(x))/0.00001

def plotar (*args:Callable,**kwargs):
    numero_amostras= kwargs.get ('numero_amostras',50)
    escalax=kwargs.get ('escala_x',0.1)
    escalay=kwargs.get ('escala_y',0.1)
    linha_espessura=kwargs.get ('linha_espessura',0.5)
    x=linspace(0,1,numero_amostras)
    fig, eixos = mp.subplots(layout='constrained')
    for funcao in args:
        eixos.plot (x,tuple(map(funcao,x)),scalex=escalax,scaley=escalay,linewidth=linha_espessura,label=funcao.__name__)
    eixos.grid()
    eixos.legend()
    mp.savefig('saida.png')

def grafico_duplo (*args:Iterable,**kwargs):
    numero_amostras1= kwargs.get ('numero_amostras1',30)
    numero_amostras2= kwargs.get ('numero_amostras2',100)
    
    escalax=kwargs.get ('escala_x',0.1)
    escalay=kwargs.get ('escala_y',0.1)
    
    linha_espessura=kwargs.get ('linha_espessura',0.5)
    
    titulo1=kwargs.get ('titulo_1','sem nada')
    titulo2=kwargs.get ('titulo_2','sem nada')
    
    eixox1=kwargs.get ('eixo_x1','x')
    eixox2=kwargs.get ('eixo_x1','x')
    
    eixoy1=kwargs.get ('eixo_y1',r'Aproximações de $U^{ε}$')
    eixoy2=kwargs.get ('eixo_y2',r'$N_{x/ε}$')
    
    x1=linspace(0,1,numero_amostras1)
    x2=linspace(0,1,numero_amostras2)
    fig, (eixo1,eixo2) = mp.subplots(ncols=2,layout='constrained')
    for funcao in args[0]:
        eixo1.plot (x1,tuple(map(funcao,x1)),scalex=escalax,scaley=escalay,linewidth=linha_espessura,label=funcao.__name__)
    for funcao in args[1]:
        eixo2.plot (x2,tuple(map(funcao,x2)),scalex=escalax,scaley=escalay,linewidth=linha_espessura,label=funcao.__name__)
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
    
    mp.savefig('saida.png')
