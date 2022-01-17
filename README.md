# pyqtspecgram
Python spectogram plotted using pyqtgraph

Pyqtplot allows significantly faster navigation and zooming for larger scale waterfalls compared to pyplots specgram method.

See more on [https://github.com/epeters13/pyqtspecgram](https://github.com/epeters13/pyqtspecgram)

**Author**: Edwin G.W. Peters

## Requirements

 - scipy
 - pyqtgraph

## Installation
pip install pyqtspecgram

or

python setup.py install

## Usage
Check "test_pyqtspecgram" for an example

Plot a waterfall

```
from pyqtspecgram import pyqtspecgram
import numpy as np

Fs = 1e6
t = 5  # sec
N = int(t * Fs)
sigma_noise_2 = 0.1
NFFT = 4096

a = np.exp(1j * 2 * np.pi * 150e3 / Fs * np.arange(N))
a += np.exp(-1j * 2 * np.pi * 298e3 / Fs * np.arange(N))
a += np.sqrt(sigma_noise_2) / 2 * (np.random.randn(N) + 1j * np.random.randn(N))

Sxx, f_a, t_a, fig = pyqtspecgram(a, NFFT, Fs, Fc=0)
```

## Todo

 - Prevent garbage collection when returning from main thread to allow figure to remain open in the background in an interactive ipython console
 - Export coordinates in graph to console with double or right click
 - Allow dynamic time-averaged spectrogramming for very large data sets

