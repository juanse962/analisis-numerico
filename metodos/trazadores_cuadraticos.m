clc
clear all

x   =   input('\nIngrese el vector x= ');
y   =   input('Ingrese el vector y= ');
N   =   length(x)-1;
V   =   [0;zeros(2*N,1);zeros(N-1,1)];
Z   =   zeros(length(V),length(V));
j=1;
f=1;

for i=2:2:2*N    
    Z(i,f:f+2)          =   [x(j)^2 x(j) 1];
    V(i)                =   y(j);
    j                   =   j+1;
    Z(i+1,f:f+2)        =   [x(j)^2 x(j) 1];  
    V(i+1)              =   y(j);
    f                   =   f+3;
end

j=1;
l=2;
for i=2*N+2:3*N
    
    Z(i,j:j+1)            =   [2*x(l) 1];
    Z(i,j+3:j+4)          =   [-2*x(l) -1];
    j                     =   j+3;
    l                     =   l+1;
end

Z(1,1)=1;
Coeff       =       Z\V;
pos=1;
valor=length(x);
valor1=1;
valor2=3;
fprintf('Los tramos correspondientes son: %g \n',N);
    
    for i=1:(length(x)-1) 
        fprintf('\nEntre xi y xf : %g y %g\n\n',x(pos),x(pos+1));
        fprintf('Los coeficientes corresponden a X^2, X y el término independiente, respectivamente\n\n');
        for i=valor1:(valor2)
            a=Coeff(i,1);
            fprintf('%f \t', a);
        end
        
        fprintf('\nEntre xi y xf : %g y %g\n\n',x(pos),x(pos+1)); 
        fprintf('Los coeficientes corresponden a X^2, X y el término independiente, respectivamente\n\n');
        
        for i=valor1:(valor2)
            a=Coeff(i,1);
            fprintf('\n%f \t\n', a);
        end
        
        valor1=valor1+3;
        valor2=valor2+3;
        pos=pos+1;
    end