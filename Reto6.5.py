def calcularValorPrestamo(prestamo: float, tasaIinteres: float, meses: int) -> float:
  interes = tasaInteres * prestamo / 100
  return prestamo + meses * interes

if __name__ == '__main__':
  prestamo = float(input("Ingrese el valor del préstamo en pesos: "))
  tasaInteres = float(input("Ingrese la tasa de interés en porcentaje: "))
  meses = int(input("Ingrese el número de meses para el préstamo: "))
  valorPrestamo = calcularValorPrestamo(prestamo, tasaInteres, meses)
  print("El valor a pagar es de: " + str(valorPrestamo))
