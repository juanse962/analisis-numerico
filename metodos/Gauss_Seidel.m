format short
fprintf('GAUSS SEIDEL ITERATIVE METHOD\n\n\n')
a= [[20,-1,3,4];[6,23,4,3];[7,21,46,9];[-3,-9,12,38]];
b= [[30;-10;20;-14]];
x= [[0;0;0;0]];
iter=20;
tol=0.00006;
k=norm(a)*norm(a^-1);
determinante=det(a);
if determinante==0
    fprint('\Ininfite solution\n')
end
n=length(b);
d=diag(diag(a));
l=d-tril(a);
u=d-triu(a);
fprintf('\n SOLUCTION:\n')
T=((d-l)^-1)*u;
disp(T)
re=max(abs(eig(T)))
if re>1
    fprint('the method does not converge')
    
    return
end
C=((d-l)^-1)*b;
i=0;
err=tol+1;
z=[i,x(1),x(2),x(3),err];

while err>tol & i<iter
    xi=T*x+C;
    i=i+1;
    err=norm(xi-x);
    x=xi;
    z(i,1)=i;
    z(i,2)=x(1);
    z(i,3)=x(2);
    z(i,4)=x(3);
    z(i,5)=err;
end
fprintf('\nTABLE:\n\n n x1 x2 x3 Error\n\n ')
disp(z)