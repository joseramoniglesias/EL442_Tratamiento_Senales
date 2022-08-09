% function H = TRAT05_ButterworthMask(N,M,Do,n)
%
% Construccion de mascara H en el dominio de la frecuencia para un filtro
% Butterworth.
% 
% El tamano de la matriz H es NxM
% NxM debe ser del tamano de la imagen.
% La frecuencia de corte es Do.
% El ordel del filtro Butterworh es n.
%
% Jos� Ram�n Iglesias, Agosto 2020
%
function H = TRAT05_ButterworthMask(N,M,Do,n)

H = zeros(N,M);
m = 2*n;

for u=1:N
    for v=1:M
        H(u,v) = 1/(1+((sqrt((u-N/2)^2+(v-M/2)^2))/Do)^m);
    end
end

