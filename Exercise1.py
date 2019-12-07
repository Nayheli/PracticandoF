def main():
    nombresP=[]
    edadP=[]
    generoP=[]

    N=-1
    while N<=0 or N>30:
        N = int(input("Ingrese numero de personas: "))
    for i in range(N):
        nombre=input("Nombre "+str(i+1)+" : ")    
        nombresP.append(nombre)
        ed=-1
        while ed<=0 or ed>99:
            ed=int(input("Edad "+str(i+1)+" : "))
            edadP.append(ed)

        ge=""
        while ge!="F" and ge!="M":
            ge= input("Genero "+str(i+1)+" : ")
            generoP.append(ge)
    sumaM=0
    sumaF=0
    contador=0
    for i in range (N):
        if generoP[i]=="M":
            sumaM=sumaM+edadP[i]
            contador=contador+1
        else:
            sumaF=sumaF+edadP[i]
    promedioM=sumaM/contador            
    promedioF=sumaF/(N-contador)
    print



if __name__ == "__main__":
    main()
