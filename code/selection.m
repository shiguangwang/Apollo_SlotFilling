function [best_ft, best_ff, results] = selection(sc)
init_tt = 0.1:0.1:0.9;
init_tf = 0.1:0.1:0.9;

[~, nume] = size(sc);

results = zeros(10,10);
best_ft = zeros(10,10);
best_ff = zeros(10,10);

for i = 1:1:9
    for j = 1:1:9
        itt = init_tt(i);
        itf = init_tf(j);
        accuracy = -1;
        bft = -1;
        bff = -1;
        for ift = 0.1:0.1:itt
            for iff = 0.1:0.1:itf
                [~, event] = emc(sc, itt, ift, itf, iff);
                temp = sum(event) / nume;
                if temp > accuracy
                    accuracy = temp;
                    bft = ift;
                    bff = iff;
                end
            end
        end
        results(i,j) = accuracy;
        best_ft(i,j) = bft;
        best_ff(i,j) = bff;
    end
end
end
