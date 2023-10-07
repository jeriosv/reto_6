import math
import random
import statistics as stats

def promedio(a,b,c,d,e): 
    return((a+b+c+d+e)/5)

def mediana(a,b,c,d,e): 
    datos = [a,b,c,d,e]
    return (stats.mean(datos))

def promedioMultiplicativo(a,b,c,d,e): 
    m=(a*b*c*d*e)
    return math.sqrt(m)

def ordenAscendente(a,b,c,d,e): 
    lista = [a,b,c,d,e]
    lista.sort()
    return lista

def ordenaDescendente(a,b,c,d,e): 
    listap = [a,b,c,d,e]
    listap.sort(reverse=True)
    return listap
                
def potencia(a,b,c,d,e): 
    listapb = [a,b,c,d,e]
    return(max(listapb)**min(listapb))

def raizCubicaMenor(a,b,c,d,e): 
    listapbp = [a,b,c,d,e]
    return((min(listapbp))**(1/3))

def main():
    continuar=8;
    try:
        while continuar==8:
            print("Ingresa 5 números");
            print("");
            a=float(input("Ingrese el valor del primer "))
            print("");
            b=float(input("Ingrese el valor del segundo "))
            print("");
            c=float(input("Ingrese el valor del tercer "))
            print("");
            d=float(input("Ingrese el valor del cuarto "))
            print("");
            e=float(input("Ingrese el valor del quinto "))
            print("");
            print("El promedio de los 5 números es",promedio(a,b,c,d,e));
            print("");
            print("La mediana de los 5 números es",mediana(a,b,c,d,e));
            print("");
            print("El promedio multiplicativo de los 5 números es",promedioMultiplicativo(a,b,c,d,e));
            print("");
            print("Ordenados de menor a mayor, son",ordenAscendente(a,b,c,d,e));
            print("");
            print("Ordenados de mayor a menor, son",ordenaDescendente(a,b,c,d,e));
            print("");
            print("La potencia del mayor número elevado al menor número es",potencia(a,b,c,d,e));
            print("");
            print("La raíz cúbica del menor número es",raizCubicaMenor(a,b,c,d,e));
            print("");
            continuar=int(input("¿Desea volver a hacerlo con otros 5 números? 8 = SI, 9 = NO "))
            print("");
            print("");
    except:
        print("Error en los datos ingresados");

main() 
