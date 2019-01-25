from PIL import Image

imagePath = 'barbara.png'
im = Image.open(imagePath)
img = im.load()
newimdata = []
largura = im.size[0]
altura = im.size[1]
vetor = [0,0,0,0,0,0,0,0,0,0]
im.show()

for x in range(0,largura-1):
    for y in range(0,altura-1):
        i =0
        if x != 0 and y != 0:
            for valorx in range(x-1,x+2):
                for valory in range(y-1,y+2):
                    vetor[i] = img[valorx,valory]
                    i += 1
                #print(img[valorx,valory])
        elif x == 0 and y != 0:
            for valorx in range(x,x+3):
                for valory in range(y-1,y+2):
                    vetor[i] = img[valorx,valory]
                    i += 1
        elif x != 0 and y == 0:
            for valorx in range(x-1,x+2):
                for valory in range(y,y+3):
                    vetor[i] = img[valorx,valory]
                    i += 1
        else:
            for valorx in range(x,x+3):
                for valory in range(y,y+3):
                    vetor[i] = img[valorx,valory]
                    i += 1
        #print(vetor)
        vetor.sort()
        #print(vetor)
        #print(vetor[4])
        im.putpixel((x,y), vetor[4])
    
im.show()
im.save('MyImage.png')
