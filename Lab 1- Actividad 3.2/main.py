from operaciones import OperacionesVectores

# Imprimir operaciones realizadas a los vectores
operacion = OperacionesVectores()


# a. Operación de suma
print("\n*****************************************************")
print("Operación de suma")
print(operacion.OperSuma([3, 5, 4], [-1, 8, 2])) 
print(operacion.OperSuma([1, 6, -9], [13, 21, -10], [-8, 24, 25])) 


# a. Operación de resta
print("\n*****************************************************")
print("Operación de resta")
print(operacion.OperResta([4, 1, 2], [3, 5, 8]))
print(operacion.OperResta([3, 8, -7], [14, 27, -10], [-13, 31, 5]))


# a. Operación de multiplicación de un vector por un escalar
print("\n*****************************************************")
print("Operación de multiplicación de un vector por un escalar")
print(operacion.OperMultEscalar([3, 5, 8], 7)) 
print(operacion.OperMultEscalar([-21, 8, 16], -2))


# b. Multiplicación de vectores (cross product)
print("\n*****************************************************")
print("Operación de multiplicación de vectores")
print(operacion.crossProduct([3, 5, 4], [-1, 8, 2]))
print(operacion.crossProduct([5, 11, 10], [9, 18, 12]))


# c. Producto interno (producto punto)
print("\n*****************************************************")
print("Operación producto punto")
print(operacion.productoPunto([3, 7, 10], [14, 2, 9]))
print(operacion.productoPunto([5, 8, -13], [-5, 41, 3]))


# d. División de un vector por un escalar
print("\n*****************************************************")
print("Operación de división de un vector por un escalar")
print(operacion.operDivEscalar([20, 15, 32], 5))
print(operacion.operDivEscalar([35, 44, 12], 6))


# e. Calcular ángulo entre dos vectores
print("\n*****************************************************")
print("Cálculo del ángulo entre dos vectores")
print(operacion.operCalcAngulo([3, 5, 4], [-1, 8, 2]))
print(operacion.operCalcAngulo([20, 15, 32], [35, 44, 12]))


# e. Normalización de vectores
print("\n*****************************************************")
print("Operación de normalización de vectores")
print(operacion.normalizacionVecs([6, 9, 13]))
print(operacion.normalizacionVecs([21, 10, 16]))
