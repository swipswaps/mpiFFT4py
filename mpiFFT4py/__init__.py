import pyximport
pyximport.install()
from cython.maths import *
from serialFFT import *
from slab import FastFourierTransform as slab_FFT
from pencil import FastFourierTransform as pencil_FFT
from line import FastFourierTransform as line_FFT
from mpibase import work_arrays, datatypes

