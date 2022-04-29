% (c) José Ramón Iglesias(2018) - 
%https://sites.google.com/a/unicesar.edu.co/jose-r-iglesias/
%    enterpause display "press <Enter> to continue..." and wait for <Enter>
%    enterpause(t) means pause(t)
%
function enterpause(t)
if ~exist('t','var')
    disp('press <Enter> to continue...')
    pause
else
    pause(t)
end