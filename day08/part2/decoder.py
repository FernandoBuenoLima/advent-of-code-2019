from lib import *

with open("input.txt") as file:
    input = file.read()

layers = getLayersAsMatrices(input)

image = layers[0]

for i in range(1, len(layers)):
    addLayerToBottomOfImage(image, layers[i])

printImage(image)
