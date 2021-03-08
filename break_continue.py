def run() :
  # Ejemplo de uso del continue
  # for contador in range(100):
  #   if contador % 2 != 0:
  #     continue
  #   print(contador)

  # Ejemplo de uso del brack
  # for i in range(10000):
  #   print(i)
  #   if i == 5455:
  #     break

  texto = input('Escribe un texto: ')
  for letra in texto:
    if letra == 'o':
      break
    print(letra)

if __name__ == '__main__':
  run()