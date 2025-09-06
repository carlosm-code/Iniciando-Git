import numpy as np
import random

class Estudiante:
    def __init__(self, codigo, nombre, promAc, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.promAc = promAc
        self.programa = programa
    
    def informacion(self):
        print(f"Estudiante {self.codigo}, nombre: {self.nombre}, promedio: {round(self.promAc,2)}, carrera: {self.programa}")

def generarEstudiantes():
    totalEstudiantes = np.empty(6500, dtype=object)
    nombres = ["Carlos", "Jesus", "Daniel", "Sebastian", "Nicolas", "Camilo"]
    for i in range(6500):
        codigo = random.randint(19800000, 20250000)
        nombre = random.choice(nombres)
        promAc = random.uniform(0.0, 5.0)
        programa = random.randint(11, 15)
        totalEstudiantes[i] = Estudiante(codigo, nombre, promAc, programa)
    return totalEstudiantes

def estudiantesBuenPromedio(totalEstudiantes):
    print("------Parte 1------")
    print("Ingrese la carrera que desea verificar: 11 Sistemas, 12 Industrial, 13 Civil, 14 Quimica, 15 Electronica")
    carrera = int(input())
    while carrera < 11 or carrera > 15:
        print("Por favor ingrese un valor adecuado del 11 al 15")
        carrera = int(input())

    contador = 0
    for est in totalEstudiantes:
        if est.promAc >= 4.0 and est.programa == carrera:
            contador += 1
            est.informacion()

    print("--------------------------------------------------------------")
    print(f"Hubieron {contador} estudiantes que cumplieron con la condición")
    print("--------------------------------------------------------------")

def estudiantesAntiguos(totalEstudiantes):
    print()
    print("------Parte 2------")
    contador = 0
    for est in totalEstudiantes:
        if est.promAc >= 2.7 and est.promAc < 3.2:
            temp = str(est.codigo)[:3]   
            if int(temp) <= 198:         
                contador += 1
                est.informacion()

    print("--------------------------------------------------------------")
    print(f"Hubieron {contador} estudiantes que cumplieron con la condición")
    print("--------------------------------------------------------------")

def main():
    estudiantes = generarEstudiantes()
    estudiantesBuenPromedio(estudiantes)
    estudiantesAntiguos(estudiantes)

if __name__ == "__main__":
    main()