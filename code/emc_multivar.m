function eventvalvec = emc_multivar(sc, event_size, event_category, category_num)
% EMC  The basic multivar EM fact-finder algorithm with conflict claims
%   eventvalvec = EMC(sc, event_size, event_category)
%
%   sc: The observations from the sources about the events
%   event_size: The number of possible values of each event
%   event_category: the event category
%   category_num: the number of event categories
%   eventvalvec: The estimated event value
%
% By default, UNKNOWN - 0, event values start from 1 to n_j

format long
UNKNOWN = 0;

[nums, nume] = size(sc);  % get the number of sources and number of events

% initialize the parameters
[ttinit, ffinit] = initparam_multivar(sc, event_size, event_category, category_num);
tt = ttinit;  % ell T_i = pr(SC_ij = v | ell C_j = v)
ff = ffinit;  % ell F_i = pr(SC_ij = ~v | ell C_j = v)
dv = cell(nume,1);
for j = 1:1:nume
    dv{j} = ones(event_size(j),1) * 0.5;
end

threshold = 0.0005;  % the threshold for judging convergence
isconverged = false;  

debug_niteration = 0;

while ~isconverged
    % Compute the Z(j, n) = pr(Z_j = v | X_j, theta^(n))
    % Results are contained in a cell array zcell
    zcell = cell(nume,1);
    for j = 1:1:nume
        zcell{j} = zeros(event_size(j), 1);
        for v = 1:1:event_size(j)
            zcell{j}(v) = dv{j}(v);
            ecat = event_category(j);
            for i = 1:1:nums
                if sc(i,j) == v
                    zcell{j}(v) = zcell{j}(v) * tt(i, ecat);
                else if sc(i,j) == UNKNOWN
                        scal = 1 - tt(i,ecat) - ff(i,ecat);
                        zcell{j}(v) = zcell{j}(v) * scal;
                    else  % sc(i,j) = ~v
                        zcell{j}(v) = zcell{j}(v) * ff(i,ecat);
                    end
                end
            end
        end
        zsum = sum(zcell{j});
        zcell{j} = zcell{j} / zsum;
    end
    
    % Update the parameters.
    ttnow = zeros(nums, category_num);
    ffnow = zeros(nums, category_num);
    for ecat = 1:1:category_num
        numeventsincat = sum(event_category == ecat);
        for i = 1:1:nums
            for j = 1:1:nume
                for v = 1:1:event_size(j)
                    if sc(i,j) == v && event_category(j) == ecat
                        ttnow(i,ecat) = ttnow(i,ecat) + zcell{j}(v);
                    else if sc(i,j) > UNKNOWN && event_category(j) == ecat
                            ffnow(i,ecat) = ffnow(i,ecat) + zcell{j}(v);
                        end
                    end
                end
            end
        end
        ttnow(:,ecat) = ttnow(:,ecat) / numeventsincat;
        ffnow(:,ecat) = ffnow(:,ecat) / numeventsincat;
    end
    dvnow = zcell;
    
    newparam = [ttnow;ffnow];
    for j = 1:1:nume
        newparam = [newparam;dvnow{j}];
    end
    oldparam = [tt;ff];
    for j = 1:1:nume
        oldparam = [oldparam;dv{j}];
    end
    difference = abs(newparam - oldparam);
    if max(difference) < threshold
        isconverged = true;
    end
    
    % debug info
    disp(debug_niteration)
    disp(max(difference))
    debug_niteration = debug_niteration + 1;
    
    if debug_niteration > 500
        isconverged = true;
    end
    
    tt = ttnow;
    ff = ffnow;
    dv = dvnow;
end

%  Estimate the event value
eventvalvec = zeros(nume,1);
for j = 1:1:nume
    bestval = -1;
    bestidx = 0;
    for v = 1:1:event_size(j)
        if dv{j}(v) > bestval
            bestval = dv{j}(v);
            bestidx = v;
        end
    end
    eventvalvec(j) = bestidx;
end
end
