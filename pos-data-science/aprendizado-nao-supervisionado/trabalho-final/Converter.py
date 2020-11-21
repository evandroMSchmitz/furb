import argparse

import cv2 as cv
import os

def convert_to_dataset_image(path: str, write_path: str, image_label: str, start_id: int):
    
    for root, _, files in os.walk(path):
        image_files = [os.path.join(root, file) for file in files if file.endswith(".jpg")]

    image_id = start_id
    for file_name in image_files:
        img = cv.imread(file_name, cv.IMREAD_GRAYSCALE)

        # Muda o tamanho para o padrão da base OLR 70x80
        dst = cv.resize(img, (70, 80))

        cv.imwrite(f"{write_path}\{image_id}_{image_label}.jpg", dst)
        image_id += 1

# Argumentos para rodar o arquivo
parser = argparse.ArgumentParser()

parser.add_argument(
    '-c', 
    '--convertpath', 
    type=str,
    default='.\imagens',
    help='Caminho para as imagens que se deseja converter')

parser.add_argument(
    '-d', 
    '--databasepath', 
    type=str,
    default='.\dataset\ORL2',
    help='Caminho para a base de dados para escrever os arquivos')

parser.add_argument(
    '-il', 
    '--image_label', 
    type=str,
    required=True,
    help='Label do conjunto de imagens')

parser.add_argument(
    '-si', 
    '--start_id', 
    type=int,
    default=401,
    help='Id inicial da primeira imagem, o resto será incrementado sequencialmente')

args = parser.parse_args()

convert_to_dataset_image(args.convertpath, args.databasepath, args.image_label, args.start_id)