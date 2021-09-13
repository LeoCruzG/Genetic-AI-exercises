import random
import math
from decimal import Decimal

def evaluation (q):
    fxx = q

    total = 0
    #total = (6.983*math.pow(fxx[0], 2)) + (12.415*math.pow(fxx[1], 2))-fxx[0]
    #total = 6.983*(math.pow(fxx[0], 2))
    #total += 12.415*(math.pow(fxx[1], 2))
    #total -= fxx[0]

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

def mutacion(p, v, F, l):
    limites = l
    pobb = p
    varss = v
    size = len(pobb)
    i1 = 0
    i2 = 0
    i3 = 0
    
    pvars = []

    for x in range (size):
        ptemp = []

        i1 = random.randrange(0, size)
        while (i1 == x):
            i1 = random.randrange(0, size)
        
        i2 = random.randrange(0, size)
        while (i2 == x or i2 == i1):
            i2 = random.randrange(0, size)
        
        i3 = random.randrange(0, size)
        while (i3 == x or i3 == i1 or i3 == i2):
            i3 = random.randrange(0, size)
        

        #diferencia
        
        for y in range(varss):
            ptemp.append(F*(pobb[i1][y]-pobb[i2][y]))

        #suma del tercer vector
        for y in range(varss):
            ptemp[y]=ptemp[y]+pobb[i3][y]
        
        #comprobación
        for y in range(varss):
            while (ptemp[y]>=limites[y][0] or ptemp[y]<=limites[y][1]):
                if ptemp[y] >= limites[y][0]:
                    ptemp[y] = (2*limites[y][0])-ptemp[y]
                if ptemp[y] <= limites[y][1]:
                    ptemp[y] = (2*limites[y][1])-ptemp[y]
        pvars.append(ptemp)
    return pvars

def recombinacion(p, m, s, v, cr):
    pobb = p
    mutt = m
    res_pob = []
    varss = v
    CR = cr
    trail_v = []


    #recombinacion
    for x in range(s):
        switcher = []
        for y in range(varss):
            #no se incluye el jrand = j porque cr se va a dejar en 0.5
            r = random.random()
            #print(x, y)
            if (r<CR):
                switcher.append(mutt[x][y])
            elif (r>CR):
                switcher.append(pobb[x][y])
            elif (r==CR):
                switcher.append(pob[x][y])
                
        trail_v.append(switcher)
    
    #for x in range (s):
        #print("Recombinado: ", x," f(x)",evaluation(trail_v[x]), " x ",trail_v[x][0] , " y ", trail_v[x][1])


    #seleccion
    for x in range(s):
        tempEvalPob = evaluation(pobb[x])
        tempEvalTrail = evaluation(trail_v[x])

        if (tempEvalTrail < tempEvalPob):
            res_pob.append(trail_v[x])
        elif (tempEvalTrail > tempEvalPob):
            res_pob.append(pobb[x])
        elif(tempEvalTrail == tempEvalPob):
            res_pob.append(pobb[x])
        


    return res_pob

pobSize = 60
#upplimit = 4
#lowlimit = -2
#upplimitv2 = 3
#lowlimitv2 = -3
condicionParo = 300
salto = 1
variables = 10

F_value = 0.1
CR_value = 0.1
num_variables = 10


inicioCadena2 = 24

mejor = []
pob = []
result = []
ind = []
limits = []

for x in range (num_variables):
    rangetemp = []
    # if x == 0:
    #     rangetemp.append(4)
    #     rangetemp.append(-2)
    # elif x == 1:
    #     rangetemp.append(3)
    #     rangetemp.append(-3)
    # rangetemp.append(100)
    # rangetemp.append(-100)
    rangetemp.append(5.12)
    rangetemp.append(-5.12)
    limits.append(rangetemp)
    mejor.append(0)

mejor.append(10000000)

for x in range (pobSize):
    indtmp = []
    tmprangeup = rangetemp
    for y in range (variables):
        # if y==0:
        #     indtmp.append(random.uniform(limits[0][0], limits[0][1]))
        # elif y==1:
        #     indtmp.append(random.uniform(limits[1][0], limits[1][1]))
        indtmp.append(random.uniform(limits[y][0], limits[y][1]))
    result.append(evaluation(indtmp))
    pob.append(indtmp)
    if (result[x] < mejor[variables]):
        mejor[variables] = result[x]
        for y in range (variables):
            mejor[y] = pob[x][y]

print("Mejor población base: - f(x)", mejor[variables],  " x ", mejor[0] , " y ", mejor[1])
#for x in range (pobSize):
    #print("Individuo: ", x, " - f(x)", result[x],  " x ",pob[x][0] , " y ", pob[x][1])

#ptemp = mutacion(pob, variables, F_value, limits)

#for x in range (pobSize):
    #print("Mutante: ", x, " x ",ptemp[x][0] , " y ", ptemp[x][1])

#pob = recombinacion(pob, ptemp, pobSize, num_variables, CR_value)

#for x in range (pobSize):
    #result[x] = evaluation(pob[x])
    #if (result[x] < mejor[variables]):
       # mejor[variables] = result[x]
       # for y in range (variables):
            #mejor[y] = pob[x][y]
    #print("Individuo: ", x, " - f(x)", result[x],  " x ",pob[x][0] , " y ", pob[x][1])

#print("Mejor: - f(x)", mejor[variables],  " x ", mejor[0] , " y ", mejor[1])

# jrand es siempre aleatorio y se hace cada que se entra al for
# tarea - leer documento,  y probarlo en otras funciones
# 2 x limite_violado x valor_que_viola --- repetir hasta que quede dentro de los límites

for x in range(condicionParo):
    ptemp = mutacion(pob, variables, F_value, limits)

    pob = recombinacion(pob, ptemp, pobSize, num_variables, CR_value)

    for y in range (pobSize):
        result[y] = evaluation(pob[y])
        if (result[y] < mejor[variables]):
            mejor[variables] = result[y]
            for z in range (variables):
                mejor[z] = pob[y][z]

    print("Iteración:", x+1," - f(x)", mejor[variables],  " x1 ", mejor[0] , " x2 ", mejor[1])

print("Los mejores valores fueron: x1", mejor[0] , " x2 ", mejor[1], " con un valor de f(x) de ", mejor[variables])
test = []
test.append(0.07316113390459211)
test.append(-.000000291536470191204)
#print(evaluation(test))