function [reliabilityvec, eventvalvec] = emc(sc)
% EMC  The basic EM fact-finder algorithm with conflict claims
%   [reliabilityvec, eventvalvec] = EMC(sc)
%   sc: The observations from the sources about the events
%   reliabilityvec: The estimated source reliability
%   eventvalvec: The estimated event value
%
% By default, FALSE - 0, TRUE - 1, UNKNOWN - 2

format long
FALSE = 0;
TRUE = 1;
UNKNOWN = 2;  % define some constants

% % best possible parameters so far
% init_tt = 0.9;
% init_ft = 0.9;
% init_tf = 0.5;
% init_ff = 0.4;

% We use voting to select the parameters
[init_tt, init_ft, init_tf, init_ff] = initparam(sc);

[nums, nume] = size(sc);  % get the number of sources and number of events

% initialize the parameters
tt = init_tt;  % T_i^T = pr(SC_ij = T | C_j = T)
ft = init_ft;  % F_i^T = pr(SC_ij = F | C_j = T)
tf = init_tf;  % T_i^F = pr(SC_ij = F | C_j = F)
ff = init_ff;  % F_i^F = pr(SC_ij = T | C_j = F)
dv = ones(nume, 1)*0.5;  % d_j = pr(C_j = T)

threshold = 0.0001;  % the threshold for judging convergence
isconverged = false;  

debug_niteration = 0;

while ~isconverged
    % Compute the Z(j, n) = pr(Z_j = T | X_j, theta^(n))
    % By definition, we have Z(j,n) = A(j, n) / (A(j,n) + B(j,n)).
    % Here A(j,n) = pr(X_j | Z_j = T, theta^(n)) * pr(Z_j = T | theta^(n))
    % and B(j,n) = pr(X_j | Z_j = F, theta^(n)) * pr(Z_j = F | theta^(n))
    % The results are in zvec.
    amask = zeros(nums, nume);
    amask = amask + (tt*ones(1, nume)).*(sc == TRUE);
    amask = amask + (ft*ones(1, nume)).*(sc == FALSE);
    amask = amask + ((1 - tt - ff) * ones(1,nume)) .* (sc == UNKNOWN);
    avec = prod(amask,1)' .* dv;
    
    bmask = zeros(nums, nume);
    bmask = bmask + (tf*ones(1,nume)) .* (sc == FALSE);
    bmask = bmask + (ff*ones(1,nume)) .* (sc == TRUE);
    bmask = bmask + ((1 - tf - ff) * ones(1,nume)) .* (sc == UNKNOWN);
    bvec = prod(bmask,1)' .* (1 - dv);
    
    zvec = avec ./ (avec + bvec);
    
    % Update the parameters.
    % T_i^T = sum_{j in sc == T} Z(j,n) / sum_{j} Z(j,n)
    % F_i^T = sum_{j in sc == F} Z(j,n) / sum_{j} Z(j,n)
    % T_i^F = sum_{j in sc == F} (1 - Z(j,n)) / sum_{j} (1 - Z(j,n))
    % F_i^F = sum_{j in sc == T} (1 - Z(j,n)) / sum_{j} (1 - Z(j,n))
    % d_j = Z(j,n)
    zmat = (zvec * ones(1,nums))';  % now each row of zmat is a zvec
    
    ttzmask = zmat .* (sc == TRUE);
    ttnow = sum(ttzmask,2) / sum(zvec);
    
    ftzmask = zmat .* (sc == FALSE);
    ftnow = sum(ftzmask,2) / sum(zvec);
    
    tfzmask = (1 - zmat) .* (sc ==FALSE);
    tfnow = sum(tfzmask,2) / sum((1 - zvec));
    
    ffzmask = (1 - zmat) .* (sc == TRUE);
    ffnow = sum(ffzmask,2) / sum((1 - zvec));
    
    dvnow = zvec;
    
    newparam = [ttnow;ftnow;tfnow;ffnow;dvnow];
    oldparam = [tt;ft;tf;ff;dv];
    difference = abs(newparam - oldparam);
    if max(difference) < threshold
        isconverged = true;
    end
    
    % debug info
    disp(debug_niteration)
    disp(max(difference))
    debug_niteration = debug_niteration + 1;
    
    if debug_niteration > 1000
        isconverged = true;
    end
    
    tt = ttnow;
    ft = ftnow;
    tf = tfnow;
    ff = ffnow;
    dv = dvnow;
end

%  Estimate the event value
event = dv >= 0.5;
eventvalvec = zeros(nume,1);
eventvalvec(event == true) = TRUE;
eventvalvec(event == false) = FALSE;

%  Estimate the source reliability
%  By definition t_i = pr(C_j^v | SC_{ij}^v)
%                    = 1/2 * (pr(C_j^T | SC_ij^T) + pr(C_j^F | SC_ij^F)).
%
%  pr(C_j^T | SC_ij^T) = pr(SC_ij^T | C_j^T) * pr(C_j^T) / pr(SC_ij^T)
%                      = tt(i) * dv(j) / (tt(i)*dv(j) + ff(i)*(1-dv(j)))
%
%  pr(C_j^F | SC_ij^F) = pr(SC_ij^F | C_j^F) * pr(C_j^F) / pr(SC_ij^F)
%                      = tf(i)*(1-dv(j)) / (tf(i)*(1-dv(j)) + ft(i)*dv(j))
ttmask = tt * dv';
ffmask = ff * (1-dv)';
tfmask = tf * (1-dv)';
ftmask = ft * dv';

reliabilitymask = ttmask ./ (ttmask+ffmask) + tfmask ./ (tfmask + ftmask);
reliabilitymask = reliabilitymask / 2;
reliabilityvec = sum(reliabilitymask,2) / nume;
end
