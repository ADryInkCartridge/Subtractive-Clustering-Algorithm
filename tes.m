M = readmatrix('testdata177n2.csv')
[centers,U] = fcm(M,2);

maxU = max(U);
index1 = find(U(1,:) == maxU);
index2 = find(U(2,:) == maxU);

plot(M(index1,1),M(index1,2),'ob')
hold on
plot(M(index2,1),M(index2,2),'or')
plot(centers(1,1),centers(1,2),'xb','MarkerSize',15,'LineWidth',3)
plot(centers(2,1),centers(2,2),'xr','MarkerSize',15,'LineWidth',3)
hold off