#En este banco, puedes sacar o ingresar dinero como en un banco normal y corriente
import time
print("BIENVENIDO A LISBONA ECONOMICAL SOCIETY, el mejor banco del mundo")
time.sleep(0.5)
dinero=500
cartera=0
while True:
    time.sleep(0.5)
    print("Tienes",dinero,"euros en el banco y",cartera,"en la cartera")
    time.sleep(1)
    preg=input("¿Qué deseas hacer?, SACAR,INGRESAR,SALIR --> ")
    if preg=="SACAR":
        sac=int(input("Cuánto dinero deseas sacar --> "))
        if (sac>dinero):
            print("No puedes sacar más dinero del que posees en tu cuenta")
        else:
            dinero=dinero-sac
            cartera=cartera+sac
    if preg=="INGRESAR":
        ing=int(input("Cuánto dinero deseas ingresar --> "))
        if ing>cartera:
            print("No puedes ingresar más dinero del que llevas encima")
        else:
            dinero=dinero+ing
            cartera=cartera-ing
    if preg=="SALIR":
        break
    if dinero==0:
        print("Te has quedado sin dinero en el banco")
