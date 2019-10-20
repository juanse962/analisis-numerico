format short
fprintf(' FACTORIZACION LU CROULT\n\n\n');

A=[[3,-2,-2,-1];[-2,8,-2,-2];[-2,-2,4,2];[-1,-2,2,3]];
b = [[0;0;0;0]];
[n,m]=size(A);
C=[A,b];

if n==m
    for k=1:n

        u(k,k)=1;
        suma=0;
        for p=1:k-1
            suma=suma+L(k,p)*u(p,k);
        end
        L(k,k)=(A(k,k)-suma);
        
        for i=k+1:n
            suma=0;
            for r=1:k-1
                suma=suma+L(i,r)*u(r,k);
            end
            L(i,k)=(A(i,k)-suma);
        end
        for j=k+1:n
            suma=0;
            for s=1:k-1
                suma=suma+L(k,s)*u(s,j);
            end
            u(k,j)=(A(k,j)-suma)/L(k,k); 
        end
    end
    memoriau=1; 
    memoriaL=1; 
    for i=1:n
        memoriaL=memoriaL*L(i,i);
    end
    producto=memoriaL*memoriau; %calculo del determinante total
    
    if producto~=0
        for i=1:n
            suma=0;
            for p=1:i-1
                suma=suma+L(i,p)*z(p);
            end
            z(i)=(b(i)-suma)/L(i,i); %obtencion del vector Z
        end
        for i=n:-1:1
            suma=0;
            for p=(i+1):n
                suma = suma+u(i,p)*x(p);
            end
            x(i)=(z(i)-suma)/u(i,i); 
        end
    else
        fprintf('\nEl determinante es igual a cero, por lo tanto el sistema tiene infinita o ninguna solucion\n')
    end
end
fprintf('Matriz Ab:\n')
disp(C)
fprintf('Matriz L:\n')
disp(L)
fprintf('Matriz U:\n')
disp(u)
fprintf('El vector Z:\n')
disp(z)
fprintf('\n\nLa solucion de X1 hasta Xn es:\n');
for i=1:n
    xi=x(1,i);
    fprintf('\nX%g=',i)
    disp(xi);
end