format long
fprintf(' FACTORIZATION LU DOOLITLE\n\n\n');

A= [[45,13,-4,8];[-5,-28,4,-14];[9,15,63,-7];[2,3,-8,-42]];
b= [[-25;82;75;-43]];
[n,m]=size(A);
C=[A,b];
if n==m
    for k=1:n
        L(k,k)=1; 
        sum=0;
        for p=1:k-1
            sum=sum+L(k,p)*u(p,k);
        end
        u(k,k)=(A(k,k)-sum);
        for i=k+1:n
            sum=0;
            for r=1:k-1
                sum=sum+L(i,r)*u(r,k);
            end
            L(i,k)=(A(i,k)-sum)/u(k,k); 
        end
        for j=k+1:n
            sum=0;
            for s=1:k-1
                sum=sum+L(k,s)*u(s,j);
            end
            u(k,j)=(A(k,j)-sum);
        end
    end
    memoryu=1; 
    memoryL=1;
    for i=1:n
        memoryu=memoryu*u(i,i);
    end
    multiplied=memoryL*memoryu; 
    
    if multiplied~=0
        for i=1:n
            sum=0;
            for p=1:i-1
                sum=sum+L(i,p)*z(p);
            end
            z(i)=(b(i)-sum)/L(i,i); %obtencion del vector Z
        end
        for i=n:-1:1
            sum=0;
            for p=(i+1):n
                sum = sum+u(i,p)*x(p);
            end
            x(i)=(z(i)-sum)/u(i,i);
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