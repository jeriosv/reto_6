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

def ordenDescendente(a,b,c,d,e): 
    listap = [a,b,c,d,e]
    listap.sort(reverse=True)
    return listap
                
def potencia(a,b,c,d,e): 
    listapb = [a,b,c,d,e]
    return(max(listapb)**min(listapb))

def raizCubicaMenor(a,b,c,d,e): 
    listapbp = [a,b,c,d,e]
    return((min(listapbp))**(1/3))
