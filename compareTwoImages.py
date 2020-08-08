from PIL import Image #pip3 install pillow
import numpy as np
import os
import re

#https://note.nkmk.me/en/python-numpy-image-processing/

def isDifferenceImage(pathImage1, pathImage2, threshold):
    image1 = Image.open(pathImage1)
    image2 = Image.open(pathImage2)
    numpy_image = np.array(image1)
    numpy_image2 = np.array(image2)
    # print(numpy_image)
    anchoX, altoY, z = numpy_image.shape
    anchoX2, altoY2, z2 = numpy_image2.shape
    # print(str(anchoX) + " image 1")
    # print(str(anchoX2) + " image 2")
    norma = np.divide(numpy_image, 255)  # normalizamos el arreglo
    norma2 = np.divide(numpy_image2, 255)  # normalizamos el arreglo
    np_round = np.round(norma, 2)
    np_round2 = np.round(norma2, 2)
    tempMatx = np.abs(np.subtract(np_round, np_round2))
    #    print(tempMatx)
    # print(numpy_image.shape)
    list = [0, 0, 0]
    matx_diff = np.array(list)
    step = 5
    for x in range(0, anchoX ,step):
        for y in range(0, altoY, step):
            # print(tempMatx[x, y])
            matx_diff = np.add(matx_diff, tempMatx[x, y])
    # print('>>>>> Diff')
    # print(matx_diff)  # redondeamos a 2 digitos
    total = np.sum(matx_diff).round(2)
    print("total > "+str(total))
    if total > threshold:
        return True
    else:
        return False


def tryint(s):
    try:
        return int(s)
    except ValueError:
        return s


def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [tryint(c) for c in re.split('([0-9]+)', s)]


def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)


def deleteDuplicateFiles(mypath, threshold):
    conta = 0
    image1 = ''
    image2 = ''
    files = os.listdir(mypath)
    sort_nicely(files)
    for file in files:
        if conta == 0:
            image1 = file
            print("image1: "+os.path.join(mypath, image1))
        else:
            image2 = file
            print("image1: " + image1 + " image2: " + image2)
            #aqui procesamos las imagenes
            isdiff = isDifferenceImage(os.path.join(mypath, image1), os.path.join(mypath, image2), threshold)
            print('>>>>> Is Different? = '+str(isdiff))
            if isdiff == False:
                os.remove(os.path.join(mypath, image2))
            else:
                image1 = image2
        conta += 1



if __name__ == '__main__':
    deleteDuplicateFiles(os.getcwd()+"/image", 1000)
    # pathImage1= os.getcwd()+"/image/frame-560.jpg"
    # pathImage2= os.getcwd() + "/image/frame-580.jpg"
    # isdiff = isDifferenceImage(pathImage1, pathImage2, 30000)
    # print('>>>>> Is Different? = '+str(isdiff))
