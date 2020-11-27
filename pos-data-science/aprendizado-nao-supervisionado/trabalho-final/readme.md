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
10 componentes principais, acurácia: 90.24%
Corretos: 111
Distância mínima: 134.88780590312552
Distância máxima: 2338.630704335874
Distância média: 686.21093745969
********************
11 componentes principais, acurácia: 91.06%
Corretos: 112
Distância mínima: 136.2279150930823
Distância máxima: 2373.9400191038385
Distância média: 716.3938158437263
********************
12 componentes principais, acurácia: 92.68%
Corretos: 114
Distância mínima: 140.79395558417872
Distância máxima: 2461.5880132695065
Distância média: 743.4790726202218
********************
13 componentes principais, acurácia: 93.50%
Corretos: 115
Distância mínima: 140.79410628434243
Distância máxima: 2462.3970937422
Distância média: 762.1586435102096
********************
14 componentes principais, acurácia: 93.50%
Corretos: 115
Distância mínima: 140.8091650638214
Distância máxima: 2484.5877221689825
Distância média: 783.5716169188278
********************
15 componentes principais, acurácia: 93.50%
Corretos: 115
Distância mínima: 141.3500503751107
Distância máxima: 2565.024367535039
Distância média: 811.30986398111
********************
16 componentes principais, acurácia: 94.31%
Corretos: 116
Distância mínima: 149.16879305729503
Distância máxima: 2668.7398928411267
Distância média: 830.0657538072555
********************
17 componentes principais, acurácia: 95.12%
Corretos: 117
Distância mínima: 155.64011999342412
Distância máxima: 2670.411396670196
Distância média: 845.3228385775507
********************
18 componentes principais, acurácia: 94.31%
Corretos: 116
Distância mínima: 166.9409661461254
Distância máxima: 2688.16396096212
Distância média: 859.224249338427
********************
19 componentes principais, acurácia: 94.31%
Corretos: 116
Distância mínima: 172.28431892494157
Distância máxima: 2692.445881385788
Distância média: 871.9779875048241
********************
20 componentes principais, acurácia: 94.31%
Corretos: 116
Distância mínima: 186.20232558722697
Distância máxima: 2812.7502829468212
Distância média: 886.7705964099902
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
