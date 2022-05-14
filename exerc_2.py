from tempfile import tempdir
import numpy as np
import cv2 as cv

def showImage( img ):
    from matplotlib import pyplot as plt
    plt.imshow(img)
    plt.show()

def getColor(img, i, j):
    return img.item(i, j, 0), img.item(i, j, 1), img.item(i, j, 2)

def setColor(img, i, j, b, g, r):
    img.itemset((i, j, 0), b)
    img.itemset((i, j, 1), g)
    img.itemset((i, j, 2), r)
    return 

def cutOffQuarter( img, quarter ):
    altura, largura = img.shape

    first_quarter = img[0:int(altura/2), 0:int(largura/2)]
    second_quarter = img[0:int(altura/2), int(largura/2):largura]
    third_quarter = img[int(altura/2):altura, 0:int(largura/2)]
    fourth_quarter = img[int(altura/2):altura, int(largura/2):largura]

    if quarter == 1 :    
        return first_quarter 
    elif quarter == 2 :    
        return second_quarter 
    elif quarter == 3 :    
        return third_quarter 
    elif quarter == 4 :    
        return fourth_quarter 

def trocaRegioes( img ):
    cv.imwrite("imgs/temp_shift.png", img)
    tempImg = cv.imread("imgs/temp_shift.png", 0)

    altura, largura = img.shape

    tempImg[0:int(altura/2), 0:int(largura/2)] = cutOffQuarter(img, 4)
    tempImg[0:int(altura/2), int(largura/2):largura] = cutOffQuarter(img, 3)
    tempImg[int(altura/2):altura, 0:int(largura/2)] = cutOffQuarter(img, 2)
    tempImg[int(altura/2):altura, int(largura/2):largura] = cutOffQuarter(img, 1)

    return tempImg

def invertRegions( img ):
    y1 = input('y1: ')
    x1 = input('x1: ')
    y2 = input('y2: ')
    x2 = input('x2: ')

    rectangle = img[int(y1):int(y2), int(x1):int(x2)]
    altura, largura = rectangle.shape

    for i in range (0, altura):
        for j in range(0, largura):
            rectangle.itemset((i, j), 255-(rectangle.item(i, j)))

    img[int(y1):int(y2), int(x1):int(x2)] = rectangle

    cv.imwrite("imgs/maui_inverted.png", img)

    return img
    
def main():
    img = cv.imread("imgs/maui.jpg", 0)
    cv.imwrite("imgs/maui_shifted.png", trocaRegioes(img))
    showImage(trocaRegioes(img))


#main()

img = cv.imread("imgs/maui.jpg", 0)
showImage(invertRegions(img))


