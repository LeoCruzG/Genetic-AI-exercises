import random
import math
from decimal import Decimal

def evaluation (q):
    fxx = q

    total = 0
    #total = (6.983*math.pow(fxx[0], 2)) + (12.415*math.pow(fxx[1], 2))-fxx[0]

    #Step
    # for x in range(len(fxx)):
    #     total += math.pow(int(fxx[x]+0.5), 2)

    #Schwefel
    # for x in range(len(fxx)):
    #     temp = 0
    #     for y in range(x+1):
    #         temp += fxx[y]
    #     total += math.pow(temp, 2)


    #Rastrigin
    for x in range(len(fxx)):
       total += math.pow(fxx[x], 2) - (10*math.cos(2*math.pi*fxx[x]) ) + 10


    return total

def vuelo(p, m, pb, v, l, vss, w, c1, c2):
    limites = l
    pobb = p
    vel = v
    mej = m
    persm = pb
    numvars = vss
    size = len(pobb)
    r1 = 0
    r2 = 0

    pvars = []
    vvars = []

    for x in range (size):
        r1 = random.random()
        r2 = random.random()
        vtemp = []
        ptemp = []

        #cálculo velocidad

        for y in range(numvars):
            velocidad_personal = c1*r1*(persm[x][y]-pobb[x][y])
            velocidad_swarm = c2*r2*(mej[y]-pobb[x][y])
            velocidad_atrasada = w*vel[x][y]
            vtemp.append(velocidad_atrasada + velocidad_personal + velocidad_swarm)
            ptemp.append(pobb[x][y] + vtemp[y])
        
        #comprobación
        #print("antes de while")
        for y in range(numvars):
            #print("for antes del while")
            while (ptemp[y]>=limites[y][0] or ptemp[y]<=limites[y][1]):
                #print("dentro de while ", y, ptemp[y], limites[y][0], limits[y][1])
                if ptemp[y] >= limites[y][0]:
                    ptemp[y] = (2*limites[y][0])-ptemp[y]
                    if ptemp[y] == limites[y][0]:
                        ptemp[y]-= 0.001
                if ptemp[y] <= limites[y][1]:
                    ptemp[y] = (2*limites[y][1])-ptemp[y]
                    if ptemp[y] == limites[y][1]:
                        ptemp[y]+= 0.001
        vvars.append(vtemp)
        pvars.append(ptemp)
    return pvars, vvars

def mutacion(p, v, F, l, s):
    limites = l
    pobb = p
    varss = v
    size = len(pobb)
    i1 = 0
    i2 = 0
    i3 = 0
    
    pvars = []

    for x in range (size):
        if (random.random() < F):
            for y in range (variables):
                pobb[x][y]= mejor[y]+random.uniform(s,-s)
                if (random.random() < F):
                    tm = int(random.uniform(0,varss))
                    while tm == y:
                        tm = int(random.uniform(0,varss))
                    pobb[x][y]= pobb[x][tm]
                    #print("switch", y, tm)
            
    return pobb

pobSize = 50
condicionParo = 200
salto = 1
variables = 10
num_variables = 10

F_value = 0.8
W_value = 0.11
c1_value = 1.6
c2_value = 1.6
step_mutacion = 3

inicioCadena2 = 24

mejor = []
pob = []
result = []
pbest = []
limits = []
velocidad = []

#rangos
for x in range (num_variables):
    rangetemp = []
    """ if x == 0:
        rangetemp.append(4)
        rangetemp.append(-2)
    elif x == 1:
        rangetemp.append(3)
        rangetemp.append(-3) """
    rangetemp.append(5.12)
    rangetemp.append(-5.12)
    limits.append(rangetemp)
    mejor.append(0)

mejor.append(10000000)

#llenado de primera población
for x in range (pobSize):
    indtmp = []
    vtemp = []
    tmprangeup = rangetemp
    for y in range (variables):
        vtemp.append(0)
        """ if y==0:
            indtmp.append(random.uniform(limits[0][0], limits[0][1]))
        elif y==1:
            indtmp.append(random.uniform(limits[1][0], limits[1][1])) """
        indtmp.append(random.uniform(limits[y][0], limits[y][1]))
    result.append(evaluation(indtmp))
    pob.append(indtmp)
    pbest.append(indtmp)
    velocidad.append(vtemp)

    if (result[x] < mejor[variables]):
        mejor[variables] = result[x]
        for y in range (variables):
            mejor[y] = pob[x][y]

print("Mejor de la población base: - f(x)", mejor[variables],  " x ", mejor[0] , " y ", mejor[1])
# for x in range (pobSize):
#     print("Individuo: ", x, " - f(x)", result[x],  " x ",pob[x][0] , " y ", pob[x][1])
#     print("Individuo: ", x, " - (v) -  x ",velocidad[x][0] , " y ", velocidad[x][1])
#     print("Individuo: ", x, " - (b) -  x ",pbest[x][0] , " y ", pbest[x][1])

for x in range(condicionParo):
    #print("start")
    temp = vuelo(pob, mejor, pbest, velocidad, limits, variables, W_value, c1_value, c2_value)
    ptemp = temp[0]
    vtemp = temp[1]
    #print("después de vtemp y ptemp")
    if random.random() < 0.5 :
        ptemp = mutacion(ptemp, variables, F_value, limits, step_mutacion)

    pob = ptemp
    velocidad = vtemp
   # print("después de mutacion")

    for y in range (pobSize):
        
        rtemp = evaluation(pbest[y])
        result[y] = evaluation(pob[y])
        if (rtemp > result[y]):
            for z in range (variables):
                pbest[y][z] = pob[y][z]

        if (result[y] < mejor[variables]):
            mejor[variables] = result[y]
            for z in range (variables):
                mejor[z] = pob[y][z]
    #print("después evaluación")
    if (x==int(condicionParo/2)):
        step_mutacion = 1
    if(x==int(condicionParo/4)):
        step_mutacion = 0.5
    print("Iteración:", x+1," - f(x)", mejor[variables],  " x1 ", mejor[0] , " x2 ", mejor[1])

print("Los mejores valores fueron: x1", mejor[0] , " x2 ", mejor[1], " con un valor de f(x) de ", mejor[variables])

""" test = []
test.append(0.12876951694488525)
test.append(0.019100487232208252)
print(evaluation(test))
test = []
test.append(0.07316113390459211)
test.append(-.000000291536470191204)
print(evaluation(test))
fxx = []
fxx.append(100)
fxx.append(200)
fxx.append(3000)
for x in range(len(fxx)):
    print(x) """