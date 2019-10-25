clear all
disp('Trazador cubico')
format short

x=[-1,0,3,4]
y=[15.5,3,8,1]


n=length(x)-1;
A=zeros(n*4);
b=zeros(n*4,1);

for i=1:n  
    A(i+1,[4*i-3 4*i-2 4*i-1 4*i])=[((x(1+i))^3) ((x(i+1))^2) x(i+1) 1];
    b(i+1)=y(i+1);
end
A(1,[1 2 3 4])=[((x(1))^3) ((x(1))^2)  x(1) 1];
b(1)=y(1);

for i=2:n  
     A(n+i,4*i-7:4*i)=[((x(i))^3) ((x(i))^2) x(i) 1 -((x(i))^3) -((x(i))^2) -x(i) -1];
     b(n+i)=0;
end

for i=2:n  
     A(n+(n-1)+i,4*i-7:4*i)=[(3*(x(i)^2)) (2*x(i)) 1 0 -(3*(x(i)^2)) -(2*x(i)) -1 0];
     b(n+(n-1)+i)=0;
end

for i=2:n  
     A(3*n+(i-2),4*i-7:4*i)=[(6*x(i)) 2 0 0 -(6*x(i)) -2 0 0];
     b(3*n)=0;
end

A((4*n)-1,1)=6*x(1); 
A((4*n)-1,2)=2;
b(4*n)=0;

A(4*n,(4*n)-3)=6*x(n+1);  
A(4*n,(4*n)-2)=2;
b(4*n)=0;

fprintf('La matriz del trazador cubico es: \n');
disp(A);
fprintf('El vector b es: \n');
disp(b);

fprintf('El vector solucion de los coeficientes es:\n');
fprintf('El vector solucion de los coeficientes corresponden a X^3, X^2, X y el término independiente, respectivamente:\n');

S=A\b;
for j=1:4:length(S)
    for i=j:j+3
        fprintf('%f \t',S(i));
        fprintf('%f \t',S(i)); 
        
    end
    fprintf('\n');
end