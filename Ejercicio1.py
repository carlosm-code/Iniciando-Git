import numpy as np
import random

class Candidatos:
    def __init__(self, numero, votos = 0):
        self.numero = numero
        self.votos = votos
    
    def informacion(self):
        print(f"Aspirante con el con el número: {self.numero}, tiene {self.votos} votos")

def generarVotos(listaAspirantes, votantes):
    for i in range(len(listaAspirantes)):
        temp = random.randint(0, votantes)
        votantes -= temp
        listaAspirantes[i].votos = temp
    print("Los votos han sido generados aleatoriamente")

def mostrarResultados(listaAspirantes):
    listaOrdenada = np.argsort([aspirante.votos for aspirante in listaAspirantes])[::-1]
    listaOrdenada = listaAspirantes[listaOrdenada]

    print("-----Resultados de las elecciones-----")
    for i in range(len(listaOrdenada)):
        listaOrdenada[i].informacion()

def main():
    numCandidatos = 30
    numVotantes = 5000

    listaAspirantes = np.empty(numCandidatos, dtype=object)
    for i in range(numCandidatos):
        listaAspirantes[i] = Candidatos(i+1)

    generarVotos(listaAspirantes, numVotantes)
    mostrarResultados(listaAspirantes)

if __name__ == "__main__":
    main()
