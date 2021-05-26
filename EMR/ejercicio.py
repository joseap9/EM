# recibe dos strings del mismo largo
# y retorna un string con los caracteres "no borrados"
def calcular_data_vigente(data, info):
  data_vigente = ""
  for i in range(len(data)):
    if info[i]== "O":
      data_vigente = data_vigente + data[i]
  return data_vigente

#retorna True cuando palabra aparece en data en la posicion dada
#retorna False cuando palabra no aparece en data en la posicion dada
def existe_palabra(palabra,data,posicion):
  if len(data)-posicion < len(palabra):
    return False

  for i in range(0,len(palabra)-1):
    if palabra[i] != data[posicion+i]:
     return False
  return True

def buscar_palabra(palabra,data):
  for i in range(0,len(data)-len(palabra)):
    existe_palabra_2=existe_palabra(palabra,data,i)
    if existe_palabra_2 == True:
      return i
  return -1 

data_ingresada = input("ingrese letras en mayúscula: ")
info_ingresada = input("dada a la posición de cada elemento, ingrese (X) si quiere borrar el elemento o (O) si quiere conservarlo: ")
palabra_ingresada = input("ingrese una palabra cualquiera en mayúscula: ")

data_guardada=calcular_data_vigente(data_ingresada,info_ingresada)
#print(data_guardada)

posicion=buscar_palabra(palabra_ingresada,data_guardada)
print(posicion)