# mindlin
for english speakers:\n
abstract:\n
research using matplotlib and numpy from python and a bunch of c++ code (for optimization) analysing
structures with a rapdly oscilating property

this code is a tool for the research i'm doing for the Universidade Federal de Sergipe (UFS), Universidade
Federal de Pelotas (UFPEL), both from Brazil (and there are other universitys) about Applied Mindlin microstructure
and i'm at the moment coding the Asymptotic Homogenization Method with a rapdily oscilating property of the medium analysed.


before going to the code, notice that i'm brazilian, and translate code, despite being necessary
in the future, is not a priority at the moment, and for pratical reasons i'm gonna keep the code
in portuguese for now, so if you don't know any portuguese be aware of that (if you still interested
in viewing this research in the short term, there's some more text scroll down and, maybe, try 
google translate, or maybe even learn portuguese, it's up to you, good luck!).

futurely imma code the finite element method as well.

para pessoas que entendem português:
resumo:
pesquisa utilizando matplotlib e numpy do python e um monte de codigo em c++ (para otimização) para analisar
estruturas com uma propiedade rapidamente oscilante 

esse código é uma ferramenta para a pesquisa que estou desenvolvendo pela Universidade Federal de Sergipe (UFS),
Universidade Federal de Pelotas (UFPEL), ambas do Brasil (há outras com as quais não tive tanto contato), sobre 
a teoria microestrutural de Mindlin aplicada e estou no momento fazendo o código para o método de Homogeneização
Assintótica com uma propridamente do meio analisado que rapidamente oscila.

Antes de ir ao código, se você fala português, será tranquilo entender maior parte das funções e constantes que
estão nele inseridas (o codigo c++ ta muito mal organizado, mas tentei manter tudo o mais "entendível" possivel,
já peço desculpas de antemão, sou novo nesse mundo do c++)

futuramente irei também fazer um código para o metodo de elementos finitos.

ao código:

existem diversas formas de se calcular a propiedade analisada pelo método da homogeneização assintótica, o código foca
em duas mais um exemplo de cada para cada caso.
essas duas formas são:
1-forma exata do problema
-é abordada a integração direta da modelagem matemática elíptica;
-é possível ver no "rascunho_metodo_exato.png" as integrações (a ser substituído a posteriori) ;
-o código main.py pode ser usado para plotar os gráficos desejados;
-o código está em forma de uma função "continuo_exato_geral.py" que realiza as operações no código "continuo_exato.cpp",
 o qual se encontra na pasta "magia_cpp", se o leitor não está familizarizado com a linguagem c++, por favor ver o codigo
 "velhocaso_continuo_geral_real.py" que se encontra na pasta "velho", esse código é mais user-friendly e melhor de entender
 a lógica e tentar conciliar o código com a teoria no rascunho.
 
2-forma aproximada por expansão assintótica e homogeneização matemática
-é abordada a aproximação com duas funções para aproximação, mas é possível também ver as de menor grau;
-nesse temos várias funções, que se apresentam no rascunho "rascunho_metodo_aproximado.png", e que citando são:
  -u0;
  -u1 (chamada de ue1 no arquivo velho);
  -u2 (chamada de ue2 no arquivo velho);
  -N1;
  -N2;
  -funcao_a (função de propriedade do meio analisado);
  -funcao_f;
  -funcao_F (primeira anti-derivada de funcao_f).
-como mostrado no rascunho, as funções u dependem das N (exceto a 0) e todas podem ser chamadas ao mesmo tempo, ler instruções
 de uso no main para saber como usar os gráficos;
-como o metodo exato, pode ser muito confuso o codigo em c++, então tente o equivalente da pasta "velho" o arquivo 
 "velhocaso_continuo_geral_aproximado.py".
 
É importante observar que, por acaso, essas duas são um caso do geral, pois contemplam apenas propiedades rapidamente oscilantes
e-periódicas CONTINUAMENTE DERIVÁVEIS, ou seja, não se aplicam aos casos em que há saltos de na função de propriedade (funcao_a)
