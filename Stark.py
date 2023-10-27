from os import system
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



def nombres_genero(lista_personajes, genero):
    nombres_genero=[]
    for i in range(len(lista_personajes)):
        if lista_personajes[i]['genero'] == genero:
            nombres_genero.append(lista_personajes[i]['nombre'])
    
    for i in range(len(nombres_genero)):
        print(nombres_genero[i])

def max_altura_genero(lista_personajes, genero):
    altura_genero=[]
    personaje={}
    for i in range(len(lista_personajes)):
        if lista_personajes[i]['genero'] == genero:
            personaje= {'nombre': lista_personajes[i]['nombre'],'altura': lista_personajes[i]['altura']}
            altura_genero.append(personaje)
    
    #for i in range(len(altura_genero)):
    #    print(f"Nombre: {altura_genero[i]['nombre']}, Altura: {altura_genero[i]['altura']}")
    
    posicion_max = altura_maxima(altura_genero)
    print(f"Superheroe de genero {genero} con mayor altura {altura_genero[posicion_max]['nombre']} con altura {altura_genero[posicion_max]['altura']}")


def min_altura_genero(lista_personajes, genero):
    altura_genero=[]
    personaje={}
    for i in range(len(lista_personajes)):
        if lista_personajes[i]['genero'] == genero:
            personaje= {'nombre': lista_personajes[i]['nombre'],'altura': lista_personajes[i]['altura']}
            altura_genero.append(personaje)
    
    #for i in range(len(altura_genero)):
    #    print(f"Nombre: {altura_genero[i]['nombre']}, Altura: {altura_genero[i]['altura']}")
    
    posicion_min = altura_minima(altura_genero)
    print(f"Superheroe de genero {genero} con mayor altura {altura_genero[posicion_min]['nombre']} con altura {altura_genero[posicion_min]['altura']}")

def promedio_por_genero(lista_personajes, genero):
    altura_genero=[]
    personaje={}
    promedio = 0

    for i in range(len(lista_personajes)):
        if lista_personajes[i]['genero'] == genero:
            personaje= {'nombre': lista_personajes[i]['nombre'],'altura': lista_personajes[i]['altura']}
            altura_genero.append(personaje)

    cant_personajes = len(altura_genero)
    suma_alturas = 0

    for i in range(cant_personajes):
        suma_alturas += float(altura_genero[i]['altura'])
        promedio = suma_alturas/cant_personajes

    return promedio

def lista_colores_de_ojos(lista_personajes):
    lista_colores_ojos = []
    existe_color = None
    color_ojo ={}
    
    for i in range(len(lista_personajes)):
            color = lista_personajes[i]['color_ojos']
            
            if i > 0:
                for j in range(len(lista_colores_ojos)):
                    existe_color = False
                    if color.lower() == lista_colores_ojos[j]['color_ojos'].lower():
                        existe_color = True
                        break
            
            if (existe_color == False) or (i == 0):
                color_ojo = {'color_ojos': color, 'cantidad' : 1}
                lista_colores_ojos.append(color_ojo)
            else:
                for k in range(len(lista_colores_ojos)):
                    if lista_colores_ojos[k]['color_ojos'].lower() == color.lower():
                        lista_colores_ojos[k]['cantidad'] += 1
                        break

    return lista_colores_ojos


def lista_colores_de_pelo(lista_personajes):
    lista_colores_pelo = []
    existe_color = None
    color_pelo ={}
    
    for i in range(len(lista_personajes)):
            
            color = lista_personajes[i]['color_pelo']
            
            if i > 0:
                for j in range(len(lista_colores_pelo)):
                    existe_color = False
                    if color.lower() == lista_colores_pelo[j]['color_pelo'].lower():
                        existe_color = True
                        break
            
            if (existe_color == False) or (i == 0):
                color_ojo = {'color_pelo': color, 'cantidad' : 1}
                lista_colores_pelo.append(color_ojo)
            else:
                for k in range(len(lista_colores_pelo)):
                    if lista_colores_pelo[k]['color_pelo'].lower() == color.lower():
                        lista_colores_pelo[k]['cantidad'] += 1
                        break

    return lista_colores_pelo 
    
    


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
    print("10- Nombres con genero 'M'.")
    print("11- Nombres con genero 'F'.")
    print("12- Superheroe de genero Masculino con mayor altura.")
    print("13- Superheroe de genero Femenino con mayor altura.")
    print("14- Superheroe de genero Masculino con menor altura.")
    print("15- Superheroe de genero Femenino con menor altura.")
    print("16- Altura promedio de genero Masculino.")
    print("17- Altura promedio de genero Femenino.")
    print("18- Colores de ojos")
    print("19- Colores de pelo")
    
    opcion = int(input("Ingrese un valor: "))
    #if opcion<=50 and opcion>=0:
        #break

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
        case 10:
            nombres_genero(lista_personajes, 'M')
        case 11:
            nombres_genero(lista_personajes, 'F')
        case 12:
            max_altura_genero(lista_personajes, 'M')
        case 13:
            max_altura_genero(lista_personajes, 'F')
        case 14:
            min_altura_genero(lista_personajes, 'M')
        case 15:
            min_altura_genero(lista_personajes, 'F')
        case 16:
            promedio = promedio_por_genero(lista_personajes,'M')
            print(f"Altura promedio masculino {promedio}")
        case 17:
            promedio = promedio_por_genero(lista_personajes,'F')
            print(f"Altura promedio femenino {promedio}")
        case 18:
            lista_col = lista_colores_de_ojos(lista_personajes)

            for i in range(len(lista_col)):
                print(lista_col[i])
        case 19:
            lista_col_pelo = lista_colores_de_pelo(lista_personajes)
            
            for i in range(len(lista_col_pelo)):
                print(lista_col_pelo[i])

        
    opcion = input("\nOtra opcion? S/N:  ")
    if opcion != 'S' and opcion != 's':
        break
    else:
        system('cls')

    
