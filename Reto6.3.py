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
