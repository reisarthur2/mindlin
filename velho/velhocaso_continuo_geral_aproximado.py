from numpy import cos,pi,sin
from funcoes_uteis import integral,derivada,plotar,grafico_duplo
from fractions import Fraction
import time
start_time = time.time()
l=.2
L=1

e=l/L

funcao_a = lambda y: 1+0.25*cos(2*pi*(y/e))
funcao_f = lambda x: x
funcao_F = lambda x: integral (funcao_f,x)
a_chapeu = (integral(lambda x: (funcao_a(x))**-1))**-1

#fazer u0 ser independente do programador--
def d2u0dx2 (x):
    return funcao_f(x)/a_chapeu
#--
constante_u0 = integral (lambda x: integral (funcao_f,x))
def du0dx (x):
    return (funcao_F(x)-constante_u0)/a_chapeu

def u0 (x):
    return (integral (funcao_F,x)-x*constante_u0)/a_chapeu
# TRAPAÇA GRRRRRRRRRRR >:(
#def u0 (x):
#    return (x*(x**2-1))/(6*a_chapeu)

def N1 (y):
    return integral (lambda s: (a_chapeu/funcao_a(s))-1,y)

def u1 (x):
    return (derivada(u0,x))*N1(x/e)

tudocte=integral(N1)*a_chapeu

def N2(y):
    return integral (lambda s: -N1(s)+tudocte/funcao_a(s),y)

def u2 (x):
    return (funcao_f(x)/a_chapeu)*N2(x/e)

def ue1 (x):
    return u0(x)+e*u1(x)

def ue2 (x):
    return u0(x)+e*u1(x)+e*e*u2(x)

zero=lambda x: 0

#grafico_duplo([u0,ue1,ue2],[N1,N2],titulo_1=f'ε={Fraction (e).limit_denominator()}',titulo_2=f'ε={Fraction (e).limit_denominator()}')

grafico_duplo([N1,N2],[])

end_time = time.time()

# Calculando o tempo decorrido
elapsed_time = end_time - start_time

print(f'Tempo de execução: {elapsed_time:.5f} segundos')