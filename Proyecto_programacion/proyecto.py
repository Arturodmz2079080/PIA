from os import system,name

def limpiar():
    if name == "nt":
        system("cls")
    else:
        system("clear")
def registrador():
    contador=1
    limpiar()
    while True:
        try:
            print("que desea hacer")
            print("[1]:Registrar una venta")
            print("[2]:Salir")
            menu=input("Opcion:")
            lista_mult=[]
            if menu == "1":
                ciclo=1
                while ciclo == 1:
                    limpiar()
                    while True:
                        v_descripcion= input(f" Descripcion del producto {contador}: ")
                        if v_descripcion == "":
                            print("La descripción esta vacia, por favor ingrese una descripción valida")
                        else:
                            break
                    while True:
                        v_cantidad= int(input("¿Cuantas piezas se vendieron?: "))
                        if v_cantidad < 0:
                            print("La cantidad proporcionada no puede ser negativa por favor, ingresa una cantidad con valor positivo.")
                        elif v_cantidad > 0:
                            break
                    while True:
                        v_precio=float(input("¿Cual es el precio del producto?: "))
                        if v_precio < 0:
                            print("La cantidad proporcionada no puede ser negativa por favor, ingresa un precio con valor positivo.")
                        elif v_precio > 0:
                            break
                    lista_mult.append(v_cantidad * v_precio)
                    contador+=1
                    print("")
                    print("¿Que deseas hacer?")
                    print("[1]: seguir registrando ventas")
                    print("[0]: salir del registrador de ventas")
                    ciclo=int(input("Opcion:"))
                    limpiar()
                a=sum(lista_mult)
                print("PROCESO REALIZADO")
                print(f"El monto total es de {a} pesos")
            elif menu == "2":
                limpiar()
                break
            else:
                print(f"La opción {menu} no es válida")
        except:
            print(f"Ocurrió un problema")
    print("Hasta luego")


print("proyecto integrador de aprendizaje")
registrador()







