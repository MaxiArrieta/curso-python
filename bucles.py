def run():
  print('Potencias de 2 hasta 1000000')
  LIMITE = 1000000
  i = 1
  potencia_2 = 2 ** i
  while potencia_2 < LIMITE:
    print('2 ^ ' + str(i) + ' = ' + str(potencia_2) + '\n')
    i += 1
    potencia_2 = 2 ** i


if __name__ == '__main__':
  run()