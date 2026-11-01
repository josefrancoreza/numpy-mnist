import numpy as numeros

imagen = numeros.zeros((28, 28), dtype=numeros.uint8)
lote = numeros.zeros((10,28, 28), dtype=numeros.uint8)


pixels = numeros.array([0,128,255], dtype=numeros.uint8)
normalizados = pixels.astype(numeros.float32)/255.0
print(normalizados)
