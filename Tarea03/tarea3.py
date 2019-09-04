from sympy import *
import math
x = symbols('x')
y = symbols('y')
z = symbols('z')

def biseccion_circunferencia(intervalo,niter,tolerancia,function_circulo,v,a):

    xi = intervalo[0][0][0]
    yi = intervalo[0][0][1]
    zi = intervalo[0][0][2]
    xf = intervalo[0][1][0]
    yf = intervalo[0][1][1]
    zf = intervalo[0][1][2]
    alphai = (x)
    alphaf = 1
    niter = niter

    function_circulo = function_circulo

    fxi_circulo = function_circulo.subs(x, xi).subs(y,yi).subs(z,zi)
    fxf_circulo = function_circulo.subs(x, xf).subs(y,yf).subs(z,zf)

    if(fxi_circulo == 0):
        return[xi,yi.zi]
    elif (fxf_circulo == 0):
        return [xf,yf,zf]
    elif (fxi_circulo * fxf_circulo < 0):
        xm = (xi+xf)/2
        ym = (yi+yf)/2
        zm = (zi+zf)/2

        fxm_circulo = function_circulo.subs(x, xm).subs(y,ym).subs(z,zm)
        count = 1
        error = float(tolerancia) + 1
        while (error > tolerancia) and (count < niter) and (fxm_circulo != 0):
            if(fxi_circulo * fxm_circulo < 0):
                xf = xm
                yf = ym
                zf = zm
                rf = recta_r3([(xi, yi, zi)], [(xf,yf, zf)],a,v)
                fxf_circulo = function_circulo.subs(x, rf[0]).subs(y,rf[1]).subs(z,rf[2])

            else:
                xi = xm
                yi = ym
                zi = zm
                ri = recta_r3([(xf, yf, zf)], [(xi,yi, zi)],a,v)               
                fxi_circulo = function_circulo.subs(x,ri[0]).subs(y,ri[1]).subs(z,ri[2])  
            xaux = xm  
            xm = (xi+xf)/2
            ym = (yi+yf)/2
            zm = (zi+zf)/2
            rm = recta_r3([(xm, ym, zm)], [(0,0, 0)],a,v)
            fxm_circulo = function_circulo.subs(x, rm[0]).subs(y,rm[1]).subs(z,rm[2])
            error = abs(xm-xaux)
            count += 1 
        if(fxm_circulo == 0):
            return [xm,ym,zm]
        elif(error < tolerancia):
            return[xm,ym,zm]
        else:
            print("Fracaso el numero de iteraciones: ",niter)    

def recta_r3(punto0,punto1,alpha,v):
    
    x = punto0[0][0]+(v[0][0]*alpha)
    y = punto0[0][1]+(v[0][1]*alpha)
    z = punto0[0][2]+(v[0][2]*alpha)

    return x,y,z

def busqueda_esfera(p0,p1,delta,niter, function_esfera):
    intervalos = []
    v1 = p1[0]-p0[0]
    if p0[0]<p1[0]: a = delta/v1
    else: a = -delta/v1
    v=[((p1[0]-p0[0]),(p1[1]-p0[1]),(p1[2]-p0[2]))]

    pia = [p0[0], p0[1], p0[2]]
    fx0 = function_esfera.subs(x, pia[0]).subs(y,pia[1]).subs(z,pia[2])
    if fx0 == 0:
        print("Raiz en (",pia[0],",",pia[1],",",pia[2],")")

    pid = [0, 0, 0]
    pid[0], pid[1], pid[2] = recta_r3([(p0[0], p0[1], p0[2])], [(p1[0], p1[1], p1[2])],a,v)
    fx1 = function_esfera.subs(x, pid[0]).subs(y,pid[1]).subs(z,pid[2])
    if fx1 == 0:
        print("Raiz en (",pid[0],",",pid[1],",",pid[2],")")
    count=1
    while (count < niter) and (pid[0] != p1[0] or pid[1] != p1[1] or pid[2] != p1[2]):
        if fx0 * fx1 < 0:
            intervalo = [(pia[0],pia[1],pia[2]), (pid[0],pid[1],pid[2])]
            intervalos.append(intervalo)
        pia[0] = pid[0]
        pia[1] = pid[1]
        pia[2] = pid[2]
        pid[0], pid[1], pid[2] = recta_r3([(pid[0], pid[1], pid[2])], [(p1[0], p1[1], p1[2])],a,v)
        fx0 = fx1
        fx1 = function_esfera.subs(x, pid[0]).subs(y,pid[1]).subs(z,pid[2])
        if fx1 == 0:
            print("Raiz en (",pid[0],",",pid[1],",",pid[2],")")
        count += 1

    return intervalos,v,a

def raices_circunferencia(p0,p1,delta,niter):

    print("-----Raices en r3-----\n")
    function_esfera = x**2+y**2+z**2 - 4
    intervalos = busqueda_esfera(p0, p1, delta, niter, function_esfera)
    for i in range(len(intervalos[0])):
        raiz = biseccion_circunferencia([intervalos[0][i]],niter,0.00048,function_esfera,intervalos[1],intervalos[2])
        print ("Para el intervalo: {0} tiene una raiz en: {1}".format(intervalos[0][i],raiz))

raices_circunferencia([-2.08,-0.19,0],[1.25,-0.59,1.45],0.2,100)