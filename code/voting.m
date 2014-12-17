function event = voting(sc)
% VOTING  The function to get the value of event solely based on SC
%

TRUE = 1;
FALSE = 0;

[~, nume] = size(sc);

truemask = sc==TRUE;
falsemask = sc==FALSE;

truevote = sum(truemask,1);
falsevote = sum(falsemask, 1);

temp = (truevote>falsevote)';
event = zeros(nume,1);
event(temp==true) = TRUE;
event(temp==false) = FALSE;
