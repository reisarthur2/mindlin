from fractions import Fraction
from funcoes import plotar,grafico_duplo
import time

from continuo_exato_geral import exato_ue
from continuo_aproximado_geral import aproximado_numerico_un
from continuo_exemplo1 import aproximado_analitico_un

from caso_partes_exato_geral import exato_partes_ue
from caso_partes_aproximado import partes_numerico_un
from caso_partes_exemplo1 import partes_analitico_un
"""
nota1: é bom ler o que as funcoes recebem e o que retornam
       passando o mouse por cima das mesmas com a tecla ctrl
       segurada
nota2: é bom ter bom senso e nao complicar nada (se for para
       aumentar a velocidade do codigo em pelo menos 300x
       complicar é uma atitude válida) 
nota3: é importante perceber que as funções aproximadas retornam
       várias funções, e que para saber a forma de plotar os graficos 
       nas funções, é bom ver os exemplos abaixo
nota4: ainda será implementada uma função que altera as funções analisadas
       direto pelo python, sem precisar saber nada de cpp
nota5: leia o README, é interessante :)
nota6: se quiser mudar a precisão da integral, é porque está mexendo
       com coisas mais pesadas, que são para adultos que sabem o que
       estão fazendo, se você é um desses, pode ir no arquivo do header
       funcoescpp.h em magia_cpp e, ou adotar outro dos metodos la oferecidos,
       ou mudar a precisão que se encontra no ultimo parâmetro que se encontra
       como declaração de parâmetro com valor padrão (int n = 1500 no fim da linha
       35 do header)
       
análise:
       é perceptível ao "brincar" com várior gráficos e comparar com os outros
       que em questão de velocidade e precisão u0 nas aproximadas é superior
       até para epsilons maiores

mas se for para fazer um top 3:
1-analitico
2-exato
3-numerico

no aproximado quanto mais contas analiticas forem inseridas, menos pesado
se torna o programa, mas o exato também não fica para trás
"""
#por favor mudar o epsilon do jeito que desejar
epsilon=1/4

#tem vários exemplos de uso, meu preferido é o 4
exemplo_analisado = 4

#exemplo 1.1 de uso - apenas um gráfico, para aproximadas é preciso
#                   saber qual gráfico se quer, veja as saidas
#                   para saber como consegui-lo!
if (exemplo_analisado==1.1):
      plotar (exato_ue(epsilon=epsilon))
#exemplo 1.2
if (exemplo_analisado==1.2):
      plotar (aproximado_analitico_un('u2',epsilon=epsilon)[0][0])

#exemplo 2 de uso - muitos gráficos com duas telas
if (exemplo_analisado==2):
      analise= partes_analitico_un ('u1','n1',epsilon=epsilon)
      primeiro = analise[0]
      segundo = analise[1]
      titulo_1=f'ε={Fraction (epsilon).limit_denominator()}'
      titulo_2=f'ε={Fraction (epsilon).limit_denominator()}'
      grafico_duplo (primeiro,segundo,rotulo_eixo_x1='x',rotulo_eixo_x2='y ou x/ε',titulo_1=titulo_1,titulo_2=titulo_2)

#exemplo 3 de uso - muitíssimos gráficos com duas telas
if (exemplo_analisado==3):
      analise1 = partes_analitico_un ('u0','u1','n1',epsilon=epsilon,precisao_grafico=50)
      analise2 = partes_numerico_un ('u0','u1','n1',epsilon=epsilon,precisao_grafico=50)
      primeiro = analise1[0]
      primeiro.append (exato_partes_ue(epsilon=epsilon,precisao_grafico=50))
      primeiro.extend (analise2[0])
      segundo = analise1[1]
      segundo.extend (analise2[1])
      titulo_1=f'ε={Fraction (epsilon).limit_denominator()}'
      titulo_2=f'ε={Fraction (epsilon).limit_denominator()}'
      grafico_duplo (primeiro,segundo,rotulo_eixo_x1='x',rotulo_eixo_x2='y ou x/ε',titulo_1=titulo_1,titulo_2=titulo_2)

#exemplo 4 de uso - comparando a velocidade de vários métodos
if (exemplo_analisado==4):
      #tempo do primeiro
      start_time = time.time()

      grafico1 = (exato_partes_ue(epsilon=epsilon))

      end_time = time.time()
      elapsed_time = end_time - start_time
      print(f'Tempo de execução do primeiro gráfico: {elapsed_time:.5f} segundos')

      #tempo do segundo
      start_time = time.time()

      grafico2 = (partes_numerico_un('u1',epsilon=epsilon)[0][0])

      end_time = time.time()
      elapsed_time = end_time - start_time
      print(f'Tempo de execução do segundo gráfico: {elapsed_time:.5f} segundos')

      #tempo do terceiro
      start_time = time.time()

      grafico3 = (partes_analitico_un('u1',epsilon=epsilon)[0][0])

      end_time = time.time()
      elapsed_time = end_time - start_time
      print(f'Tempo de execução do terceiro gráfico: {elapsed_time:.5f} segundos')

      #comparação
      titulo=f'ε={Fraction (epsilon).limit_denominator()}'
      plotar(grafico1,grafico2,grafico3,titulo=titulo)