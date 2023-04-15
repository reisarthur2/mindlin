from numpy import cos,pi,sin
from funcoes_uteis import integral,derivada,plotar

l=0.5
L=1

e=l/L

funcao_a = lambda y: 1+0.25*cos(2*pi*(y/e))

funcao_f = lambda x: x

a_chapeu = (integral(lambda x: (funcao_a(x))**-1))**-1

#fazer u0 ser independente do programador
def u0 (x):
    return (x*(x**2-1))/(6*a_chapeu)

def N1 (y):
    return integral (lambda s: (a_chapeu/funcao_a(s))-1,y)

def u1 (x):
    return (derivada(u0,x))*N1(x/e)

def N2(y):
    tudocte=integral(N1)*a_chapeu
    return integral (lambda s: -N1(s)+tudocte/funcao_a(s),y)

def u2 (x):
    return (funcao_f(x)/a_chapeu)*N2(x/e)

def ue2 (x):
    return u0(x)+e*u1(x)+e*e*u2(x)

def ue1 (x):
    return u0(x)+e*u1(x)

plotar(ue1,ue2,u0)