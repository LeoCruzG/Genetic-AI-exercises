import random
import numpy as np
import math
from decimal import Decimal

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

def toDecimals(c, ll, ul, llv2, ulv2, sizev1, sizev2):
    question = c
    answer = []

    answer.append(ll+((c[0]/(pow(2,sizev1)-1))*(ul-ll)))
    #print(question[0], " - " ,answer[0])
    answer.append(llv2+((c[1]/(pow(2,sizev2)-1))*(ulv2-llv2)))
    #print(question[1], " - ",answer[1])
    return answer

def parsed(c, ini):
    cadena = c
    var = []

    tmp1 = []
    tmp2 = []
    for x in range(ini):
        tmp1.append(cadena[x])
    for x in range(ini, len(c)):
        tmp2.append(cadena[x])
    var.append(int("".join(tmp1), 2))
    var.append(int("".join(tmp2), 2))

    return var

def evaluation (q):
    fxx = q

    total = 0
    #total = (math.pow(fxx[0], 2))+(math.pow(fxx[1] ,2))

    #total = (math.pow((1.5-fxx[0]+(fxx[0]*fxx[1])), 2))
    #total += (math.pow((2.25-fxx[0]+(fxx[0]*(math.pow(fxx[1],2)))), 2)) 
    #total += math.pow((2.625-fxx[0]+(fxx[0]*(math.pow(fxx[1], 3)))), 2)

    total = 6.983*(math.pow(fxx[0], 2))
    total += 12.415*(math.pow(fxx[1], 2))
    total -= fxx[0]
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

        if (evaluation(pobDecimal[tmpa]) < evaluation(pobDecimal[tmpb])):
            padres.append(poblacion[tmpa])
            winner = tmpa
        elif (evaluation(pobDecimal[tmpa]) > evaluation(pobDecimal[tmpb])):
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
    
# tamaño cadena, decodificacion, funcion objetivo


size = 46
pobSize = 200
upplimit = 4
lowlimit = -2
upplimitv2 = 3
lowlimitv2 = -3
probabilidadCruza = 0.6
probabilidadMutacion = 0.1
minimo = 10000
condicionParo = 300
salto = 1

inicioCadena2 = 24

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
    parsedpob.append(parsed(temp, inicioCadena2))
    decimalpob.append(toDecimals(parsedpob[x], lowlimit, upplimit, lowlimitv2, upplimitv2, (inicioCadena2-1), (size-inicioCadena2-1)))

#for x in range (pobSize):
    #print("Individuo ", x, " - ","".join(pob[x]),  " ", parsedpob[x], " ", decimalpob[x])

for x in range (pobSize):
    temp = evaluation(decimalpob[x])
    if (temp < minimo and temp > 0):
        mejor = decimalpob[x]
        minimo = temp

#for x in range (pobSize):
    #print("Individuo ", x, " - ","".join(pob[x]),  " ", parsedpob[x], " ", decimalpob[x], " " , round(evaluation(decimalpob[x]), 3))

print("Generación inicial : Mejor valor ",mejor, " - f(x1, x2): ",minimo)

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
        parsedpob[x]=parsed(pob[x], inicioCadena2)
        decimalpob[x]=(toDecimals(parsedpob[x], lowlimit, upplimit, lowlimitv2, upplimitv2, (inicioCadena2-1), (size-inicioCadena2-1)))
        if (evaluation(decimalpob[x]) < minimo):
            mejor = decimalpob[x]
            minimo = evaluation(decimalpob[x])

    if (v%salto == 0):
        print("Generación", (v+1),": Mejores valores x1:",mejor[0],"x2:", mejor[1],"- f(x1, x2): ",minimo)
    #for x in range (pobSize):
     #  print("Individuo ", x, " - ","".join(pob[x]),  " ", parsedpob[x], " ", round(decimalpob[x], 6), " " , round(evaluation(decimalpob[x]), 6))


print ("El mejor valor fue ", mejor, " - f(x1, x2): ", minimo)
testing = []
testing.append(0.07236)
testing.append(-0.00469)
#print (evaluation(testing))
