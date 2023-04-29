from funcoes_uteis import integral,plotar, fourier_coeficientes, transformada_fourier,grafico_duplo
from numpy import cos,pi,sin , abs
import time
start_time = time.time()

#modificável--------------------------------------
l=1
L=32

a1=2
a2=3
delta=.25

e=l/L

funcao_aantiga = lambda x: a1 if (x<.5-delta) else a1 if (x>.5+delta) else a2
funcao_x = lambda x: -1+x-x

coeficientes=fourier_coeficientes (funcao_aantiga,numero_senoides=1000)
funcao_a = lambda x : transformada_fourier (coeficientes,x)

#---------------------------------------------
a_chapeu = (integral(lambda x: (funcao_a(x))**-1))**-1
funcao_F = lambda t: integral (funcao_x,t)

parte_constante_k0 = a_chapeu*integral(lambda t: funcao_F(t)/funcao_a(t))
def ue (x):
    return integral(lambda s: (funcao_F(s)-parte_constante_k0)/funcao_a(s),x)

grafico_duplo([ue],[funcao_a,funcao_aantiga])

end_time = time.time()

# Calculando o tempo decorrido
elapsed_time = end_time - start_time

print(f'Tempo de execução: {elapsed_time:.5f} segundos')