# Reto No. 6
Ejercicios sobre manejo de funciones

Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. 

1. Dado la figura de la imagen, desarrolle:
![image](https://github.com/jeriosv/reto_6/assets/142249529/f5418875-8173-4f23-a42b-04087954dd4a)
 
   - Una función matemática para calcular el volumen y el área superficial.
   - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
   - Revise como utilizar el valor de pi usando import math y math.pi
  
   ```python
   n : int 
   n = int(input("Ingrese un número entero: ")) # Conversión a entero

   if n == 97 or n == 101 or n == 105 or n == 111 or n == 117:
      print( (n), " sí es una vocal minúscula.")
   else:
      print( (n), " no es una vocal minúscula.")

   print("El número ", (n), " corresponde al código ASCII: ", chr(n))

   ```

2. Dado la figura de la imagen, desarrolle:
![image](https://github.com/jeriosv/reto_6/assets/142249529/7d67351e-e091-4f29-9308-afe5aae20b16)

   - Una función matemática para calcular el área y el perimetro.
     ```python
     ```
   - Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
      ```python
     ```
   - Revise como utilizar el valor de pi usando import math y math.pi
     ```python
     ```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
   
    ```python
     ```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
   
    ```python
     ```

5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
   
    ```python
     ```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

     ```python
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
     ```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

    ```python
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


