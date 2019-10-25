A=[[4,-1,0,3];[1,15.5,3,8];[0,-1.3,-4,1.1];[14,5,-2,30]];
B=[1;1;1;1];
 
[n,n]=size(A);
X=zeros(n,1);
D=zeros(n,1);
C=zeros(1,n);
Cp=zeros(1,n);
L=eye(n);
P=eye(n);
U=zeros(n,n);
U=A;
 
for q=1:n-1
 
    [y,j]=max(abs(U(q:n,q)));
    C=U(q,:);
    U(q,:)=U(j+q-1,:);
    U(j+q-1,:)=C;
 
    Cp=P(q,:);
    P(q,:)=P(j+q-1,:);
    P(j+q-1,:)=Cp;
  
    %Calculo del multiplicador,
 
    for k=q+1:n
    m=U(k,q)/U(q,q);
    L(k,q) = m
    U(k,q:n)=U(k,q:n)-m*U(q,q:n)
    end
end
h=L(2,1);
L(2,1)=L(3,1);
L(3,1)=h;
 
%comprobacion
 
PA=P*A;
LU=L*U;
PB=P*B;
 
D(1)=PB(1)/L(1,1);
for k=2:n
   D(k)=(PB(k)-L(k,1:k-1)*D(1:k-1))/L(k,k);
end
 
X(n)=D(n)/U(n,n);
 
for k=n-1:-1:1
    X(k)=(D(k)-U(k,k+1:n)*X(k+1:n))/U(k,k);
end
X