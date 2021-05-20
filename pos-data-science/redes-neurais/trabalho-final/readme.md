# Trabalho Final da Disciplina de Redes Neurais
O objetivo deste trabalho é utilizar o PyTorch para desenvolver redes reunais e aplicar elas em um problema de classificação de granulométricas de rochas. 

## Setup
- Ter Jupyter Notebook
- Ter a seguintes versões de libs:
```
matplotlib: 3.3.2
numpy: 1.19.2
pandas: 1.1.3
pytorch: 1.8.1
sklearn: 0.24.2
```
Este trabalho foi feito usando o Anaconda.

## Execução
Os códigos do trabalho bem como as anotações estão no notebook _Trabalho Final - Lithology Prediction.ipynb_. Foram testadas redes neurais e as que tiveram melhores resultados foram usadas para classificar o arquivo _hidden.csv_.

## Dataset de treinamento
O dataset de treinamento, o arquivo _lithology.csv_, é muito grande para ser colocado no repositório, mas ele pode ser encontrado neste [link](https://drive.google.com/file/d/1YkEBZaz_8RZFK5bzwAkkBksXWKefQfKC/view?usp=sharing).

## Saídas
Como saídas da execução existem duas configurações de pesos de duas redes treinadas (arquivos _prediction_ModelSimples.pth_ e _prediction_Model2Camadas.pth_), que foram escolhidas com base nos vários testes feitos.
Também existem os arquivos _df_hidden_lithology_ModelSimples.csv_ e _df_hidden_lithology_Model2Camadas.csv_ que contém o resutlado da classificação do arquivo _hidden.csv_.

Os pesos do arquivo _prediction_ModelSimples.pth_ e a classificação do arquivo _df_hidden_lithology_ModelSimples.csv_ foram gerados com o modelo escolhido utilizando uma proporção treino/teste de 80/20. Já os pesos do _prediction_Model2Camadas.pth_ e a classificação do _df_hidden_lithology_Model2Camadas.csv_ foram gerados usando uma configuração de rede diferente escolhida depois de alguns testes usando uma proporção de treino/teste/validação de  60/20/20, para mais informações olhar o notebook. A divisão de validação só foi feita mais no final do trabalho, então alguns dos atributos utilizados para fazer o treinamento e o teste podem ter um certo viés, visto que já tinha sido testa antes, mas com outro modelo de divisão.

Independente do modelo escolhido o treino final antes da classificação foi feito utilizando o dataset _lithology.csv_ completo, aplicando as normalizações e os métodos de treino que deram os melhores resultados.

## Para a avaliação do trabalho
Para a avaliação do trabalho o arquivo que deve ser considerado é o **df_hidden_lithology_Model2Camadas.csv**.

## Autor
Evandro Matheus Schmitz
