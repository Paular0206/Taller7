# Importar biblioteca Numpy con su alias
import numpy as np

# Crear un arreglo 
X=np.array([[2,5,7],[1,6,3],[4,9,0]])

# Calcular los valores y vectores propios 
A, B=np.linalg.eig(X)
# La función np.linalg.eig() calcula los valores propios y vectores propios de una matriz. Esta funcion solo admite
# una matriz cuadrada como entrada. La variable A almacena los valores propios y la variable B almacena los vectores propios.

# Imprimir resultado
print("Valores propios:", A)
print("Vectores propios:")
for i in range(len(B.T)):
    print(B[:, i])