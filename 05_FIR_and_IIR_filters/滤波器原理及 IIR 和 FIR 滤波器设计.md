### 1. 滤波器原理

#### 1.1 Z 变换

我们知道傅里叶变换可以写成如下形式，来表示信号在频域上的信息。
$$
\begin{aligned}
S(f) &=\sum_{n=0}^{N-1} s(n) \cos (2 \pi f n / N)-j \sum_{n=0}^{N-1} s(n) \sin (2 \pi f n / N) \\
&=\sum_{n=0}^{N-1} s(n) e^{-j 2 \pi f n / N}
\end{aligned}
                                 
$$
更一般地，我们可以将 e^j2πfn/N 替换成任意复数 Z，此时就完成了信号在时域向 Z 域的转换，我们叫 Z 变换
$$
X(z) \equiv Z\{x(n)\}=\sum_{n=0}^{N-1} x(n) z^{-n}
$$

#### 1.2 转换函数

如下图所示，滤波实际上就是在 Z 频率中，设计一个**转换函数 H(z)** 与原信号 X(z) 相乘，将想要滤掉的频域清零。在频域上的乘积操作相当于在时域上的卷积操作。

![image-20220706162942123](https://s2.loli.net/2022/07/06/qYDXj8ocImCGF7H.png)

类似于**多项式展开**，转换函数即为，分子分母的多项式展开之和。
$$
Y(z)=X(z) \cdot H(z)=X(z) \frac{\sum_{k=0}^{K} b_{k} z^{-k}}{\sum_{l=0}^{L} a_{l} z^{-1}}.......................(1)
$$
在时域中的计算公式如下
$$
y(n) = \sum_{k = 0}^{K} b_{k} x(n-k)-\sum_{l 1}^{L} a_{l} y(n-l)
$$

> 设计滤波器实际上就是设计 bk 和 al 这两组数据，K 和 L 对应着滤波器的阶数。

### 2. FIR 和 IIR 区别

FIR 为有限脉冲滤波器，IIR为无线脉冲滤波器。当转换函数 H(z) 中只考虑 的时候即为FIR，同时考虑  b<sub>k</sub> 和 a<sub>l</sub>的时候为即为 IIR。

> FIR 的输出仅与之前的输入 x(n-k) 有关，而IIR 不仅与之前的输入有关而且还与之前的输出 y(n-l) 有关， 
>
>  FIR和 IIR 的特点如下 
>
> * FIR 相对稳定
>
> * FIR 的相位变化式线性的
>
> * FIR 需要较高的阶数来满足滤波条件
>
> * FIR计算效率相对较低
>
>   
>
> * IIR 仅需要较低的阶数满足滤波条件
>
> * IIR 计算效率较高，但是计算需要用到整段信号
>
> * IIR 可能不太稳定，因为 a<sub>l</sub> 可能为0
>
> * IIR 的相位是非线性变化的

### 3. FIR 滤波器设计

在 Matlab 和 Python中分别使用 `fir()`和 `scipy.signal.firwin()`函数设计滤波器，需要注意的是函数输入参数的条件。fir() 的 wn 被 fs/2 归一化了在0到1之间，所以wn=f/(fs/2)。firwin() 在没有输入 fs 的情况下跟 fir() 的条件是一样的，在给了 fs 的输入之后可以直接用f，而不需要归一化。

```python
# Matlab

function sigfilter = filter_2sFIR(sig,f,fs,n,type,win)
% A two-stage FIR filter processing using the window method
%
% The  input arguments are identical to those used in FIRPM
%  sig: is the signal to be filtered arranged, each row is a measurement
%    f: a vector of cutoff frequencies in Hz. f is a number for lowpass and
%       highpass filters, and is a two-element vector for bandpass or bandstop
%       filter.
%   fs: the sampling frequency.
%    n: the order of FIR filter.
% type: 'low' for lowpass filter; 'high' for highpass filter; 
%       'bandpass' for bandpass filter; 'stop' for bandstop filter.
%  win: assign the N+1 length window vector to window the impulse response. 
%       (same way as in PWELCH). Default is hamming window.
%
%  Details of input arguments and examples, please help FIR1.
%
%  [Author]: Lu, Chia-Feng 2013.11.08

if nargin<5
    type='low';
    win=[];
elseif nargin<6
    win=[];
end

if f>=fs/2
   error('The sampling frequency is not adequent for the given cutoff frequency, please input a lower f.') 
end

if isempty(win)
    b = fir1(n,f/(fs/2),type);
else
    b = fir1(n,f/(fs/2),type,win);
end

if size(sig,2)<=3*n
    error('Signal must have length more than 3 times filter order for FILTFILT process')
end

sigfilter=[];
for i=1:size(sig,1)
    sigfilter(i,:) = filtfilt(b,1,sig(i,:));
end

# Python

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

```



### 4. IIR 滤波器设计

IIR 滤波器可以选择 巴特沃斯（butter），切比雪夫（cheb1ord）或者椭圆（ ellipord）滤波器，这里以 butter 滤波器为例

```python
# Matlab

function sigfilter=filter_2sIIR(sig,f,fs,n,type)
% A two-stage IIR filter processing using Butterworth filter design
%
% The  input arguments are identical to those used in BUTTER
%  sig: is the signal to be filtered arranged, each row is a measurement
%    f: a vector of cutoff frequencies in Hz. f is a number for lowpass and
%       highpass filters, and is a two-element vector for bandpass or bandstop
%       filter.
%   fs: the sampling frequency.
%    n: the order of IIR filter.
% type: 'low' for lowpass filter; 'high' for highpass filter; 
%       'bandpass' for bandpass filter; 'stop' for bandstop filter.
%
%  Details of input arguments and examples, please help BUTTER.
%
%  [Author]: Lu, Chia-Feng 2013.11.08

if nargin<4
    error('Not enough input arguments! pleas check') 
elseif nargin<5
    type='low';
end

if f>=fs/2
   error('The sampling frequency is not adequent for the given cutoff frequency, please input a lower f.') 
end

if strcmpi(type,'bandpass')
    %%% highpass
    [b,a]=butter(n,f(1)/(fs/2),'high');
    sigfilter=[];
    for i=1:size(sig,1)
        sigfilter(i,:) = filtfilt(b,a,sig(i,:));
    end
    
    %%% lowpass
    [b,a]=butter(n,f(end)/(fs/2),'low');
    for i=1:size(sigfilter,1)
        sigfilter(i,:) = filtfilt(b,a,sigfilter(i,:));
    end
else
    [b,a]=butter(n,f/(fs/2),type);

    sigfilter=[];
    for i=1:size(sig,1)
        sigfilter(i,:) = filtfilt(b,a,sig(i,:));
    end
end

### Python

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
```

