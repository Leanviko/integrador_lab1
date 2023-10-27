from data_stark import lista_personajes

#punto A
def lista_nombres(lista_personajes):
    for i in range(len(lista_personajes)):
        print(lista_personajes[i]["nombre"])

#punto B
def lista_nombres_altura(lista_personajes):
    for i in range(len(lista_personajes)):
        print(f"{lista_personajes[i]['nombre']}. Altura: {lista_personajes[i]['altura']}")


#punto C
def altura_maxima(lista_personajes):
    alt_max = 0
    posicion_altura_maxima = 0
    for i in range(len(lista_personajes)):

        if float(lista_personajes[i]['altura']) > alt_max:
            alt_max = float(lista_personajes[i]['altura'])
            posicion_altura_maxima= i

    return posicion_altura_maxima

#punto D
def altura_minima(lista_personajes):
    alt_min = None
    posicion_altura_minima = 0
    for i in range(len(lista_personajes)):
        if i == 0:
            
            alt_min = float(lista_personajes[i]['altura'])
            posicion_altura_minima = i
        elif float(lista_personajes[i]['altura']) < alt_min:
            alt_min = float(lista_personajes[i]['altura'])
            posicion_altura_minima = i
    return posicion_altura_minima

#punto D
def promedio_altura(lista_personajes):
    alt_suma = 0
    cant_super = 0
    for i in range(len(lista_personajes)):
        alt_suma += float(lista_personajes[i]['altura'])
        cant_super += 1
    if cant_super > 0:
        promedio_alt = alt_suma/cant_super
        print(f"Suma: {alt_suma}, Cantidad registros: {cant_super}, Promedio: {promedio_alt}")
    else:
        print("No hay registros")

#punto G
#
#

#punto H
def mas_pesado(lista_personajes):
    peso_max = 0
    posicion_peso_maximo = 0
    for i in range(len(lista_personajes)):
        if float(lista_personajes[i]['peso']) > peso_max:
            peso_max = float(lista_personajes[i]['altura'])
            posicion_peso_maximo= i
    return posicion_peso_maximo



def menos_pesado(lista_personajes):
    peso_min = None
    posicion_peso_minimo = 0
    for i in range(len(lista_personajes)):
        if i == 0: 
            peso_min = float(lista_personajes[i]['peso'])
            posicion_peso_min = i
        elif float(lista_personajes[i]['peso']) < peso_min:
            alt_min = float(lista_personajes[i]['peso'])
            posicion_peso_min = i
    return posicion_peso_minimo



while True:
    print("Base de datos Stark.\n")
    print("1- Nombres de pila.")
    print("2- Nombres y altura.")
    print("3- Altura Maxima.")
    print("4- Altura Minima.")
    print("5- Promedio de todas las alturas.")
    print("6- Superheroe más alto.")
    print("7- Superheroe más bajo.")
    print("8- Superheroe más pesado.")
    print("9- Superheroe más liviano.")
    
    opcion = int(input("Ingrese un valor: "))
    if opcion<=9 and opcion>=0:
        break

print("\n")
match opcion:
    case 1:
        lista_nombres(lista_personajes)
    case 2:
        lista_nombres_altura(lista_personajes)
    case 3:
        posicion_max = altura_maxima(lista_personajes)
        MAXIMO = lista_personajes[posicion_max]['altura']
        print(f"Altura máxima: {MAXIMO}")
    case 4:
        posicion_min = altura_minima(lista_personajes)
        MINIMO = lista_personajes[posicion_min]['altura']
        print(f"Altura minima: {MINIMO}")
    case 5:
        promedio_altura(lista_personajes)
    case 6:
        posicion_max = altura_maxima(lista_personajes)
        NOMBRE_MAXIMO = lista_personajes[posicion_max]['nombre']
        print(f"Nombre superheroe con altura maxima: {NOMBRE_MAXIMO}")
    case 7:
        posicion_min = altura_minima(lista_personajes)
        NOMBRE_MINIMO = lista_personajes[posicion_min]['nombre']
        print(f"Nombre superheroe con altura minima: {NOMBRE_MINIMO}")
    case 8:
        pos_pesado = mas_pesado(lista_personajes)
        print(f"El más pesado es {lista_personajes[pos_pesado]['nombre']} con un peso de {lista_personajes[pos_pesado]['peso']}")
    case 9:
        pos_liviano = menos_pesado(lista_personajes)
        print(f"El más liviano es {lista_personajes[pos_liviano]['nombre']} con un peso de {lista_personajes[pos_liviano]['peso']}")


    
