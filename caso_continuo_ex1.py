from fractions import Fraction
from numpy import cos,pi,sin
from funcoes_uteis import grafico_duplo, integral,derivada,plotar

l=1
L=100

e=l/L
def func (s):
    return ((s)**2-(1/3))/(1+0.25*cos((2*pi*s/e)))/(2)

def ue (x):
    return integral(func,x)