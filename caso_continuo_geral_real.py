from funcoes_uteis import integral,plotar
from numpy import cos,pi,sin
import time
start_time = time.time()

#modificável--------------------------------------
l=1
L=32

e=l/L

funcao_a = lambda x: 1+0.25*cos(2*pi*x/e)
funcao_x = lambda x: x
#---------------------------------------------
a_chapeu = (integral(lambda x: (funcao_a(x))**-1))**-1
funcao_F = lambda t: integral (funcao_x,t)
parte_constante = a_chapeu*integral(lambda t: funcao_F(t)/funcao_a(t))
def ue (x):
    return integral(lambda s: (funcao_F(s)-parte_constante)/funcao_a(s),x)

plotar(ue)

end_time = time.time()

# Calculando o tempo decorrido
elapsed_time = end_time - start_time

print(f'Tempo de execução: {elapsed_time:.5f} segundos')