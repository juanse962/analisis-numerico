format short 
fprintf('JACOBI ITERATIVE METHOD\n\n\n')
a= [[3,-1,1];[3,4,2];[3,3,6];
b= [[1;0;4]];
x= [[0;0;0]];
iter=20;
tol=0.000001;
cond=norm(a)*norm(a^-1);
determinante=det(a);
if determinante==0
    fprint('\Ininfite solution\n')
    return
end
n=length(b);
d=diag(diag(a)); 
l=d-tril(a);
u=d-triu(a);
T=d^-1*(l+u); 
re=max(abs(eig(T)))
if re>1
    fprint('the method does not converge')
    return
end
C=d^-1*b;
i=0;
err=tol+1;
z=[i,x(1),x(2),x(3),err];
while err>tol & i<iter
    
    xi=T*x+C;
    err=norm(xi-x);
    x=xi;
    i=i+1;
    z(i,1)=i;
    z(i,2)=x(1);
    z(i,3)=x(2);
    z(i,4)=x(3);
    z(i,5)=err;
end
fprintf('\nTABLE:\n\n n x1 x2 x3 Error\n\n ');
disp(z)