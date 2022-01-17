
# Author Edwin G.W. Peters
# Email edwin.peters@unsw.edu.au
# date 2022-01-12

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from scipy.signal import spectrogram
import numpy as np


# global config
pg.setConfigOptions(antialias=True, leftButtonPan=True, imageAxisOrder='row-major')


def pyqtspecgram(sig, NFFT, Fs, Fc=0., **kwargs):
    """
    Plot a spectrogram pyplot style using pyqtgraph

    Compute and plot a spectrogram of data in x. Data are split into NFFT length segments and the spectrum of each section is computed using scipy's spectrogram method. The windowing function window is applied to each segment, and the amount of overlap of each segment is specified with noverlap. The spectrogram is plotted as a colormap (using pyqtgraph).
    """
    f_a, t_a, Sa = spectrogram(sig, fs=Fs, return_onesided=False, nfft=NFFT, noverlap=0, detrend=False, nperseg=NFFT, window=('tukey', 0.0), scaling='density')
    f_a = np.fft.fftshift(f_a) + Fc
    lSa = np.fft.fftshift(10 * np.log10(Sa), axes=0)

    win = pg.GraphicsLayoutWidget(show=True, title='Spectrogram')

    win.resize(1000, 800)
    win.setWindowTitle('Waterfall')

    # pg.dbg() # debugging?

    # label to print the coordinates
    label = pg.LabelItem(justify='right')
    win.addItem(label)

    plot = win.addPlot(row=1, col=0)

    plot.setXRange(0, lSa.shape[1] * NFFT / Fs)
    plot.setYRange(Fc + -Fs / 2, Fc + Fs / 2)
    plot.setLabel(axis='left', text='Frequency [Hz]')
    plot.setLabel(axis='bottom', text='time [s]')
    # set scroll limits
    plot.setLimits(xMin=t_a[0] - (t_a[10] - t_a[0]), xMax=t_a[-1] + (t_a[10] - t_a[0]),
                   yMin=f_a[0] - (f_a[10] - f_a[0]), yMax=f_a[-1] + (f_a[10] - f_a[0]))

    # Fit the plot to the axes
    tr = tr = QtGui.QTransform()
    tr.translate(0, Fc - Fs / 2)
    tr.scale(NFFT / Fs, Fs / NFFT)

    img = img = pg.ImageItem(border='w')
    # img.setImage(tt[0][:, :, 1:].astype(np.uint16))
    img.setImage(lSa)
    img.setTransform(tr)

    # Colourmap
    # cmap = pg.colormap.get('CET-L9')
    cmap = cmap = pg.colormap.get('viridis')  # matplotlib style
    minv, maxv = np.nanmin(np.nanmin(lSa[lSa != -np.inf])), np.nanmax(np.nanmax(lSa))
    bar = bar = pg.ColorBarItem(interactive=True, values=(minv, maxv), colorMap=cmap, label='magnitude [dB]')
    bar.setImageItem(img, insert_in=plot)

    plot.addItem(img)
    plot.showAxes(True)
    # plot.invertY(True)

    vb = vb = plot.vb

    def coord_to_loc(x, y):
        freq_loc = int(np.round((y - Fc + Fs / 2) * NFFT / Fs))
        time_loc = int(np.round(x / NFFT * Fs))

        return(time_loc, freq_loc)

    def mouseMoved(evt):
        pos = evt[0]  # using signal proxy turns original arguments into a tuple
        if plot.sceneBoundingRect().contains(pos):
            mousePoint = vb.mapSceneToView(pos)
            x_coord = mousePoint.x()
            y_coord = mousePoint.y()
            # time_loc = t_a[x_coord]
            # freq_loc = f_a[y_coord]
            if x_coord >= t_a[0] and x_coord <= t_a[-1]:
                if y_coord >= f_a[0] and y_coord <= f_a[-1]:
                    # label.setText(f"<span style='font-size: 12pt'> x: {mousePoint.x():g}, y: {mousePoint.y():g}  </span>")
                    tl, fl = coord_to_loc(x_coord, y_coord)
                    label.setText(f"<span style='font-size: 12pt'> x={mousePoint.x():g}, y={mousePoint.y():g}, mag={lSa[fl,tl]:g} dB  </span>")

    proxy = pg.SignalProxy(img.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

    # Not working yet. Check proper event connections. It seems like the integrated Qt mouse event overrides this

    # def on_double_click_out(event):
    #     mouseEvent = event[0]
    #     mousePoint = mouseEvent.pos()
    #     print('clicked!')
    #     if mouseEvent.double():
    #         print("Double click")
    #     if plot.p1.sceneBoundingRect().contains(mousePoint):
    #         print('x=', mousePoint.x(), ' y=', mousePoint.y())

    # pg.SignalProxy(img.scene().sigMouseClicked, rateLimit=60, slot=on_double_click_out)

    pg.exec()

    return Sa, f_a, t_a, pg
