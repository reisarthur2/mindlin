from continuo_exato_geral import exato_ue
from continuo_aproximado_geral import aproximado_un
from funcoes import plotar,grafico_duplo

"""
nota1: é bom ler o que as funcoes recebem e o que retornam
      passando o mouse por cima das mesmas com a tecla ctrl
      segurada
nota2: é bom ter bom senso e nao complicar nada (se for para
       aumentar a velocidade do codigo em pelo menos 300x
       complicar é uma atitude válida)
"""

#plotar (exato_ue(limite_superior=2.5,limite_inferior=.5))
#plotar (aproximado_un('u2','U0','b',precisao_grafico=.1,nome_custom='sus'),linha_espessura=.5)


analise=aproximado_un ('u1','u0','n1','a',"u2","n2",epsilon=1,precisao_grafico=(.05))

grafico_duplo (analise[0],analise[1])