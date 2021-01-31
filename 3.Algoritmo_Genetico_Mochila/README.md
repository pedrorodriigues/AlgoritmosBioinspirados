O problema da mochila binária consiste em um problema de maximização da utilidade dos itens levados(v) restrito à capacidade da mochila(c). Formalmente, dados dois vetores vetores p e v de n posições e um número c, deseja-se encontrar um subconjunto X de {0, 1, , ..., n − 1} que maximize v(X) sob a restrição Pp(X) ≤ c. Diremos que 0, 1, 2, ..., n − 1 são os objetos do problema, p[i] é o peso do objeto i, e que v[i] é o valor(utilidade) do objeto i. Diremos que c é a capacidade da instância. Diremos ainda que um subconjunto X de {0, 1, 2, ..., n} ´e uma mochila se Pp(X) ≤ c. O valor de uma mochila X é dado pela função v(X), e nosso objetivo é encontrar uma mochila de valor máximo, e.g maximizar v(X). v(X) = X ∀i∈X v[i] 
Como já foi dito, existem várias questões que podem mudar de acordo com o problema a ser resolvido, as mais importantes são as questões relativas a função objetivo escolhida e a representação, sendo que a segunda reflete na implementação de detalhes de todos os operadores genéticos. As principais questões são as listadas a seguir:

Função objetivo com penalização;    
Representação;    
Estratégia de seleção;    
Cruzamento, pode ser feito o de n pontos;   
Mutação, pode ser feita a de negação do bit;   
Elitismo. 
