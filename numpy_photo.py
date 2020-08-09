import os
from skimage import io
from PIL import Image #pip3 install pillow


if __name__ == '__main__':
    photo = io.imread(os.path.join(os.getcwd(), "test", "480.jpg"))
    print(photo.shape)
  #  img = Image.fromarray(photo[::-1], 'RGB') # reverso la imagen
  #  img = Image.fromarray(photo[:, ::-1], 'RGB') # flip horizontal
  #  algo = photo[::5, ::5] # el ::5 reduce la imagen en un 1/5
  #  algo = photo[50:150:1, ::1] # recorta un rect y=50 , x = 150
  #  algo = photo[50::1, ::1] # diferente: le quita 50 pix de arriba
  #  algo = photo[0:1:1, ::1]  #(1, 1920, 3) A:B:Scala, C:D:Scala, A >= B
  #  algo = photo[0:100:, ::]  #  (100, 1920, 3)
  #  algo = photo[100:200:, ::]  # (100, 1920, 3) OK
    altoY, anchoX, z = photo.shape
    altoYbox = int(altoY / 5)
    anchoXbox = int(anchoX / 5)
    print(altoYbox, anchoXbox)
    count=0
    for y in range(0, altoY  , altoYbox):
        for x in range(0, anchoX  , anchoXbox):
            yMas= y + altoYbox
            xMas= x + anchoXbox
            #print("y: "+ str(y) +" mas: "+str(yMas))
            print("x: "+ str(x) + " mas: " + str(xMas))
            algo = photo[y:yMas:, x:xMas:]  # (100, 100, 3) OK
           # print(algo.shape)
            img = Image.fromarray(algo, 'RGB')
            img.save(os.path.join(os.getcwd(), "test", 'my%d.png' % count))
            #img.show()
            count += 1



