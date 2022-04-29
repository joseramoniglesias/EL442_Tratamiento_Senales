% Example:
%
% Display of a horse using Computer Graphics
%
% Computer Vision Course
% (c) José Ramón Iglesias(2021) - https://sites.google.com/a/unicesar.edu.co/jose-r-iglesias/


load horse % 3D data: Courtesy of Ivan Sipiran
                   % horse.data is matlab/data directory
close all
%Parcela de superficie triangular
trisurf(T',M(1,:),M(2,:),M(3,:));
axis equal;
enterpause
trisurf(T',M(1,:),M(2,:),M(3,:),'FaceColor','b','EdgeColor','none');
axis equal;
enterpause
alpha 0.8;
%Crear o mover objetos ligeros en coordenadas de cámara
camlight;
enterpause
camlight(-80,-10);
enterpause
%Especificar algoritmo de iluminación
lighting p;
enterpause
view(3);
enterpause
axis off
grid off