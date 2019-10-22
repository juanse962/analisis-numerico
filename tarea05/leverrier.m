A=[7,0,1,3,2; 0,8,0,4,2; 1,0,10,1,-1; 3,4,1,7,-2; 2,2,-1,-2,12];
fprintf("Matriz A:\n");
disp(A);
n=length(A); 
p=zeros(1,n);
s=zeros(n,1);
B=zeros(n); 
for i=1:n
    B=A^i;
    %calcula la traza de las sucesivas 
    s(i)=trace(B);
end
p(1)=-s(1);
for i=2:n
    p(i)=-s(i)/i;
    for j=1:i-1
        p(i)=p(i)-p(j)*s(i-j)/i;
    end
end
raiz=roots([1 p]);
%Los valores propios aparecen en la diagonal de la matriz D
D=diag(raiz);
fprintf("Valores propios:\n");
disp(D);
%Vectores propios para cada valor propio
C=-1.*A(2:n,1);
V=zeros(n);
S=zeros(n,1); %vector propio
for i=1:length(D)
    B=A(2:n,2:n)-D(i,i)*eye(n-1);
    S=[1 (B\C)'];
    % vectores propios normalizados
    V(1:n,i)=S/norm(S);
end
fprintf("Vectores propios:\n");
disp(V);