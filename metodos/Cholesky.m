format short
fprintf(' FACTORIZACION LU CHOLESKY\n\n\n');
A=[[7,-2,-2,-1];[-2,8,-2,-2];[-2,-2,6,2];[-1,-2,-2,10]];
b = [[0;0;0;0]];
[n,m]=size(A);
C=[A,b];
disp(C)
if n==m
    for k=1:n
        sum1=0;
        for p=1:k-1
            sum1=sum1+L(k,p)*u(p,k);
        end
        L(k,k)=sqrt(A(k,k)-sum1);
        u(k,k)=L(k,k);
        for i=k+1:n
            sum2=0;
            for q=1:k-1
                sum2=sum2+L(i,q)*u(q,k);
            end
            L(i,k)=(A(i,k)-sum2)/L(k,k); 
        end
        for j=k+1:n
            sum3=0;
            for r=1:k-1
                sum3=sum3+L(k,r)*u(r,j);
            end
            u(k,j)=(A(k,j)-sum3)/L(k,k);
        end
    end
    producto=det(L)*det(u) 
    if producto~=0
        for i=1:n
            suma=0;
            for p=1:i-1
                suma=suma+L(i,p)*z(p);
            end
            z(i)=(b(i)-suma)/L(i,i);
        end
        for i=n:-1:1
            suma=0;
            for p=i+1:n
                suma = suma+u(i,p)*x(p);
            end
            x(i)=(z(i)-suma)/u(i,i); 
        end
    else
        fprintf('\Ininfite solution\n')
    end
end
fprintf('Matrix L:\n')
disp(L)
fprintf('Matrix U:\n')
disp(u)
fprintf('The vector Z:\n')
disp(z)

fprintf('\n\n Solution X1 to Xn is:\n');

for i=1:n
    xi=x(1,i);
    fprintf('\nX%g=',i)
    disp(xi);
end