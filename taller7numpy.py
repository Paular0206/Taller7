import numpy as np 
x= np.array([[2,5,3],[9,5,8],[2,3,80]])

valores, vectores= np.linalg.eig(x)

print("Valores propios", valores)
print("Vectores propios", vectores)
