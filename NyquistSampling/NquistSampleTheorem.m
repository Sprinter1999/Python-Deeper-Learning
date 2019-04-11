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
title('���Ҳ�2KHz')
ylabel('���')
xlabel('Tempo (s)')

fs = 10000;%������Ƶ�ʿ����Լ�����
ts = 1/fs;
t1 = tmin:ts:tmax;
N= length(t1);

xn = sin(2*pi*f*t1);

subplot(312)
stem(t1,xn);
title('���Ҳ� 2KHz ����Ƶ�� 10KHz')
ylabel('���')
xlabel('Tempo (s)')

%����Ƶ��
freq = (0:N-1)*fs/N;
freq = freq(1:floor(length(freq)/2));

%�ź�Ƶ��
SINAL = fft(xn);
SINAL = SINAL(1:floor(length(xn)/2));

subplot(313);
plot(freq,abs(SINAL));
title('Ƶ��Ϊ2Khz�����Ҳ���')
ylabel('���')
xlabel('Ƶ�� Hz')