#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""
Example from section 1.3.1 of the turtorial.
"""

from tftb.generators import fmlin
import matplotlib.pyplot as plt
import numpy as np

n_points = 128
fmin, fmax = 0.0, 0.5
signal, _ = fmlin(n_points, fmin, fmax)

# Plot the energy spectrum of the chirp

dsp1 = np.fft.fftshift(np.abs(np.fft.fft(signal)) ** 2)
plt.plot(np.arange(-64, 64, dtype=float) / 128.0, dsp1)
plt.xlim(-0.5, 0.5)
plt.title('Spectrum')
plt.ylabel('Squared modulus')
plt.xlabel('Normalized Frequency')
plt.grid()
plt.show()
