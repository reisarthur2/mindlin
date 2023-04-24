from fractions import Fraction
from numpy import cos,pi,sin,arctan,tan
from funcoes_uteis import grafico_duplo, integral,derivada,plotar

l=1
L=4

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

#def N1ex1 (x):
#    return +(0.00060)+((0.12629)*sin (2*pi*x*(1)))+((-0.09138)*sin (2*pi*x*(2)))+((0.06331)*sin (2*pi*x*(3)))+((-0.04770)*sin (2*pi*x*(4)))+((0.03818)*sin (2*pi*x*(5)))+((-0.03182)*sin (2*pi*x*(6)))+((0.02727)*sin (2*pi*x*(7)))+((-0.02385)*sin (2*pi*x*(8)))+((0.02120)*sin (2*pi*x*(9)))+((-0.01907)*sin (2*pi*x*(10)))+((0.01733)*sin (2*pi*x*(11)))+((-0.01589)*sin (2*pi*x*(12)))+((0.01466)*sin (2*pi*x*(13)))+((-0.01361)*sin (2*pi*x*(14)))+((0.01269)*sin (2*pi*x*(15)))+((-0.01190)*sin (2*pi*x*(16)))+((0.01119)*sin (2*pi*x*(17)))+((-0.01057)*sin (2*pi*x*(18)))+((0.01000)*sin (2*pi*x*(19)))+((-0.00950)*sin (2*pi*x*(20)))+((0.00904)*sin (2*pi*x*(21)))+((-0.00863)*sin (2*pi*x*(22)))+((0.00825)*sin (2*pi*x*(23)))+((-0.00790)*sin (2*pi*x*(24)))+((0.00758)*sin (2*pi*x*(25)))+((-0.00728)*sin (2*pi*x*(26)))+((0.00701)*sin (2*pi*x*(27)))+((-0.00675)*sin (2*pi*x*(28)))+((0.00651)*sin (2*pi*x*(29)))+((-0.00629)*sin (2*pi*x*(30)))+((0.00608)*sin (2*pi*x*(31)))+((-0.00589)*sin (2*pi*x*(32)))+((0.00570)*sin (2*pi*x*(33)))+((-0.00553)*sin (2*pi*x*(34)))+((0.00537)*sin (2*pi*x*(35)))+((-0.00521)*sin (2*pi*x*(36)))+((0.00507)*sin (2*pi*x*(37)))

produto=integral(N1ex1)*a_chapeu

def N2ex1 (y):
    return integral (lambda x: produto/funcao_a(x)-N1ex1(x),y)

def u2ex1 (y):
    return u0ex1(y)+derivada(u0ex1,y)*N1ex1(y)+(funcao_f(y)/a_chapeu)*N2ex1(y)

plotar (u2ex1)