import numpy as np
import scipy

def gen_sinusoidal(N):
    x = np.linspace(0, 2*scipy.pi, N)
    y = scipy.sin(x)
    noise = np.matlib.randn(N,1) * 0.2
    
    yv = np.matrix(y).T
    nv = np.matrix(noise)
    t = yv + nv
    return t

