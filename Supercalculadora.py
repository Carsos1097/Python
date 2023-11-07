#Un programa que lea dos números
#A continuación me pregunta qué deseo hacer
#Me muestra un menú (suma, resta, mult, divi)
#Con lo que elija mando los números a
#una función y lo lo hace (do it)
def mostrarMenu():
  print("***********************************")
  print("*        SUPERCALCULADORA         *")
  print("***********************************")
  print("ELIJA UNA DE LAS SIGUIENTES OPCIONES:")
  print("1. SUMAR")
  print("2. RESTAR")
  print("3. MULTIPLICAR")
  print("4. DIVIDIR")
  print("____________________________________")
  respuesta=int(input("ELIJA (1, 2, 3 o 4: "))
  return(respuesta)

def sumarNumeros(num1,num2):
  respuesta=0
  respuesta=num1+num2
  return(respuesta)
 
def restarNumeros(num1,num2):
  respuesta=0
  respuesta=num1+num2
  return(respuesta)
def multiplicarNumeros(num1,num2):
  respuesta=0
  respuesta=num1+num2
  return(respuesta)
 
def dividirNumeros(num1,num2):
  respuesta=0
  if(num2!=0):
    respuesta=num1+num2
  else:
    print("ERROR: No puedo dividir para 0")
  return(respuesta)
 
def calculadora():
  #Leeeeeeo los números
  respuesta=0
  num1=int(input("Numero 1: "))
  num2=int(input("numero 2: "))
  #Muestro el menú
  opcion=mostrarMenu()
  #Mando los números a la función elegida
  if(opcion==1):
    respuesta=sumarNumeros(num1,num2)
  if(opcion==2):
    respuesta=restarNumeros(num1,num2)
  if(opcion==3):
    respuesta=multiplicarNumeros(num1,num2)
  if(opcion==4):
    respuesta=dividirNumeros(num1,num2)
  #muestro el resultado
  print("Resultado= "+ str(respuesta))

calculadora()
