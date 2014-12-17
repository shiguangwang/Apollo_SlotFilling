function [tt, ff] = initparam_multivar(sc, event_size, event_category, category_num)
event = voting_multivar(sc, event_size);
[nums,~] = size(sc);
tt = zeros(nums, category_num);
ff = zeros(nums, category_num);

for i = 1:1:nums
    claims = sc(i,:)';
    true_claims = claims == event;
    false_claims = claims ~= event & claims ~= 0;
    for ecat = 1:1:category_num
        ecatmask = event_category == ecat;
        tt(i,ecat) = sum(true_claims .* ecatmask) / sum(ecatmask);
        ff(i,ecat) = sum(false_claims .* ecatmask) / sum(ecatmask);
    end
end
end
