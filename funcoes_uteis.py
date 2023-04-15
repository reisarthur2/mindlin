from numpy import linspace,trapz
import matplotlib.pyplot as mp
#funcoes basicas para fazer analise
def integral (funcao,lim_sup:float=1,lim_inf:float=0):
    precisao_por_unidade=100
    intervalo=linspace(lim_inf,lim_sup,precisao_por_unidade)
    return trapz(funcao(intervalo),intervalo)

def derivada (funcao,x):
    return (funcao(x+0.0001)-funcao(x))/0.0001


def plotar (funcao1,funcao2,funcao3,liminf=0,limsup=1):
    x=linspace(0,1,100)
    fig, eixos = mp.subplots(layout='constrained')
    eixos.plot (x,tuple(map(funcao1,x)),scalex=0.1,scaley=.01,label='ue1')
    eixos.plot (x,tuple(map(funcao2,x)),scalex=0.1,scaley=.01,label='ue2')
    eixos.plot (x,tuple(map(funcao3,x)),scalex=0.1,scaley=.01,label='u0')
    eixos.legend()
    mp.xlabel('amogus')
    #mp.show()
