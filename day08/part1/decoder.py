
WIDTH = 25
HEIGHT = 6
IMAGE_SIZE = WIDTH * HEIGHT

def getNumberOfLayers(input):
    return int(len(input) / IMAGE_SIZE)

def getLayersAsStrings(input):
    layers = []
    layerNumber = 0
    totalLayers = getNumberOfLayers(input)
    while layerNumber < totalLayers:
        layers.append(input[layerNumber*IMAGE_SIZE:(layerNumber+1)*IMAGE_SIZE])
        layerNumber += 1
    return layers

def getLayersAsArrays(input):
    layers = []
    layerNumber = 0
    totalLayers = getNumberOfLayers(input)
    while layerNumber < totalLayers:
        layer = []
        for i in range(IMAGE_SIZE):
            layer.append(int(input[(layerNumber * IMAGE_SIZE) + i]))
        layers.append(layer)
        layerNumber += 1
    return layers

def countDigitInLayer(layer, digit):
    count = 0
    for d in layer:
        if int(d) == digit:
            count += 1
    return count

with open("input.txt") as file:
    input = file.read()

layers = getLayersAsStrings(input)

layerWithLeastZeroes = 0
leastNumberOfZeroes = countDigitInLayer(layers[0], 0)

for i in range(1, getNumberOfLayers(input)):
    zeroes = countDigitInLayer(layers[i], 0)
    if zeroes < leastNumberOfZeroes:
        layerWithLeastZeroes = i
        leastNumberOfZeroes = zeroes

layer = layers[layerWithLeastZeroes]
answer = countDigitInLayer(layer, 1) * countDigitInLayer(layer, 2)

print(answer)
