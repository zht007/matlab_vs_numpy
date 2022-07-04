
import numpy as np
from scipy.signal import firwin, butter, lfilter,filtfilt

def filter_2sFIR(sig,f,fs,n,type):

    """
    A two-stage FIR filter processing using the window method

    The  input arguments are identical to those used in FIRPM
    sig: is the signal to be filtered arranged, each row is a measurement
    f: a vector of cutoff frequencies in Hz. f is a number for lowpass and
        highpass filters, and is a two-element vector for bandpass or bandstop
        filter.
    fs: the sampling frequency.
    n: the order of FIR filter.
    type: 'low' for lowpass filter 'high' for highpass filter 
        'bandpass' for bandpass filter 'stop' for bandstop filter.
    win: assign the N+1 length window vector to window the impulse response. 
        (same way as in PWELCH). Default is hamming window.

    Details of input arguments and examples, please help FIR1.

    """
    b = firwin(n,f,fs=fs, pass_zero=type)
    sigfilter = filtfilt(b,1,sig)
    return sigfilter



def filter_2sIIR(sig,f,fs,n,type):

    """
    A two-stage IIR filter processing using Butterworth filter design

    The  input arguments are identical to those used in BUTTER
    sig: is the signal to be filtered arranged
    f: a vector of cutoff frequencies in Hz. f is a number for lowpass and
        highpass filters, and is a two-element vector for bandpass or bandstop
        filter.
    fs: the sampling frequency.
    n: the order of IIR filter.
    type: 'low' for lowpass filter 'high' for highpass filter 
        'bandpass' for bandpass filter 'stop' for bandstop filter.
    """

    b, a = butter(n, f, btype=type,fs=fs)

    sigfilter = filtfilt(b,a,sig)
    
    return sigfilter


