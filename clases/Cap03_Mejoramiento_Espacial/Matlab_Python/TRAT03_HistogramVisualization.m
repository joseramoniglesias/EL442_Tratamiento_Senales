% Example:
%
% Histogram visualization 
%
% Computer Vision Course
% (JOs� Ram�n Iglesias(2021)

% close all
% X  = imread('X1.png');
X  = imread('rice.png');
% X  = imread('coins.png'); 

figure(1);clf
imshow(X,[])

n = size(X,2);
T = round(255.0*(ones(20,1)*(1:n))/n);

I = [X;T];

h = zeros(256,1);
k = 1;
figure(2);clf
figure(3);clf
for t=0:255
    J = imdilate(I==t,ones(3,3));
    h(t+1) = sum2(X==t);
    figure(2)
    Bio_edgeview(I(1:k:end,1:k:end),J(1:k:end,1:k:end))
    figure(3)
    imhist(X(X<=t));
    axis([1 255 0 2000])
    drawnow
    if t==0
        pause
    end
end
