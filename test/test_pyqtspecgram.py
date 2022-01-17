import numpy as np
import sys
sys.path.append('../src')
from pyqtspecgram import pyqtspecgram

Fs = 1e6
t = 5  # sec
N = int(t * Fs)
sigma_noise_2 = 0.1
NFFT = 4096


a = np.exp(1j * 2 * np.pi * 150e3 / Fs * np.arange(N))
a += np.exp(-1j * 2 * np.pi * 298e3 / Fs * np.arange(N))
a += np.sqrt(sigma_noise_2) / 2 * (np.random.randn(N) + 1j * np.random.randn(N))


Sxx, f_a, t_a, fig = pyqtspecgram(a, NFFT, Fs, Fc=0)
