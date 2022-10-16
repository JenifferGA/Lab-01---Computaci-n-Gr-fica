from typing import List
import math


class Modeling:
    pass

#Clase para realizar las operaciones de los vectores.
class OperacionesVectores:

    def __init__(self) -> None:
        pass

    #a.1 Operacion de suma de un vector por un escalar.
    def OperSuma(self, *vectores) -> list:
        resultado: List[float] = []
        resultado = vectores[0]
        for i in range(1, len(vectores)):
            vector = vectores[i]
            for j in range(len(vector)):
                resultado[j] += vector[j]
        return resultado

    #a.2 Operacion de resta de un vector por un escalar.
    def OperResta(self, *vectores) -> list:
        resultado: List[float] = []
        resultado = vectores[0]
        for i in range(1, len(vectores)):
            vector = vectores[i]
            for j in range(len(vector)):
                resultado[j] -= vector[j]
        return resultado

    #a.3 Operación de multiplicación de un vector por un escalar.
    def OperMultEscalar(self, vector, escalar) -> list:
        for i in range(len(vector)):
            vector[i] *= escalar
        return vector


    # b. Multiplicación de vectores. (Debe estar en R3 para poder realizar esta operación)
    def crossProduct(self, vector1, vector2) -> list: 
        try:
            resultado = [
                vector1[1]*vector2[2] - vector1[2]*vector2[1],
                -(vector1[0]*vector2[2] - vector1[2]*vector2[0]),
                vector1[0]*vector2[1] - vector1[1]*vector2[0],
            ]

            return resultado
        except IndexError:
            print("Para realizar esta operación debe ingresar los vectores en R3")


    # c. Producto punto
    def productoPunto(self, vector1, vector2) -> float:
        resultado = 0
        for i in range(len(vector1)):
            resultado += vector1[i]*vector2[i]
        return resultado


    # d. División de un vector por un escalar    
    def operDivEscalar(self, vector, escalar) -> list:
        for i in range(len(vector)):
            operacion = vector[i] / escalar
            vector[i] = round(operacion,2)
        return vector


    # e. Calcular ángulo entre dos vectores

    # Función utlizada para retornar la norma de un vector
    def norma(self, vector) -> float:
        normaVector = 0
        for x in vector:
            normaVector += x**2
        return math.sqrt(normaVector)


    def operCalcAngulo(self, vector1, vector2) -> float:
        return round(math.degrees(math.acos(self.productoPunto(vector1, vector2)/
                            (self.norma(vector1)*self.norma(vector2)))),2)

    
    # f. Normalización de vectores
    def normalizacionVecs(self, vector):
        normaVector = self.norma(vector)
        resultadoVector = []

        for i in vector:
            resultadoVector.append(round((i/normaVector),2))

        return resultadoVector


   


