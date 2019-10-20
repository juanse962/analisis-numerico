print("------- Interpolacion Polinomica (Lagrange) -------")

x = 2.5
xp = [1.0, 2.0, 3.0]
yp = [1.0, 8.0, 27.0]

numberOfPoints = len(xp)
y = 0

for i in range(numberOfPoints):
        product = yp[i]
        for j in range(numberOfPoints):
            if i != j:
                product *= (x - xp[j])/(xp[i] - xp[j])

        y += product


zipped_x_y = list(zip(xp, yp))
print("interpolated value  f({}) is = {}".format(x,y))