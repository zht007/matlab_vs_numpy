function Y=filter_proc(td,sr,fn,val)
%%% filtering design: butterworth IIR filters %%%
% td  input data (if is matrix, input in row vectors for measurements)
% sr  sampling rate
% fn  cutoff frequency
% val filter type: 1 for lowpass, 2 for highpass, 3 for bandpass
%
% Author: Lu, Chia-Feng 2013.10.23
if nargin~=4
   disp('Error use in inputs, please check.') 
   return
end

if isempty(fn)   
    disp('Please input the cuttof frequency')
    return
else
    if max(fn)/2>=sr
        disp('The sampling rate is not sufficient for the cuttof frequency.')
        return
    end
    
    Y=[];
    [meas,timept]=size(td); %%% epo_tem = signal --> 21*15000
    if val == 1  % lowpass filter
        [a,b]=butter(6,fn/(sr/2),'low');  % create parameters of butterworth filter
        for i=1:meas
            Y(i,:)=filtfilt(a,b,td(i,:));  % zero-phase shift filtering
        end
    elseif val == 2   % highpass filter
        [a,b]=butter(6,fn/(sr/2),'high');  % create parameters of butterworth filter
        for i=1:meas
            Y(i,:)=filtfilt(a,b,td(i,:));  % zero-phase shift filtering
        end
    elseif val == 3    % bandpass filter
        [a,b]=butter(6,fn(1)/(sr/2),'high');  % create parameters of butterworth filter
        for i=1:meas
            Y(i,:)=filtfilt(a,b,td(i,:));  % zero-phase shift filtering
        end
        [a,b]=butter(6,fn(end)/(sr/2),'low');  % create parameters of butterworth filter
        for i=1:meas
            Y(i,:)=filtfilt(a,b,Y(i,:));  % zero-phase shift filtering
        end
    end
end