# Trabalho Final da Disciplina de Deep Learning
O objetivo deste trabalho é utilizar o PyTorch um modelo de recorrencia que permita classificar textos tempo como base de treinamento o IMDb.  

## Setup
- Ter Jupyter Notebook
- Ter a seguintes versões de libs:
```
matplotlib: 3.3.4
numpy: 1.20.2
pandas: 1.2.5
pytorch: 1.8.0
torchtext: 0.9.0
sklearn: 0.24.2
```
Este trabalho foi feito usando o Anaconda.

## Execução

Siga as instruções e execute célula a célula do notebook, mas cuidado as vezes durante a execução da importação do IMDb ocorrem erros estranhos, onde a base não é carregada corretamente e isso pode afetar o resto da execução do notebook.

Como contra partida você pode executar uma rede já treinada, seguindo as instruções que estão na seção **Definição para carregar o modelo, vocabulário e fazer um predict**.
Para isso você precisa baixar o arquivo do modelo já treinado, que se encontra [aqui](), e colocar ele na mesma pasta onde estão o `Trabalho.ipynb` e o `vocab.txt`, os três arquivos precisam estar juntos. Depois disso é só executar as células do **Definição para carregar o modelo, vocabulário e fazer um predict** e as que ele indicar que são necessárias e estão em outras partes do notebook.

## Referências

Este trabalho só foi possível graças a [este tutorial](https://towardsdatascience.com/sentiment-analysis-using-lstm-step-by-step-50d074f09948) escrito por Samarth Agrawal.

## Autor
Evandro Matheus Schmitz
