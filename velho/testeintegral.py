from funcoes_uteis import plotar , integral
from numpy import cos,pi,sin, polynomial , vectorize
import time
start_time = time.time()

#def integral (funcao,lim_sup:float=1,lim_inf:float=0,**kwargs):
#    grau_quadratura= 100
#    x, w = polynomial.legendre.leggauss(grau_quadratura)
#    t = 0.5*(lim_sup-lim_inf)*x + 0.5*(lim_sup+lim_inf)
#    try:
#        return 0.5*(lim_sup-lim_inf)*sum(w*funcao(t))
#    except:
#        return 0.5*(lim_sup-lim_inf)*sum(w*vectorize(funcao)(t))




end_time = time.time()

# Calculando o tempo decorrido
elapsed_time = end_time - start_time

print(f'Tempo de execução: {elapsed_time:.5f} segundos')



#botar por fora a quadratura em funcao de e=l/L