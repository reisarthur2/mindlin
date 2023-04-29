from fractions import Fraction
from numpy import cos,pi,sin,arctan,tan
from funcoes_uteis import grafico_duplo, integral,derivada,plotar, fourier_coeficientes, transformada_fourier
import time
start_time = time.time()

l=1
L=1

e=l/L
funcao_f = lambda x: x
funcao_a = lambda y: 1+0.25*cos(2*pi*(y/e))

a_chapeu = (integral(lambda x: (funcao_a(x))**-1))**-1
raiz=(1-.25**2)**.5
def func (s):
    return ((s)**2-(1/3))/(1+0.25*cos((2*pi*s/e)))/(2)

def ue (x):
    return integral(func,x)

def u0ex1 (x):
    return (x*(x**2-1))/(6*a_chapeu)

def N1ex1 (y):
    if y<1/2: return a_chapeu/pi/raiz*arctan(0.75*tan(y*pi)/raiz)-y
    if y-1/2<0.001: return 0
    if y>1/2: return a_chapeu/pi/raiz*arctan(0.75*tan(pi*y)/raiz)-y+1

#N1ex1_trans_coeficientes = fourier_coeficientes(N1ex1velha)
#def N1ex1 (y):#nova
#    return transformada_fourier(N1ex1_trans_coeficientes,y)

produto=integral(N1ex1)*a_chapeu

def N2ex1 (y):
    return integral (lambda x: produto/funcao_a(x)-N1ex1(x),y)

def u2ex1 (y):
    return u0ex1(y)+derivada(u0ex1,y)*N1ex1(y)+(funcao_f(y)/a_chapeu)*N2ex1(y)

plotar (u2ex1)

end_time = time.time()

# Calculando o tempo decorrido
elapsed_time = end_time - start_time

print(f'Tempo de execução: {elapsed_time:.5f} segundos')