function event = voting_multivar(sc, event_size)
% VOTING_MULTIVAR  The function simply uses the voting algorithm to get the
% value of the events.
%
% The input of the function is:
%    sc: the source claim matrix with multiple valued claims.
%    event_size: the number of possible values for each event.
[~, nume] = size(sc);
event = zeros(nume,1);

for j = 1:1:nume
    claimvec = sc(:,j);
    vote_cnt = 0;
    vote_val = 0;
    for v = 1:1:event_size(j)
        temp = sum(claimvec == v);
        if temp > vote_cnt
            vote_val = v;
            vote_cnt = temp;
        end
    end
    event(j) = vote_val;
end
end
