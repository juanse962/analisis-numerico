format long

U=[[4,-1,0,3];[1,15.5,3,8];[0,-1.3,-4,1.1];[14,5,-2,30]];
b=[1;1;1;1];

[n,m]=size(U);
a=[U,b];
L=eye(n);
Z=zeros(n,1);
X=zeros(n,1);

fprintf('\n La Matriz aumentada [Ab] es = \n');
disp(a);

%%Matriz U Escalonada.

if n==m
    d=diag(a);
    for k=1: n-1
        if U(k,k)~=0
            fprintf('\n ETAPA %g=\n\n',k)
            %Se hallan los multiplicadores
            for i=(k+1):n
                m(i,k)=U(i,k)/U(k,k);
                for j=k:n
                    U(i,j)= U(i,j) - m(i,k)*U(k,j);
                    if i>j
                        L(i,j)= m(i,k);
                    end
                    if i==j
                        L(i,j)= 1;
                    end
                    if i<j
                        L(i,j)= 0;
                    end
                end
            end
            fprintf('\nLa matriz U:\n')
            disp(U)
            fprintf('\nLa matriz L correspondiente a esta etapa despu�s del proceso:\n')
            disp(L)
        end
    end
end

if U(1,1)~=0
    fprintf('\n La matriz U final es \n\n')
    disp(U)
    fprintf('\n La matriz L final es \n\n')
    disp(L)
end

%%Sustitucion progresiva Lz=b (hallo Z)
if U(1,1)~=0
 fprintf('\n\nLa solucion de Z1 hasta Zn es:\n');
 Z(1)=b(1)/L(1,1);
    for i=2:n
       Z(i)=(b(i)-L(i,1:i-1)*Z(1:i-1))/L(i,i);
    end
end  

%%Sustitucion regresiva Ux=z
if U(1,1)~=0
    fprintf('\n\nLa solucion de X1 hasta Xn es:\n');
    X(n)=Z(n)/U(n,n);
    
    for k=n-1:-1:1
        X(k)=(Z(k)-U(k,k+1:n)*X(k+1:n))/U(k,k);
    end
    disp(X);
end