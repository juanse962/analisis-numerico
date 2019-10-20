format long
fprintf('GAUSS SEIDEL ITERATIVE METHOD\n\n\n')
a= [[5,3,1];[3,4,-1];[1,-1,4]];
b= [[24;30;-24]];
x= [[0;0;0]];
iter=40;
tol=0.00001;
w=1;
k=norm(a)*norm(a^-1);
determinant=det(a);
if determinant==0
    fprint('\Ininfite solution\n')
end
n=length(b);
d=diag(diag(a)); 
l=d-tril(a); 
u=d-triu(a); 
Tw=((d-w*l)^-1)*((1-w)*d+w*u); 
T=((d-l)^-1)*u;
disp(T)
re=max(abs(eig(T)))
if re>1
    fprint('the method does not converge')
return
end
fprintf('\nEl vector constante es::\n')
Cw=w*(d-w*l)^-1*b; 
disp(Cw)
i=0;
err=tol+1;
z=[i,x(1),x(2),x(3),err]; 
while err>=tol & i<=iter

xi=Tw*x+Cw;
err=norm(xi-x);
x=xi;
i=i+1;
z(i,1)=i;
z(i,2)=x(1);
z(i,3)=x(2);
z(i,4)=x(3);
z(i,5)=err;
end
fprintf('\nTABLE:\n\n n x1 x2 x3 Error\n\n ')
disp(z)