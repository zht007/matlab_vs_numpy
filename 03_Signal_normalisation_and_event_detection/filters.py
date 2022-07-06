
import numpy as np
from scipy.signal import firwin, butter, lfilter,filtfilt,buttord,cheb1ord,ellipord

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
    type: 'lowpass' for lowpass filter 'highpass' for highpass filter 
        'bandpass' for bandpass filter 'bandstop' for bandstop filter.
    win: assign the N+1 length window vector to window the impulse response. 
        (same way as in PWELCH). Default is hamming window.

    Details of input arguments and examples, please help FIR1.

    """
    if type == 'highpass' or type == 'bandstop':
        n |=1   # Ensure that n is odd. The statement sets the lowest bit of n to 1
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
    # b, a = cheb1ord(n, f, btype=type,fs=fs)
    # b, a = ellipord(n, f, btype=type,fs=fs)
    
    sigfilter = filtfilt(b,a,sig)
    
    return sigfilter

def filter_3sIIR(sig,wp,ws,rp,rs,fs,type):

    """
    A three-stage IIR filter processing using Butterworth filter design

    The  input arguments are identical to those used in BUTTORD
    sig: is the signal to be filtered arranged, each row is a measurement
    f: a vector of cutoff frequencies in Hz. f is a number for lowpass and
        highpass filters, and is a two-element vector for bandpass or bandstop
        filter.
    wp and ws are the passband and stopband edge frequencies, in Hz. For example,
        Lowpass:    Wp = 60,      Ws = 65,
        Highpass:   Wp = 125,     Ws = 120,
        Bandpass:   Wp = [65, 120], Ws = [60, 125]
        Bandstop:   Wp = [60, 125], Ws = [65, 120]
    rp: loses no more than rp dB in the passband (3dB) and;
    rs: has at least rs dB of attenuation in the stopband.
    fs: the sampling frequency.
    type: 'low' for lowpass filter; 'high' for highpass filter; 
        'bandpass' for bandpass filter; 'stop' for bandsto filter.

    Details of input arguments and examples, please help BUTTORD.

    """

    # if max(np.array([wp, ws])/(fs/2))>=1:
        # print('The sampling frequency is not adequent for the given cutoff frequency, please input a lower f.') 

    if type =='low' or type=='high':
        [n,wn]=buttord(wp/(fs/2),ws/(fs/2),rp,rs)
    else:
        [n,wn]=buttord([wp[0]/(fs/2), wp[1]/(fs/2)],[ws[0]/(fs/2), ws[1]/(fs/2)],rp,rs)


    b, a = butter(n,wn,type)

    sigfilter = filtfilt(b,a,sig)
    # for i in range(len(sig)):
    #     sigfilter(i,:) = filtfilt(b,a,sig[i,:])

    return sigfilter,n
