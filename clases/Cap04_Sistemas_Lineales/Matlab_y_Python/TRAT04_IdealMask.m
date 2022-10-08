% function H = TRAT05_IdealMask(N,M,Do)
%
% Construccion de mascara H en el dominio de la frecuencia para un filtro
% pasa bajos ideal.
% 
% El tamano de la matriz H es NxM
% NxM debe ser del tamano de la imagen.
% La frecuencia de corte es Do.
%
% Jos� Ram�n Iglesias, Agosto 2020
%

function H = TRAT05_IdealMask(N,M,Do)

D = zeros(N,M);
H = D;

for u=1:N
    for v=1:M
        D(u,v) = sqrt((u-N/2)^2+(v-M/2)^2);
    end
end

H(D<Do) = 1;




