menu = """ 
Bienvenido al conversor de monedas 💰

1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Elige una opcion: """

def conversor(tipo_pesos, valor_dolar):
  pesos = float(input('Cuantos pesos ' + tipo_pesos +' tienes?: '))
  dolares = pesos / valor_dolar
  dolares = str(round(dolares, 2))
  print('Tienes $ ' + dolares + ' dolares')

opcion = input(menu)

if opcion == '1':
  valor_dolar = 90.37
  conversor('Argentinos', valor_dolar)
elif opcion == '2':
  valor_dolar = 3635.15
  conversor('Colombianos', valor_dolar)
elif opcion == '3':
  valor_dolar = 21.32
  conversor('Mexicanos', valor_dolar)
else:
  print("Ingresa una opcion correcta por favor")
