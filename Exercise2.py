NOMBREP=[]
VOTOS=[]

print("Ingrese los nombres de los 6 partidos politicos")
for i in range(6):
    nombre=input("NOMBREP["+str(i+1)+"] = ")
    NOMBREP.append(nombre)

print("Ingrese los votos de los 6 partidos politicos")
for i in range(6):
    votos=int(input("VOTOS["+str(i+1)+"] = "))  
    VOTOS.append(votos)

mayor=0
for i in range(6):
    if VOTOS[i]>mayor:
        mayor=VOTOS[i]
        posGanador=i

print("El partidfo ganador es : ",NOMBREP[posGanador]," obtuvo ",mayor," votos")              