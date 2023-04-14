from functools import reduce
from numpy import cos,pi,sin,sqrt,linspace
import matplotlib.pyplot as mp

dx=0.02

l=0.5
L=1

e=l/L

#limitado quanto a profundidade de recursão
def integral (funcao,limsup_ou_var:float=L,liminf:float=0,primeiro=1):
    if (limsup_ou_var<=liminf or primeiro==1):
        return ((dx/2)*(funcao(limsup_ou_var)+2*integral(funcao,limsup_ou_var-dx,liminf,0))) if primeiro==1 else funcao(limsup_ou_var)/2
    else:
        return funcao (limsup_ou_var)+integral(funcao,limsup_ou_var-dx,liminf,primeiro)

def plotar (funcao1,funcao2,funcao3,liminf=0,limsup=1):
    x=linspace(0,1,100)
    fig, eixos = mp.subplots(layout='constrained')
    eixos.plot (x,tuple(map(funcao1,x)),scalex=0.1,scaley=.01,label='ue1')
    eixos.plot (x,tuple(map(funcao2,x)),scalex=0.1,scaley=.01,label='ue2')
    eixos.plot (x,tuple(map(funcao3,x)),scalex=0.1,scaley=.01,label='u0')
    eixos.legend()
    mp.xlabel('amogus')
    mp.show()

#nao sei por que nao funciona, mas tem potencial grande
#def integral (funcao,limsup:float=1,liminf:float=0):
#    auxiliar=linspace(liminf,limsup,100)
#    return ((limsup-liminf)/100)*0.5*(2*reduce(lambda x,y: x+y,map(funcao,auxiliar))-funcao(liminf)-funcao(limsup))



def derivada (funcao,x):
    return (funcao(x+0.0001)-funcao(x))/0.0001

def funcao_a (y):
    return 1+0.25*cos(2*pi*(y/e))

def funcao_f (x):
    return x

a_chapeu=(integral(lambda x: (funcao_a(x))**-1))**-1

#fazer u0 ser independente do programador
def u0 (x,achapeu=a_chapeu):
    return (x*(x**2-1))/(6*achapeu)


def N1 (y,achapeu=a_chapeu):
    return integral (lambda s: (achapeu/funcao_a(s))-1,y)

def u1 (x,achapeu=a_chapeu):
    return (derivada(u0,x))*N1(x/e,achapeu)

def N2(y,achapeu=a_chapeu):
    tudocte=integral(N1)*achapeu
    return integral (lambda s: -N1(s)+tudocte/funcao_a(s),y)

def u2 (x,achapeu=a_chapeu):
    return (funcao_f(x)/achapeu)*N2(x/e,achapeu)

def ue2 (x):
    return u0(x)+e*u1(x)+e*e*u2(x)

def ue1 (x):
    return u0(x)+e*u1(x)

plotar(ue1,ue2,u0,a_chapeu)