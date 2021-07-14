M = readmatrix('noPCA.csv')
[C,S] = subclust(M,1);
writematrix(C,'C.csv') 
writematrix(S,'S.csv') 