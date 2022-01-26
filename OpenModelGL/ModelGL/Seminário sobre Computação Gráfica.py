
import numpy as np
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from skimage.filter import gabor_kernel
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Função utilizada para reescalar o kernel
def resize_kernel(aKernelIn, iNewSize):
    x = np.array([v for v in range(len(aKernelIn))])
    y = np.array([v for v in range(len(aKernelIn))])
    z = aKernelIn

    xx = np.linspace(x.min(), x.max(), iNewSize)
    yy = np.linspace(y.min(), y.max(), iNewSize)

    aKernelOut = np.zeros((iNewSize, iNewSize), np.float)    
    oNewKernel = interpolate.RectBivariateSpline(x, y, z)
    aKernelOut = oNewKernel(xx, yy)

    return aKernelOut


if __name__ == "__main__":
    fLambda = 3.0000000001   # comprimento de onda (em pixels)
    fTheta  = 0              # orientação (em radianos)
    fSigma  = 0.56 * fLambda # envelope gaussiano (com 1 oitava de largura de banda)
    fPsi    = np.pi / 2      # deslocamento (offset)

    # Tamanho do kernel (3 desvios para cada lado, para limitar cut-off)
    iLen = int(math.ceil(3.0 * fSigma))
    if(iLen % 2 != 0):
        iLen += 1

    # Obtém o kernel Gabor para os parâmetros definidos
    z = np.real(gabor_kernel(fLambda, theta=fTheta, sigma_x=fSigma, sigma_y=fSigma, offset=fPsi))

    # Plotagem do kernel

    fig = plt.figure(figsize=(16, 9))
    fig.suptitle(r'Gabor kernel para $\lambda=3.0$, $\theta=0.0$, $\sigma=0.56\lambda$ e $\psi=\frac{\pi}{2}$', fontsize=25)
    grid = gridspec.GridSpec(1, 2, width_ratios=[1, 2])
   fLambda = 3.0000000001
    # Gráfico 2D
    plt.gray()
    ax = fig.add_subplot(grid[0])
    ax.set_title(u'Visualização 2D')
    ax.imshow(z, interpolation='nearest')
    ax.set_xticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)
    ax.set_yticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)

    # Gráfico em 3D

    # Reescalona o kernel para uma exibição melhor
    z = resize_kernel(z, 300)
    # Eixos x e y no intervalo do tamanho do kernel
    x = np.linspace(-iLen/2, iLen/2, 300)
    y = x
    x, y = meshgrid(x, y)

    ax = fig.add_subplot(grid[1], projection='3d')
    ax.set_title(u'Visualização 3D')
    ax.plot_surface(x, y, z, cmap='hot')
fLambda = 3.0
# ou
fLambda = float(3)
    print(iLen)

    plt.show() 

import numpy as np
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from skimage.filter import gabor_kernel
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Função utilizada para reescalar o kernel
def resize_kernel(aKernelIn, iNewSize):
    x = np.array([v for v in range(len(aKernelIn))])
    y = np.array([v for v in range(len(aKernelIn))])
    z = aKernelIn

    xx = np.linspace(x.min(), x.max(), iNewSize)
    yy = np.linspace(y.min(), y.max(), iNewSize)

    aKernelOut = np.zeros((iNewSize, iNewSize), np.float)    
    oNewKernel = interpolate.RectBivariateSpline(x, y, z)
    aKernelOut = oNewKernel(xx, yy)

    return aKernelOut


if __name__ == "__main__":
    fLambda = 3              # comprimento de onda (em pixels)
    fTheta  = 0              # orientação (em radianos)
    fSigma  = 0.56 * fLambda # envelope gaussiano (com 1 oitava de largura de banda)
    fPsi    = np.pi / 2      # deslocamento (offset)

    # Tamanho do kernel (3 desvios para cada lado, para limitar cut-off)
    iLen = int(math.ceil(3.0 * fSigma))
    if(iLen % 2 != 0):
        iLen += 1

    # Obtém o kernel Gabor para os parâmetros definidos
    z = np.real(gabor_kernel(1.0/fLambda, theta=fTheta, sigma_x=fSigma, sigma_y=fSigma, offset=fPsi))

    # Plotagem do kernel

    fig = plt.figure(figsize=(16, 9))
    fig.suptitle(r'Gabor kernel para $\lambda=3.0$, $\theta=0.0$, $\sigma=0.56\lambda$ e $\psi=\frac{\pi}{2}$', fontsize=25)
    grid = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

    # Gráfico 2D
    plt.gray()
    ax = fig.add_subplot(grid[0])
    ax.set_title(u'Visualização 2D')
    ax.imshow(z, interpolation='bicubic')
    ax.set_xticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)
    ax.set_yticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)

    # Gráfico em 3D

    # Reescalona o kernel para uma exibição melhor
    z = resize_kernel(z, 300)
    # Eixos x e y no intervalo do tamanho do kernel
    x = np.linspace(-iLen/2, iLen/2, 300)
    y = x
    x, y = meshgrid(x, y)

    ax = fig.add_subplot(grid[1], projection='3d')
    ax.set_title(u'Visualização 3D')
    ax.plot_surface(x, y, z, cmap='hot')

    print(iLen)

    plt.show()
   g = np.zeros(y.shape, dtype=np.complex)
g[:] = np.exp(-0.5 * (rotx**2 / sigma_x**2 + roty**2 / sigma_y**2))
g /= 2 * np.pi * sigma_x * sigma_y                                   # <- DÚVIDA 1
g *= np.exp(1j * (2 * np.pi * frequency * rotx + offset))            # <- DÚVIDA 2
g = np.zeros(y.shape, dtype=np.complex)
g[:] = np.exp(-0.5 * (rotx**2 / sigma_x**2 + roty**2 / sigma_y**2))
g *= np.exp(1j * (2 * np.pi * rotx / frequency + offset))

return g
return g    
 mport numpy as np
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from skimage.filter import gabor_kernel
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def my_gabor_kernel(frequency, theta=0, bandwidth=1, sigma_x=None, sigma_y=None,
                 offset=0):
    if sigma_x is None:
        sigma_x = _sigma_prefactor(bandwidth) / frequency
    if sigma_y is None:
        sigma_y = _sigma_prefactor(bandwidth) / frequency

    n_stds = 3
    x0 = np.ceil(max(np.abs(n_stds * sigma_x * np.cos(theta)),
                     np.abs(n_stds * sigma_y * np.sin(theta)), 1))
    y0 = np.ceil(max(np.abs(n_stds * sigma_y * np.cos(theta)),
                     np.abs(n_stds * sigma_x * np.sin(theta)), 1))
    y, x = np.mgrid[-y0:y0+1, -x0:x0+1]

    rotx = x * np.cos(theta) + y * np.sin(theta)
    roty = -x * np.sin(theta) + y * np.cos(theta)

    g = np.zeros(y.shape, dtype=np.complex)
    g[:] = np.exp(-0.5 * (rotx**2 / sigma_x**2 + roty**2 / sigma_y**2))
    #g /= 2 * np.pi * sigma_x * sigma_y
    g *= np.exp(1j * (2 * np.pi * rotx / frequency + offset))

    return g

# Função utilizada para reescalar o kernel
def resize_kernel(aKernelIn, iNewSize):
    x = np.array([v for v in range(len(aKernelIn))])
    y = np.array([v for v in range(len(aKernelIn))])
    z = aKernelIn

    xx = np.linspace(x.min(), x.max(), iNewSize)
    yy = np.linspace(y.min(), y.max(), iNewSize)

    aKernelOut = np.zeros((iNewSize, iNewSize), np.float)    
    oNewKernel = interpolate.RectBivariateSpline(x, y, z)
    aKernelOut = oNewKernel(xx, yy)

    return aKernelOut


if __name__ == "__main__":
    fLambda = 3.0000001      # comprimento de onda (em pixels)
    fTheta  = 0              # orientação (em radianos)
    fSigma  = 0.56 * fLambda # envelope gaussiano (com 1 oitava de largura de banda)
    fPsi    = np.pi / 2      # deslocamento (offset)

    # Tamanho do kernel (3 desvios para cada lado, para limitar cut-off)
    iLen = int(math.ceil(3.0 * fSigma))
    if(iLen % 2 != 0):
        iLen += 1

    # Obtém o kernel Gabor para os parâmetros definidos
    z = np.real(my_gabor_kernel(fLambda, theta=fTheta, sigma_x=fSigma, sigma_y=fSigma, offset=fPsi))
    print(z.shape)

    # Plotagem do kernel

    fig = plt.figure(figsize=(16, 9))
    fig.suptitle(r'Gabor kernel para $\lambda=3.0$, $\theta=0.0$, $\sigma=0.56\lambda$ e $\psi=\frac{\pi}{2}$', fontsize=25)
    grid = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

    # Gráfico 2D
    plt.gray()
    ax = fig.add_subplot(grid[0])
    ax.set_title(u'Visualização 2D')
    ax.imshow(z, interpolation='bicubic')
    ax.set_xticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)
    ax.set_yticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)

    # Gráfico em 3D

    # Reescalona o kernel para uma exibição melhor
    z = resize_kernel(z, 300)
    # Eixos x e y no intervalo do tamanho do kernel
    x = np.linspace(-iLen/2, iLen/2, 300)
    y = x
    x, y = meshgrid(x, y)

    ax = fig.add_subplot(grid[1], projection='3d')
    ax.set_title(u'Visualização 3D')
    ax.plot_surface(x, y, z, cmap='hot')

    print(iLen)

    plt.show() 
import numpy as np
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
from skimage.filter import gabor_kernel
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def my_gabor_kernel(frequency, theta=0, bandwidth=1, sigma_x=None, sigma_y=None,
                 offset=0):
    if sigma_x is None:
        sigma_x = _sigma_prefactor(bandwidth) / frequency
    if sigma_y is None:
        sigma_y = _sigma_prefactor(bandwidth) / frequency

    n_stds = 3
    x0 = np.ceil(max(np.abs(n_stds * sigma_x * np.cos(theta)),
                     np.abs(n_stds * sigma_y * np.sin(theta)), 1))
    y0 = np.ceil(max(np.abs(n_stds * sigma_y * np.cos(theta)),
                     np.abs(n_stds * sigma_x * np.sin(theta)), 1))
    y, x = np.mgrid[-y0:y0+1, -x0:x0+1]

    rotx = x * np.cos(theta) + y * np.sin(theta)
    roty = -x * np.sin(theta) + y * np.cos(theta)

    g = np.zeros(y.shape, dtype=np.complex)
    g[:] = np.exp(-0.5 * (rotx**2 / sigma_x**2 + roty**2 / sigma_y**2))
    #g /= 2 * np.pi * sigma_x * sigma_y
    g *= np.exp(1j * (2 * np.pi * rotx / frequency + offset))

    return g

# Função utilizada para reescalar o kernel
def resize_kernel(aKernelIn, iNewSize):
    x = np.array([v for v in range(len(aKernelIn))])
    y = np.array([v for v in range(len(aKernelIn))])
    z = aKernelIn

    xx = np.linspace(x.min(), x.max(), iNewSize)
    yy = np.linspace(y.min(), y.max(), iNewSize)

    aKernelOut = np.zeros((iNewSize, iNewSize), np.float)    
    oNewKernel = interpolate.RectBivariateSpline(x, y, z)
    aKernelOut = oNewKernel(xx, yy)

    return aKernelOut


if __name__ == "__main__":
    fLambda = 3.0000001      # comprimento de onda (em pixels)
    fTheta  = 0              # orientação (em radianos)
    fSigma  = 0.56 * fLambda # envelope gaussiano (com 1 oitava de largura de banda)
    fPsi    = np.pi / 2      # deslocamento (offset)

    # Tamanho do kernel (3 desvios para cada lado, para limitar cut-off)
    iLen = int(math.ceil(3.0 * fSigma))
    if(iLen % 2 != 0):
        iLen += 1

    # Obtém o kernel Gabor para os parâmetros definidos
    z = np.real(my_gabor_kernel(fLambda, theta=fTheta, sigma_x=fSigma, sigma_y=fSigma, offset=fPsi))
    print(z.shape)

    # Plotagem do kernel

    fig = plt.figure(figsize=(16, 9))
    fig.suptitle(r'Gabor kernel para $\lambda=3.0$, $\theta=0.0$, $\sigma=0.56\lambda$ e $\psi=\frac{\pi}{2}$', fontsize=25)
    grid = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

    # Gráfico 2D
    plt.gray()
    ax = fig.add_subplot(grid[0])
    ax.set_title(u'Visualização 2D')
    ax.imshow(z, interpolation='bicubic')
    ax.set_xticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)
    ax.set_yticklabels([v for v in range((-iLen/2)-1, iLen/2+1)], fontsize=10)

    # Gráfico em 3D

    # Reescalona o kernel para uma exibição melhor
    z = resize_kernel(z, 300)
    # Eixos x e y no intervalo do tamanho do kernel
    x = np.linspace(-iLen/2, iLen/2, 300)
    y = x
    x, y = meshgrid(x, y)

    ax = fig.add_subplot(grid[1], projection='3d')
    ax.set_title(u'Visualização 3D')
    ax.plot_surface(x, y, z, cmap='hot')

    print(iLen)

    plt.show()
    
