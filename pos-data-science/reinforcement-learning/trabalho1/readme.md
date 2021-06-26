# Trabalho 1 da Disciplina de Reinforcement Learning
O objetivo deste trabalho é utilizar criar um Agente que utilize Q-learning para aprender a se deslocar em um _grid world_ pegar um objeto e levar ele até uma base. 

A configuração do mundo é a seguinte:
- 6 linhas X 7 colunas;
- 8 paredes;
- 1 objeto;
- 3 casas que representam a base;

Representação do mundo:
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| 0 |   |   | B | B | B |   |   |
| 1 |   |   |   | X |   |   |   |
| 2 |   |   |   | O |   |   |   |
| 3 |   |   |   |   |   |   |   |
| 4 | X | X |   | X | X | X | X |
| 5 | A |   |   |   |   |   | X |

Legenda:
- A = Agente, posição inical (5, 0);
- O = Objeto;
- B = Base;
- X = Paredes, local por onde o Agente e o Objeto não podem passar;

## Ações, restrições e condições:
O agente tem 5 movimentos: ir para direita, ir para esquerda, ir para cima, ir para baixo, ficar parado. O agente não pode se mover para onde exista uma parede ou se mover para a o local do Objeto nem sair do mundo. Ao se mover para a direita ou para a esquerda do Objeto, o agente irá pegar ele automaticamente e não o soltará. Quando o agente estiver com o Objeto passa a ocupar duas células da tabela. As mesmas restrições de movimentação do agente em relação as paredes e a saída do mundo se aplicam ao Objeto. Cada época da simulação dura até o agente levar o Objeto a base ou até o o número de movimento do agente atigir o número máximo de movimentos permitidos por época.


## Setup
- Ter Jupyter Notebook
- Ter a seguintes versões de libs:
```
matplotlib: 3.3.4
numpy: 1.20.2
```
Este trabalho foi feito usando o Anaconda.

## Execução
Rodar as células do notebook na ordem em que elas aparecem. É possível mudar alguns parâmetros e configurações, mas tenha em mente que o código pode apresentar algumas inconsistências já que ele só foi testado para o cenário do trabalho

## Saídas
No final do notebook, depois da simulação, são apresentadas 3 imformações:
- O total de tempo (em segundos) da simulação;
- Um gráfico informando quantos movimentos o agente usou para concluir cada época;
- Um gráfico informando quanto tempo (em segundos) cada época durou.

## Autor
Evandro Matheus Schmitz
