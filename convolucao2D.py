import numpy as np
import matplotlib.pyplot as plt
import skimage.util as skiu

def convolucao2D(img,h):
    num_linhas = img.shape[0]
    num_colunas = img.shape[1]
    filtrada = np.zeros((num_linhas, num_colunas))
    for i in range(num_linhas):
        for j in range(num_colunas):
            for k in range(h.shape[0]):
                for l in range(h.shape[1]):
                    filtrada[i,j] += h[k,l]*img[i-k,j-1]
    return filtrada
    img = plt.imread('barbara.png')
    ruidosa = skiu.random_noise(img, 'gaussian', mean=0,var=0.008)
    plt.figure(1)
    plt.imshow(ruidosa,cmap='gray')
    plt.savefig('ruidosa.jpg')
    plt.show()

    n=5
    h = (1/n**2)*np.ones((n,n))

    saida= convolucao2D(ruidosa,h)

    plt.figure(2)
    plt.imshow(saida,cmap='gray')
    plt.savefig('saida.png')
    plt.show()
