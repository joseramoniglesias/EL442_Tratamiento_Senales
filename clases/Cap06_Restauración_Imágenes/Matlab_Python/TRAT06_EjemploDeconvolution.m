%Jos� Ram�n Iglesias Gamarra - 2020-2
close all
clear all
warning off
disp('                                 H*(u,v)');
disp(' Filro Inverso = W(u,v) = ---------------------');
disp('                          |H(u,v)|^2 + C/SNR^2');
disp(' ');
disp('SNR^2 = 1/(r^rho)                  r = sqrt(u^2+v^2)');

I = imread('saturn.png');
I = imresize(I,0.25);
F = rgb2gray(I);
figure(1)
imshow(F,[])
title('imagen original F')
F = double(F);
n = 11;
h = ones(n,n)/n/n;
G = conv2(F,h,'valid');
%Jos� Ram�n Iglesias Gamarra - 2020-2
figure(2)
imshow(G,[])
title('imagen degradada sin ruido G')


Fs = Bim_deconvolution(G,h);
figure(3)
imshow(Fs,[])
title('imagen restaurada Fs = G/H')

disp('presione enter...')
pause
Gr = G+2*randn(size(G));

figure(4)
imshow(Gr,[])
title('imagen degradada con ruido G+N')


Fs = Bim_deconvolution(Gr,h);
figure(5)
imshow(Fs,[])
title('imagen restaurada Fs = (G+N)/H')

C = 1;
while C>0
    C = input('C? (0 para finalizar)');
    if C>0
        Fs = Bim_deconvolution(Gr,h,C);
        figure(5)
        imshow(Fs,[])
        title('imagen restaurada')
    end
end

disp('buscando mejor C....')
d = -5:0.1:1;
e = zeros(size(d));
nd = length(d);
for i = 1:nd
    C = 10^d(i);
    Fs = Bim_deconvolution(Gr,h,C);
    D = abs(F-Fs);
    e(i) = mean(D(:));
    fprintf('prueba %d/%d) C=%f, err=%f\n',i,nd,C,e(i))
end
[i,j] = min(e);
C = 10^(d(j));
Fs = Bim_deconvolution(Gr,h,C);
figure(5)
imshow(Fs,[])
title('mejor imagen restaurada')
figure(6)
plot(d,e)
title(sprintf('mejor C = 10^d = %f, d=%f',C,d(j)))
xlabel('d')
ylabel('error')
disp('presione enter...')
pause




rho = 1;
while rho>0
    rho = input('rho (ej: 0.05)? ');
    if rho>0
        Fs = Bim_deconvolution(Gr,h,C,rho);
        figure(5)
        imshow(Fs,[])
        title('imagen restaurada')
    end
end
