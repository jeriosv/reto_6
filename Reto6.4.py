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
