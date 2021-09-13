import random
import numpy as np
import math

def binarycode(s):
    size = s
    c = []
    for x in range(size):
        if random.random()<0.5:
            c.append("0")
        else:
            c.append("1")
    return c

def randomChange(c, s, x, p, rand):
    size = s
    code = c
    spot = random.randint(0, size-1)
    #if random.random()<0.5:
    #    code[spot]="0"
    #else:
    #    code[spot]="1"
    #print(code)
    if (code[spot] == "1"):
        code[spot] = "0"
    else : 
        code[spot] = "1"
    #print("Individuo ", x, " fue mutado en: ", spot, " y quedó como ", code[spot], " random ",rand, " probabilidad ", p )
    #print(code)
    return code

def toDecimals(c, ll, ul, size):
    question = c
    answer = 0
    
    answer = ll+((question/(pow(2,size)-1))*(ul-ll))

    return answer

def evaluation (q):
    t = float(q)
    y0 = 300.0
    m = 0.25
    k = 0.1
    g = -32.17

    p1 = 0.0
    p2 = 0.0
    p3 = 0.0

    p1 = y0 + (((m*g)/k)*t)
    p2 = ((math.pow(m, 2))*g)/(math.pow(k,2))
    p3 = 1-math.exp(((-1)*k*t)/m)

    total = p1-(p2*p3)
    return total

def torneo (ps, p, dp):
    torneos = pobSize // 2
    poblacion = p
    pobDecimal = dp
    padres = []
    rango = (len(poblacion))
    contador = 1

    
    for x in range (torneos):
        tmpa = random.randrange(rango)
        tmpb = random.randrange(rango)
        winner  = 0
        
        while tmpa == tmpb:
            tmpb = random.randrange(rango)

        if (abs(evaluation(pobDecimal[tmpa])) < abs(evaluation(pobDecimal[tmpb]))):
            padres.append(poblacion[tmpa])
            winner = tmpa
        elif (abs(evaluation(pobDecimal[tmpa])) > abs(evaluation(pobDecimal[tmpb]))):
            padres.append(poblacion[tmpb])
            winner = tmpb
        else :
            padres.append(poblacion[tmpa])
            winner = tmpa

        #print("Torneo ",contador,": Individuo ", tmpa, " vs ", tmpb, " Ganador : ", winner)
        contador+=1
        winner2 = winner
        
        while (winner2 == winner ):
            tmpa = random.randrange(rango)
            tmpb = random.randrange(rango)
            
            while tmpa == tmpb:
                tmpb = random.randrange(rango)
            
            if (abs(evaluation(pobDecimal[tmpa])) < abs(evaluation(pobDecimal[tmpb]))):
                winner2 = tmpa
            elif (abs(evaluation(pobDecimal[tmpa])) > abs(evaluation(pobDecimal[tmpb]))):
                winner2 = tmpb
            else :
                winner2 = tmpa
        padres.append(poblacion[winner2])
        #print("Torneo ",contador,": Individuo ", tmpa, " vs ", tmpb, " Ganador : ", winner2)
        contador+=1

    return padres

def cruza (p, ps, s, pc):
    padres = p
    size = ps // 2
    rango = (len(padres)-1)+1
    longitud = s
    hijos = []
    arrTemp1 = []
    arrTemp2 = []
    contador = 0
    for x in range (size):
        r = random.random()
        if (r<pc):
            arrTemp1=[]
            arrTemp2=[]
            puntoCruza = random.randrange(rango) + 1 
            switch = True 
            for y in range (longitud):
                if puntoCruza == y:
                    switch = False
                if (switch):
                    arrTemp1.append(padres[contador][y])
                    arrTemp2.append(padres[contador+1][y])
                else:
                    arrTemp1.append(padres[contador+1][y])
                    arrTemp2.append(padres[contador][y])
            #print("Pareja - ", (x+1)," punto de cruza - ", puntoCruza, ", numero aleatorio - ", r, ", probabilidad - ", pc)
            hijos.append(arrTemp1)
            hijos.append(arrTemp2)
        else: 
            hijos.append(padres[contador])
            hijos.append(padres[contador+1])
            #print("Pareja - ", (x+1)," sin cruza, numero aleatorio - ", r, ", probabilidad - ", pc)
        contador+=2
    return hijos
    
def mutacion(h, s, p):
    hijos = h
    longitudCadena = s
    probMutacion = p
    size = len(hijos)
    for x in range (size):
        rand = random.random()
        if (rand < probMutacion):
            hijos[x] = randomChange(hijos[x], longitudCadena, x, p, rand)

    return hijos
    



size = 23
pobSize = 50
upplimit = 8
lowlimit = 0
probabilidadCruza = 0.6
probabilidadMutacion = 0.1
minimo = 10000
condicionParo = 50
salto = 1

mejor = []
pob = []
parsedpob = []
decimalpob = []
padres = []
hijos = []

test = np.array([])

code = binarycode(size)
#print (code)
for x in range (pobSize):
    temp = binarycode(size)
    pob.append(temp)
    parsedpob.append(int("".join(temp), 2))
    decimalpob.append(toDecimals(parsedpob[x], lowlimit, upplimit, size))

for x in range (pobSize):
    temp = evaluation(decimalpob[x])
    if (temp < minimo and temp > 0):
        mejor = decimalpob[x]
        minimo = temp

#for x in range (pobSize):
 #   print("Individuo ", x, " - ","".join(pob[x]),  " ", parsedpob[x], " ", round(decimalpob[x], 3), " " , round(evaluation(decimalpob[x]), 3))

print("Generación inicial : Mejor valor ",mejor, "s - y(t): ",minimo)

for v in range (condicionParo):

    padres = torneo(size, pob, decimalpob)

    #for x in range (pobSize):
     #  print("Padre ",x," - ","".join(padres[x]))

    #print("--Cruza--")

    hijos = cruza(padres, pobSize, size, probabilidadCruza)

    #for x in range (pobSize):
     #  print("Hijo ",x," - ","".join(hijos[x]))

    #print ("--Mutación--")

    hijos = mutacion(hijos, size, probabilidadMutacion)

    pob = hijos

    for x in range (pobSize):
        parsedpob[x]=(int("".join(pob[x]), 2))
        decimalpob[x]=(toDecimals(parsedpob[x], lowlimit, upplimit, size))
        if (evaluation(decimalpob[x]) < minimo and evaluation(decimalpob[x])>0):
            mejor = decimalpob[x]
            minimo = evaluation(decimalpob[x])

    if (v%salto == 0):
        print("Generación ", (v+1),": Mejor valor ",mejor, "s - y(t): ",minimo)
    #for x in range (pobSize):
     #  print("Individuo ", x, " - ","".join(pob[x]),  " ", parsedpob[x], " ", round(decimalpob[x], 6), " " , round(evaluation(decimalpob[x]), 6))

print ("El mejor valor fue ", mejor, "s - y(t): ",minimo)
