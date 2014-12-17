function [tt, ft, tf, ff] = initparam(sc)
% INITPARAM  Using voting to select the init value of param of the EM algo.
%
%    Input: 
%        sc: The source-claim matrix
%    Output:
%        tt: param T_i^T = pr(SC_ij^T | C_j^T)
%        ft: param F_i^T = pr(SC_ij^F | C_j^T)
%        tf: param T_i^F = pr(SC_ij^F | C_j^F)
%        ff: param F_i^F = pr(SC_ij^T | C_j^F)
% 
% By default: 
%    TRUE = 1, FALSE = 0, UNKNOWN = 2

TRUE = 1;
FALSE = 0;

event = voting(sc);  % using voting to get the ground truth.

[nums, ~] = size(sc);
emat = (event*ones(1,nums))';

ttmask = (sc==TRUE).*emat;
tt = sum(ttmask,2)/sum(event);

ftmask = (sc==FALSE).*emat;
ft = sum(ftmask,2)/sum(event);

tfmask = (sc==FALSE).*(1-emat);
tf = sum(tfmask,2)/sum(1-event);

ffmask = (sc==TRUE).*(1-emat);
ff = sum(ffmask,2)/sum(1-event);
