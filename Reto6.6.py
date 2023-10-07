def calcularContagios(contagiadosActuales: int, diasTranscurridos: int) -> int:
  return contagiadosActuales * (2 ** diasTranscurridos)

if __name__ == '__main__':
  contagiadosActuales = int(input("Ingrese el número de contagiados actuales: "))
  diasTranscurridos = int(input("Ingrese el número de días transcurridos a partir de hoy: "))
  totalContagios = calcularContagios(contagiadosActuales, diasTranscurridos)
  print(f"El número total de personas contagiadas después de {diasTranscurridos} días es: {totalContagios}")
