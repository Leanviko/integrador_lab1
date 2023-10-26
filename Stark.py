from data_stark import lista_personajes

#punto A

#for i in range(len(lista_personajes)):
#    print(lista_personajes[i]["nombre"])

#punto B
#for i in range(len(lista_personajes)):
#    print(f"{lista_personajes[i]['nombre']}. Altura: {lista_personajes[i]['altura']}")


#punto C
# def altura_maxima(lista_personajes):
#     alt_max = 0
#     posicion_altura_maxima = 0
#     for i in range(len(lista_personajes)):
#         if float(lista_personajes[i]['altura']) > alt_max:
#             alt_max = float(lista_personajes[i]['altura'])
#             posicion_altura_maxima= i
#     return posicion_altura_maxima

# posicion_max = altura_maxima(lista_personajes)
# print(f"Altura minima: {lista_personajes[posicion_max]['altura']}")

#punto D
# def altura_minima(lista_personajes):
#     alt_min = None
#     posicion_altura_minima = 0
#     for i in range(len(lista_personajes)):
#         if i == 0:
            
#             alt_min = float(lista_personajes[i]['altura'])
#             posicion_altura_minima = i
#         elif float(lista_personajes[i]['altura']) < alt_min:
#             alt_min = float(lista_personajes[i]['altura'])
#             posicion_altura_minima = i
#     return posicion_altura_minima

# posicion_min = altura_minima(lista_personajes)
# print(f"Altura minima: {lista_personajes[posicion_min]['altura']}")


#punto D
#alt_suma = 0
#cant_super = 0
#for i in range(len(lista_personajes)):
#    alt_suma += float(lista_personajes[i]['altura'])
#    cant_super += 1
#if cant_super > 0:
#    promedio_alt = alt_suma/cant_super
#    print(f"Suma: {alt_suma}, Cantidad registros: {cant_super}, Promedio: {promedio_alt}")
#else:
#    print("No hay registros")

#punto G
#print(f"Nombre superheroe con altura maxima: {lista_personajes[posicion_max]['nombre']}")
#print(f"Nombre superheroe con altura minima: {lista_personajes[posicion_min]['nombre']}")


#punto H
def mas_pesado(lista_personajes):
    peso_max = 0
    posicion_peso_maximo = 0
    for i in range(len(lista_personajes)):
        if float(lista_personajes[i]['peso']) > peso_max:
            peso_max = float(lista_personajes[i]['altura'])
            posicion_peso_maximo= i
    return posicion_peso_maximo

pos_pesado = mas_pesado(lista_personajes)
print(f"Peso maximo: {lista_personajes[pos_pesado]['peso']}")

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

pos_liviano = menos_pesado(lista_personajes)
print(f"Peso minimo: {lista_personajes[pos_liviano]['peso']}")
