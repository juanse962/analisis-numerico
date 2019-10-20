print("------- POLYNOMIC INTERPOLATION (Newton) -------")

vector = [1.0, 3.0, 4.0, 5.0,7.0]
matrix = [[4.31, 0.0, 0.0, 0.0,0.0], [1.5, 0.0, 0.0, 0.0,0.0], [3.2, 0.0, 0.0, 0.0], [2.6, 0.0, 0.0, 0.0, 0.0], [1.8,0.0,0.0,0.0,0.0]]
n=len(vector)

point_evaluated = float(input("Point to evaluate: "))

for i in range(1,n):
    for j in range(i,n):

        matrix[j][i] = ( (matrix[j][i-1]-matrix[j-1][i-1]) / (vector[j]-vector[j-i]))
print (matrix)
aprx = 0
mul = 1.0
for i in range(n):
    mul = matrix[i][i];
    print(mul)
    for j in range(1,i+1):
        mul = mul * (point_evaluated - vector[j-1])
    aprx = aprx + mul

print ("Interpolated value f(",point_evaluated,") es: ", aprx)