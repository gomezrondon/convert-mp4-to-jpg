import cv2
import os
import shutil
from compareTwoImages import deleteDuplicateFiles

def deleteFiles(mypath):
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))


if __name__ == '__main__':
    filePath = 'C:/temp/full-desktop.mp4'
    filename = os.path.basename(filePath)
    vidcap = cv2.VideoCapture(filePath)
    success, image = vidcap.read()
    count=0
    sampling=20
    mypath = "image"
    if not os.path.exists(mypath):
        os.makedirs(mypath)
    else:
        deleteFiles(mypath)
    while success:
        if(count % sampling==0):
            cv2.imwrite(os.getcwd()+"/image/%d.jpg" % count, image)
        success, image = vidcap.read()
        #print('read a new frame: ', success)
        count += 1

    deleteDuplicateFiles(os.getcwd()+"/image", 10000)

    file_no_ext = os.path.splitext(filename)[0]
    shutil.make_archive(file_no_ext, 'zip', os.getcwd()+"/image")