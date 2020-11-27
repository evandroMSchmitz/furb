import argparse

import cv2 as cv
import os
import numpy as np
import random
import sys

class Person():

    def __init__(self, id, label, data):
        self.id = id
        self.label = label
        self.data = data


def get_image_data(file_name):
    img = cv.imread(file_name, cv.IMREAD_GRAYSCALE)

    # Muda o tamanho para 80x80
    dst = cv.resize(img, (80, 80))

    #Converter para vetor coluna
    # shape = linha, coluna
    dst = dst.T.reshape((1, dst.shape[1] * dst.shape[0]))

    # Converte de 8 bits sem sinal, para 64 bits com sinal, preserva 1 canal apenas.
    data = np.float64(dst)
    return data


def to_person(file_name: str) -> Person:
    # D:\xx\1_1.jpg
    data_part = file_name[file_name.rfind("\\") + 1 : file_name.rfind(".jpg")]
    data = data_part.split("_")

    person = Person(int(data[0]), int(data[1]), get_image_data(file_name))
    return person


def load_dataset(path: str, p: int):
    train = []
    test = []
    for root, _, files in os.walk(path):
        image_files = [os.path.join(root, file) for file in files if file.endswith(".jpg")]

    people = [to_person(file) for file in image_files]
    people.sort(key=lambda person: person.id)

    num_samples_per_person = 10
    index = 0
    while index < len(people):
        samples = people[index: index + num_samples_per_person]

        while len(samples) > p:
            i = random.randint(0, len(samples) - 1)
            test.append(samples.pop(i))

        if p == num_samples_per_person:
            test.extend(samples)    

        train.extend(samples)

        index += num_samples_per_person
	
    return (train, test)

def run_EigenFaceRecognizer(path: str):
    train = []
    test = []
    p = 7; # holdout de 70/30, treino/teste
    train, test = load_dataset(path, p)

    start_comps = 10
    max_comps = 21

    print(f"Dados de treino: {len(train)} casos")
    print(f"Dados de teste: {len(test)} casos")

    for num_components in range(start_comps, max_comps):
        model = cv.face.EigenFaceRecognizer_create(num_components)
        src = []
        labels = []
        for person in train:
            src.append(person.data)
            labels.append(person.label)

        model.train(src, np.asarray(labels))

        max_distance = sys.float_info.min
        min_distance = sys.float_info.max
        mean_distance = 0
        corrects = 0
        true_positives = 0
        for person in test:
            label, confidence = model.predict(person.data)
            if person.label == label:
                corrects += 1
                true_positives += 1
            
            if confidence < min_distance:
                min_distance = confidence
            
            if confidence > max_distance:
                max_distance = confidence
            
            mean_distance += confidence

        acurracia = true_positives / len(test) * 100
        mean_distance /= len(test)
        print(f"{num_components} componentes principais, acurácia: {acurracia:.2f}%")
        print(f"Corretos: {corrects}")
        print(f"Distância mínima: {min_distance}")
        print(f"Distância máxima: {max_distance}")
        print(f"Distância média: {mean_distance}")
        print("*" * 20)

# Argumentos para rodar o trabalho
parser = argparse.ArgumentParser()

parser.add_argument(
    '-p', 
    '--databasepath', 
    type=str,
    default='.\dataset\ORL2',
    help='Caminho para a base de dados')

args = parser.parse_args()

run_EigenFaceRecognizer(args.databasepath)