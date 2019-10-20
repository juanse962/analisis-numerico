x1 = [2,3,4,5,6];
A = ones(length(x1), length(x1));
b=[[2;6;5;5;6]];
A(:,2) = x1;
for i = 3:length(x1)
    A(:,i) = x1.^(i-1);
end
disp(A);
a = complete_pivoting(A,b);
fprintf("Coefficients Vandermounde");
disp(a);