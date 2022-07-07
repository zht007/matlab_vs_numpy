## Overview

This repo is  tutorial comparing Matlab and [numpy](https://numpy.org/) (a python library)  in signal analysis.  Data and Matlab code obtained from [the lecture](http://cflu.lab.nycu.edu.tw/) of Dr Chia-Feng Lu. The corresponding python code is provided to help readers to learn how to use free  [numpy](https://numpy.org/), [scipy](https://docs.scipy.org/doc/scipy/index.html) and [scikit-learn](https://scikit-learn.org/) library in python to conduct signal analysis tasks. 

## Table of Contents

[01_Basic_operations](https://github.com/zht007/matlab_vs_numpy/tree/main/01_Basic_operations)

[02_Signal_preprocessing_resample_and_segment](https://github.com/zht007/matlab_vs_numpy/tree/main/02_Signal_preprocessing_resample_and_segment)

[03_Signal_normalisation_and_event_detection](https://github.com/zht007/matlab_vs_numpy/tree/main/03_Signal_normalisation_and_event_detection)

[04_Fourier_transform](https://github.com/zht007/matlab_vs_numpy/tree/main/04_Fourier_transform)

[05_FIR_and_IIR_filters](https://github.com/zht007/matlab_vs_numpy/tree/main/05_FIR_and_IIR_filters)

[06_Time_frequency_analysis](https://github.com/zht007/matlab_vs_numpy/tree/main/06_Time_frequency_analysis)

##  How to Use Jupyter nootbook with matlab 

#### 1. install python, matlab

The matlab software and Python need to be installed.

> matlab currently only supports python 3.8 and below

#### 2. install matlab_kernel

```
pip install matlab kernal
```

#### 3. Configure matlab_kernal

1. cd to the Matlab installation directory (C:\Program Files\MATLAB for Windows)
2. cd to MATLAB\\(current version directory)\extern\engines\python
3. execute the `python setup.py install` command

#### 4. install jupyter notebook or jupyter lab

```
pip install notebook
```

#### 5. Start jupyter notebook

```
jupyter notebook
```

If you open jupyter notebook in your browser and select malab in the kernel, you can use matlab in jupyter notebook just like python.

----

Reference：

[begin_matlab/00. Introduction.ipynb at master · APMonitor/begin_matlab · GitHub](https://github.com/APMonitor/begin_matlab/blob/master/matlab/00.%20Introduction.ipynb)
