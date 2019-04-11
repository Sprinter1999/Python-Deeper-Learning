clc;
clear all;
close all;

f = 2000;
t = 1/f;
tmin = 0;
tmax = 10*t;
t0 = tmin:1/100000:tmax;
xt = sin(2*pi*f*t0);

subplot(311)
plot(t0,xt);
title('正弦波2KHz')
ylabel('振幅')
xlabel('Tempo (s)')

fs = 10000;%采样的频率可以自己设置
ts = 1/fs;
t1 = tmin:ts:tmax;
N= length(t1);

xn = sin(2*pi*f*t1);

subplot(312)
stem(t1,xn);
title('正弦波 2KHz 采样频率 10KHz')
ylabel('振幅')
xlabel('Tempo (s)')

%调整频率
freq = (0:N-1)*fs/N;
freq = freq(1:floor(length(freq)/2));

%信号频谱
SINAL = fft(xn);
SINAL = SINAL(1:floor(length(xn)/2));

subplot(313);
plot(freq,abs(SINAL));
title('频率为2Khz的正弦波谱')
ylabel('振幅')
xlabel('频率 Hz')