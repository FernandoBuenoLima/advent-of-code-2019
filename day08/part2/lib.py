WIDTH = 25
HEIGHT = 6
#WIDTH = 3
#HEIGHT = 2
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

def layerArrayToMatrix(arrLayer):
    matrixLayer = []
    for i in range(HEIGHT):
        matrixLayer.append(arrLayer[i*WIDTH:(i+1)*WIDTH])
    return matrixLayer

def getLayersAsMatrices(input):
    arrLayers = getLayersAsArrays(input)
    return [layerArrayToMatrix(arrl) for arrl in arrLayers]

def addLayerToBottomOfImage(image, layer):
    for j in range(WIDTH):
        for i in range(HEIGHT):
            if image[i][j] == 2:
                image[i][j] = layer[i][j]

def printImage(image):
    for line in image:
        print(line)