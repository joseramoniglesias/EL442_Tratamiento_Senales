% José Ramón Iglesias Gamarra, 2020-2
close all
I = imread('cameraman.tif');
imshow(I)
title('imagen original')

[N,M] = size(I);

filtro = input('Filtro 1: Ideal, 2: Gaussiano 3: Butterworth ?');
Do     = input('Frecuencia de Corte (Do) ?');
S = ['Ideal      '
    'Gaussiano  '
    'Butterworth'];

switch filtro % Ideal
    case 1
        H = TRAT04_IdealMask(N,M,Do);
    case 2 % Gaussian
        H = TRAT04_GaussianMask(N,M,Do);
    case 3 % Butterworth
        n = input('Orden de Butterworth? ');
        H = TRAT04_ButterworthMask(N,M,Do,n);
end

J = TRAT05_FiltroFrecuencia(I,H,1);


