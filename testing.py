from PIL import Image #pip3 install pillow
import numpy as np
import os


#https://www.easycalculation.com/analytical/distance.php
# a=Math.sqrt(Math.pow((x2-x1),2)+Math.pow((y2-y1),2));

def distTwoPoint(x1, y1, x2, y2):
    dist = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

def centerTwoPoints(x1, y1, x2, y2):
    if x1 > x2:
        cx = x2 + (x1 - x2)/2
    else:
        cx = x1 + (x2 - x1)/2

    if y1 > y2:
        cy = y2 +(y1 - y2)/2
    else:
        cy = y1 + (y2 - y1)/2


    return [cx, cy]

if __name__ == '__main__':
    image1 = Image.open(os.path.join(os.getcwd(), "test", "testimage.jpg"))
    numpy_image = np.array(image1)
    altoY, anchoX, z = numpy_image.shape
    print(str(anchoX) + " "+str(altoY))
    print(numpy_image)
    redPoints= []
    for y in range(0, altoY ):
        for x in range(0, anchoX):
            tempMatrx = numpy_image[y, x]
            if tempMatrx[0] > 230 and tempMatrx[1] < 50 and tempMatrx[2] < 50:
                print("Red >> " +str(tempMatrx) + " y, x = "+str(y)+", "+str(x))
                redPoints.append([x, y])
            if tempMatrx[0] > 230 and tempMatrx[1] > 210 and tempMatrx[2] < 20:
                print("Yellow >> " + str(tempMatrx) + " y, x = "+str(y)+", "+str(x))
            if tempMatrx[0] < 50 and tempMatrx[1] > 150 and tempMatrx[2] < 100:
                print("Green >> " + str(tempMatrx) + " y, x = "+str(y)+", "+str(x))

    for point in redPoints:
        print(point)

    dist = distTwoPoint(3, 4, 5, 4)
    print(dist)
    centerP = centerTwoPoints(3, 4, 5, 4)
    print(centerP)