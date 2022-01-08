from math import *
import sys

def calcularDistanciaEuclidiana (puntoA, puntoB):
    suma=0
    for i in range (len(puntoA)):
        suma=suma+pow(puntoA[i]-puntoB[i],2)
    return sqrt(suma)

vector=[[58,84,34,20], [44,82,25,13],[68,50,95,26],[19,68,56,89],[14,28,86,96],[56,34,70,85],[35,20,89,16],[87,31,23,15],[91,12,6,8]]
centroide=[[100,0,0,0],[0,100,0,0],[0,0,100,0],[0,0,0,100]]

grupos=[]

print ("Los vectores son: \n")
print (vector)

for i in range(len(vector)):
    distanciaMasCercana=sys.float_info.max
    centroideMasCercano=-1
    for j in range(len(centroide)):
        distancia=calcularDistanciaEuclidiana(vector[i], centroide[j])
        if distancia<distanciaMasCercana:
            distanciaMasCercana=distancia
            centroideMasCercano=j
    grupos.append(centroideMasCercano)

print("\nLos alimentos quedan clasificados de la siguiente manera donde por medio de sus caracteristicas de nutrientes;")
print ("0 equivale a fruta por contener altos contenidos de fibra")
print("1 equivale a verduras por contener altos niveles de minerales")
print ("2 equivale a cereales por contener altos niveles de proteinas")
print ("3 equivale a productos de origen animal o leguminosas por contener altos niveles de grasas")
print (grupos)


for i in range(len(grupos)):
    for j in range(len(vector[j])):
            centroide[grupos[i]][j]= centroide[grupos[i]][j]+ vector[i][j]

for i in range (len(centroide)):
    for j in range (len(centroide[i])):
        CantidadCentroide=0
        for k in range (len(grupos)):
            if (grupos[k]== i):
                CantidadCentroide=CantidadCentroide+1
        centroide[i][j]= centroide[i][j]/CantidadCentroide

print("\nLa actualización de centroides es: ")
print(centroide)
print("\nFin de la primera iteracion")
