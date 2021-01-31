Algoritmos genéticos são algoritmos de busca baseados na mecânica da seleção natural e na genética natural, inspirado na teoria da evolução apresentada por Charlin Darwin 
Segundo Darwin, os indivíduos mais adaptados ao meio possuem mais chances de propagar suas caracterısticas, assim, seus hábitos também são passados para novas gerações e acabam por causar uma melhoria na espécie, um exemplo de evolução de espécie é a evolução do própriohomo sapiens. 

Os algoritmos genéticos usam estratégias elitistas de sobrevivência dos indivíduos mais aptos e usam fragmentos desses indivíduos para formação de novos indivíduos para a próxima geração. Esses algoritmos são genéricos o bastante para resolver problemas de naturezas diferentes, em geral, são promissores para resolver problemas que não possuem soluções analíticas simples e que uma boa aproximação é satisfatória para o usuário. É um algoritmo que trabalha com um conjunto de soluções candidatas, esse  conjunto é denominado população, cada indivíduo dessa população possui uma codificação de uma solução candidata do problema a ser tratado. Esses indivíduos são submetidos a um cálculo de aptidão (fitness) que é realizado por uma função objetivo, essa função mapeia a codificação nos parâmetros que se deseja ajustar através do AG e calcula o quão próxima a solução candidata está da solução desejada. Tanto a codificação quanto a função podem ser direta ou necessitar de funções auxiliares de mapeamento.

Existem várias questões que podem mudar de acordo com o problema a ser resolvido, as mais importantes são as questões relativas à função objetivo escolhida e a representação, sendo que a segunda reflete na implementação de detalhes de todos os operadores genéticos. As principais questões são as listadas a seguir:

Função objetivo;   
Tipo de representação;     
Estratégia de seleção;   
Cruzamento (taxa);    
Mutação (taxa);    
Elitismo 
