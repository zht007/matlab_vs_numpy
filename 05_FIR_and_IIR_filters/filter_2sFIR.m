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
