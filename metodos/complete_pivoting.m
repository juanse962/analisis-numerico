function X = complete_pivoting(A,b)
A= A;
b= b;
[n,m]=size(A);
C=[A,b];
if n==m
    for i=1:n
        mark(i)=i;
    end
    for k=1:(n-1)
        fprintf('\n Stage %g=\n\n',k)
        max=0;
        row=k;
        colum=k;
        for p=k:n
            for r=k:n
                if max<abs(C(p,r))
                    max=abs(C(p,r));
                    row=p;
                    colum=r;
                end
            end
        end
        if max ==0
            fprintf('\nThe system has infinite solutions\n')
            break
            
        else
            if row ~= k
                for j=1:(n+1)
                    aux=C(k,j);
                    C(k,j)=C(row,j);
                    C(row,j)=aux;
                end
                
            end
            if colum ~= k
                for i=1:n
                    aux=C(i,k);
                    C(i,k)=C(i,colum);
                    C(i,colum)=aux;
                end
                aux = mark(k);
                mark(k)= mark(colum);
                mark(colum)=aux;
            end
        end
        fprintf('\nThe matrix corresponding to this stage after the process:\n')
        disp(C)
        fprintf('\nThe Multipliers corresponding to this stage are:\n')
        for i=(k+1):n
            m(i,k)=C(i,k)/C(k,k);
            fprintf('\nm(%g,%g)=',i,k)
            disp(m(i,k));
            for j=k:(n+1)
                C(i,j)= C(i,j) - m(i,k)*C(k,j);
            end
        end
        fprintf('\nThe matrix corresponding to this stage after the process:\n')
        disp(C)
    end
    mark(colum)=aux
    for i=n:-1:1
        sum=0;
        for p=(i+1):n
            sum = sum + C(i,p)*X(p);
        end
        X(i)=(C(i,n+1)-sum)/C(i,i);
    end
    
    for i=1:n
        for j=1:n
            if mark(j)==i
                k=j;
            end
        end
        aux=X(k);
        X(k)=X(i);
        X(i)=aux;
        aux=mark(k);
        mark(k)=mark(i);
        mark(i)=aux;
    end
else %
    fprintf('\nThe matrix is not square\n');
end
fprintf('\n\n SOLUTION:\n');

fprintf('\n\nThe matrix Ab final:\n');
disp(C);
fprintf('\n\nThe solution de X1 to Xn es:\n');

for i=1:n
    Xi=X(1,i);
    fprintf('\nX%g=',i)
    disp(Xi);
end
end