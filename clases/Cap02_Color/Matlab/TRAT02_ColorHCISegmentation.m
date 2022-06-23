% Color Segmentation using
% (c) José ramón Iglesias(2020)


close all
k = 3;

I = imread('flor.png');
I = imresize(I,1);
[R,E,J] = Bim_segbalu(I,0);
figure(1);imshow(I);figure(2);imshow(J,[]);figure(3);imshow(R);figure(4);
Bio_edgeview(I,E,[0 1 0],k)
enterpause



I = imread('testimg1.jpg');
I = imresize(I,k);
[R,E,J] = Bim_segbalu(I,0);
figure(1);imshow(I);figure(2);imshow(J,[]);figure(3);imshow(R);figure(4);
Bio_edgeview(I,E,[0 1 0],k)
enterpause

I = imread('flamingo.jpg');
I = imresize(I,k);
[R,E,J] = Bim_segbalu(I,0);
figure(1);imshow(I);figure(2);imshow(J,[]);figure(3);imshow(R);figure(4);
Bio_edgeview(I,E,[0 1 0],k)
enterpause

I = imread('butterfly.jpg');
I = imresize(I,k);
[R,E,J] = Bim_segbalu(I);
figure(1);imshow(I);figure(2);imshow(J,[]);figure(3);imshow(R);figure(4);
Bio_edgeview(I,E,[1 0 0],k)
enterpause

I = imread('airplane.jpg');
I = imresize(I,k);
[R,E,J] = Bim_segbalu(I,-0.1);
figure(1);imshow(I);figure(2);imshow(J,[]);figure(3);imshow(R);figure(4);
Bio_edgeview(I,E,[0 1 0],k)
