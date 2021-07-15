M = readmatrix('buku.csv')
options = [1.25 0.5 0.15 0];
[C,S] = subclust(M,0.5,'Options',options);
writematrix(C,'C.csv') 
writematrix(S,'S.csv') 