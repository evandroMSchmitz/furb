# Trabalho Final da Disciplina de Aprendizado de Máquina II - Aprendizado Não Supervisionado
Trabalho  que faz aplicação de PCA usando o algoritmo EigenFaces em na basede dados [ORL disponibilizada em aula](https://github.com/lobokoch/unsupervised-learning/blob/main/dataset/ORL.rar) com a adição de mais 10 imagens.

## Setup
- Ter python versão 3.9 instalado
- Executar o comando abaixo para instalar o opencv-contrib-python e numpy (recomenda-se fazer esta instalação em uma venv do python):
```console
pip install -r requirements.txt
```

## Executando
```console
python PCA.py
```
Este arquivo aceita os seguintes argumentos:
|Parâmetro|Significado|Valor padrão|
| --- | --- | --- |
|-p ou --databasepath| Caminho para a base de dados que será usada no treinamento e teste do algoritmo de Eigenfaces | .\dataset\ORL2 |

## Exemplo de Saída
```console
Dados de treino: 288 casos
Dados de teste: 123 casos
10 componentes principais, acurácia: 93.50%
Corretos: 115
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 671.2383089482505
********************
11 componentes principais, acurácia: 94.31%
Corretos: 116
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 704.744240450055
********************
12 componentes principais, acurácia: 95.12%
Corretos: 117
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 727.5108571986297
********************
13 componentes principais, acurácia: 95.12%
Corretos: 117
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 744.689468839175
********************
14 componentes principais, acurácia: 95.12%
Corretos: 117
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 773.2679991418419
********************
15 componentes principais, acurácia: 95.12%
Corretos: 117
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 792.3140048147998
********************
16 componentes principais, acurácia: 95.12%
Corretos: 117
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 806.164441357056
********************
17 componentes principais, acurácia: 95.93%
Corretos: 118
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 826.7835694314474
********************
18 componentes principais, acurácia: 95.93%
Corretos: 118
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 842.8115075153814
********************
19 componentes principais, acurácia: 95.93%
Corretos: 118
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 859.6278299005254
********************
20 componentes principais, acurácia: 95.93%
Corretos: 118
Distância mínima: 2.2250738585072014e-308
Distância máxima: 1.7976931348623157e+308
Distância média: 876.983124159313
********************
```

## Conversor de imagens
Este trabalho também oferece um conversor de imagens simples para colocar imagens coloridas de qualquer tamanho no padrão da base de dados, que é escala de cinza de tamanho 70 x 80. Os requisitos para rodar o script de conversão são os mesmos para rodar o trabalho. Este arquivo deve ser rodado com 10 imagens de cada vez para garantir que o padrão da base seja mantido. Muitos dados são parametrizados, então é responsabilidade sua usar ele corretamente.

### Executando
```console
python Converter.py
```
Este arquivo aceita os seguintes argumentos:
|Parâmetro|Significado|Valor padrão|
| --- | --- | --- |
|-c ou --convertpath| Caminho para as imagens que se deseja converter | .\imagens |
|-d ou --databasepath| Caminho para a base de dados para escrever os arquivos | .\dataset\ORL2 |
|-il ou --image_label| Label do conjunto de imagens. Diferencia esta imagens das outras da base | - |
|-si ou --start_id| Id inicial da primeira imagem, o resto será incrementado sequencialmente | 401 |
