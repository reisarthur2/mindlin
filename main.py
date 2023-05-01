from fractions import Fraction
from funcoes import plotar,grafico_duplo

from continuo_exato_geral import exato_ue
from continuo_aproximado_geral import aproximado_numerico_un
from continuo_exemplo1 import aproximado_analitico_un

from caso_partes_exato_geral import exato_partes_ue
from caso_partes_aproximado import partes_numerico_un

"""
nota1: é bom ler o que as funcoes recebem e o que retornam
      passando o mouse por cima das mesmas com a tecla ctrl
      segurada
nota2: é bom ter bom senso e nao complicar nada (se for para
       aumentar a velocidade do codigo em pelo menos 300x
       complicar é uma atitude válida)
       
       
analise:
é perceptível ao "brincar" com várior gráficos e comparar com os outros
que em questão de velocidade e precisão u0 nas aproximadas é superior
até para epsilons maiores

mas se for para rankear:
1-analitico
2-exato
3-numerico

no aproximado quanto mais contas analiticas forem inseridas, menos pesado
se torna o programa, mas o exato também não fica para trás
"""

epsilon=1/32
#analise= partes_numerico_un ('u0',epsilon=epsilon,precisao_grafico=(30))
#primeiro = analise[0]
##primeiro.append (exato_partes_ue(epsilon=epsilon,precisao_grafico=30))
#segundo = analise[1]
#
#titulo_1=f'ε={Fraction (epsilon).limit_denominator()}'
#titulo_2=f'ε={Fraction (epsilon).limit_denominator()}'
#grafico_duplo (primeiro,segundo,rotulo_eixo_x1='x',rotulo_eixo_x2='y ou x/ε',titulo_1=titulo_1,titulo_2=titulo_2)


#plotar (aproximado_analitico_un('u0',epsilon=epsilon,precisao_grafico=30)[0][0])
plotar (exato_ue(epsilon=epsilon,precisao_grafico=30))