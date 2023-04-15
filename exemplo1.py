from numpy import cos,pi,sin
from funcoes_uteis import integral,derivada,plotar

l=0.5
L=1

e=l/L

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
