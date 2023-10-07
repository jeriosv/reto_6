# Reto No. 6
Ejercicios sobre manejo de funciones

Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. 

1. Dado la figura de la imagen, desarrolle:
![image](https://github.com/jeriosv/reto_6/assets/142249529/f5418875-8173-4f23-a42b-04087954dd4a)
 
   - Una función matemática para calcular el volumen y el área superficial.
   - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
   - Revise como utilizar el valor de pi usando import math y math.pi
  
   ```python

   import math

   def calcularVolumen(radioEsfera:float, radioCono:float, alturaCono:float) -> float:
      volumenEsfera = (4/3) * (radioEsfera**3) * math.pi
      volumenCono = (alturaCono/3) * (radioCono**2) * math.pi
      return volumenEsfera + volumenCono    

   def calcularArea(radioEsfera:float, radioCono:float, alturaCono:float) -> float:
      areaEsfera = 4 * math.pi * radioEsfera**2
      alturaOblicua = math.sqrt(alturaCono*2 + radioCono*2)
      areaCono = (math.pi * radioCono * alturaOblicua) + (math.pi * radioCono**2)
      return areaEsfera + areaCono

   if __name__ == '__main__':
      radioEsfera = float(input("Ingrese el radio de la esfera en cm: "))
      radioCono = float(input("Ingrese el radio del cono en cm: "))
      alturaCono = float(input("Ingrese la altura del cono en cm: "))
      volumen = calcularVolumen(radioEsfera, radioCono, alturaCono)
      area = calcularArea(radioEsfera, radioCono, alturaCono)
    
      print("El volumen de la figura es: " + str(volumen) + " cm^3")
      print("El área de la figura es: " + str(area) + " cm^2")

   ```

2. Dado la figura de la imagen, desarrolle:
![image](https://github.com/jeriosv/reto_6/assets/142249529/7d67351e-e091-4f29-9308-afe5aae20b16)

   - Una función matemática para calcular el área y el perimetro.
     
   - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
     
   - Revise como utilizar el valor de pi usando import math y math.pi
     ```python
     import math

     def perimetro(r:float, a:float, b:float) -> float:
       rectangulo = 2 * b + 2 * a
       circulo = 2 * math.pi * r
       return rectangulo + 2 * circulo

     def area(r:float, a:float, b:float) -> float:
       rectangulo = a * b
       circulo = math.pi * r**2
       return rectangulo + 2 * circulo

     if _name_ == '_main_':
       r = float(input("Ingrese el valor del radio (en cm): "))
       a = float(input("Ingrese la altura del rectángulo (en cm): "))
       b = float(input("Ingrese la longitud del rectángulo (en cm): "))
       per = perimetro(r, a, b)
       ar = area(r, a, b)
    
     print("El perímetro de la figura es: " + str(per) + " cm.")
     print("El área de la figura es: " + str(ar) + " cm².")
     ```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
   
    ```python
    
    def calcularCantidadCarneAves():
      pesoGallinas = nGallinas * 6
      pesoGallos = mGallos * 7
      pesoPollitos = kPollitos * 1
      pesoTotal = pesoGallinas + pesoGallos + pesoPollitos
      return pesoTotal

    if __name__ == '__main__':
      nGallinas = int(input("Ingrese el número de gallinas: "))
      mGallos = int(input("Ingrese el número de gallos: "))
      kPollitos = int(input("Ingrese el número de pollitos: "))
      cantidadCarne = calcularCantidadCarneAves()
    
    print("La cantidad de carne de aves es:", cantidadCarne, "kilos")
     ```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
   
    ```python
    def calcularVueltas(cantidadPanes, cantidadLeche, cantidadHuevos, montoPagado)-> int:

      totalCompra = ((cantidadPanes * 300) + (cantidadLeche * 3300) + (cantidadHuevos * 350))

      vueltas = montoPagado - totalCompra

      if vueltas < 0:
        return abs(vueltas)
      else:
        return vueltas

    if __name__ == '__main__':
      cantidadPanes = int(input("Ingresa el número de panes a comprar: "))
      cantidadLeche = int(input("Ingresa el número de bolsas de leche a comprar: "))
      cantidadHuevos = int(input("Ingresa el número de huevos a comprar: "))
      montoPagado = int(input("Ingresa el monto que pagará: "))

    vueltas = calcularVueltas(cantidadPanes, cantidadLeche, cantidadHuevos, montoPagado)
    
    if vueltas == 0:
        print("No hay vueltas.")
    elif vueltas < 0:
        print("Lo siento, debe pagar un adicional de:", vueltas)
    else:
        print("Sus vueltas son:", vueltas)
     ```

5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
   
    ```python
    def calcularValorPrestamo(prestamo: float, tasaIinteres: float, meses: int) -> float:
      interes = tasaInteres * prestamo / 100
      return prestamo + meses * interes

    if __name__ == '__main__':
      prestamo = float(input("Ingrese el valor del préstamo en pesos: "))
      tasaInteres = float(input("Ingrese la tasa de interés en porcentaje: "))
      meses = int(input("Ingrese el número de meses para el préstamo: "))
      valorPrestamo = calcularValorPrestamo(prestamo, tasaInteres, meses)
    
    print("El valor a pagar es de: " + str(valorPrestamo))

     ```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

     ```python
     def calcularContagios(contagiadosActuales: int, diasTranscurridos: int) -> int:
       return contagiadosActuales * (2 ** diasTranscurridos)

     if __name__ == '__main__':
       contagiadosActuales = int(input("Ingrese el número de contagiados actuales: "))
       diasTranscurridos = int(input("Ingrese el número de días transcurridos a partir de hoy: "))
       totalContagios = calcularContagios(contagiadosActuales, diasTranscurridos)
       print(f"El número total de personas contagiadas después de {diasTranscurridos} días es: {totalContagios}")

     ```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

   - El promedio
   - La mediana
   - El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
   - Ordenar los números de forma ascendente
   - Ordenar los números de forma descendente
   - La potencia del mayor número elevado al menor número
   - La raíz cúbica del menor número
  
```python
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
      
```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```python
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
    
```

9. Consultar qué es y cómo funciona pip en python.

  PIP es el administrador de paquetes Python. Se puede utilizar para instalar, actualizar y eliminar paquetes escritos en el lenguaje de programación Python.
  El nombre es un acrónimo recursivo que se puede interpretar como Pip Instalador de Paquetes o Pip Instalador Python. Este es un sistema de gestión de paquetes 
  sencillo utilizado para la instalación y administración de paquetes que pueden ser encontrados en el Python Package Index (PyPi)

10. Hacer un listado de módulos populares para python que se puedan instalar como pip y consultar cómo instalarlos.

    Uno de los módulos más populares para python son:
     - TensorFlow
     - Scikit-Learn
     - Numpy
     - Keras
     - PyTorch
     - LightGBM
     - Eli5
     - SciPy
     - Theano
     - Pandas
    
    Y algunos módulos que vienen "built-in" dentro del instalador de python son:
     - math
     - collections
     - datetime
     - random
     - sys
     - logging
     - time
     - os
    
    Para instalar un paquete desde PyPI utiliza:
      pip install paquete
     En donde paquete es el nombre de un módulo, librería, script o framework que se encuentre en https://pypi.python.org/pypi.
     Por ejemplo en windows:
      > C:\PythonXY\scripts\pip install django

     pip es un módulo de Python, por lo que si no se encuentra en la carpeta scripts también puede utilizarse:

      > C:\PythonXY\python -m pip install django


