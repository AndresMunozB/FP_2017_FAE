
#ENTRADA:string con el nombre del archivo
#SALIDA: lista de listas que contiene en cada sublista una linea del archivo
def archivo_lista(nombre_archivo):
    archivo = open(nombre_archivo,"r")
    lista=[]
    for linea in archivo:
        lista_linea = linea.strip().split(",")
        lista.append(lista_linea)
    archivo.close()
    return lista

def mostrar_lista(lista):
    for e in lista:
        print e

#ENTRADA:lista que contiene la informacion del archivo "listado"
#SALIDA: una lista que contiene el id de cada animal junto con dos booleanos,
        #el primer booleano  se interpreta para ver si existe existe un animal con ese id de sexo femenino
        #el segundo boobleano se interpreta para ver si existe un animal con ese id de sexo femenino
def crear_lista_estados(lista):
    lista_estados=[]
    for elemento in lista:
        lista_estados.append([elemento[0],False,False])
    return lista_estados

#ENTRADA:lista de estadaos, id del animal, y el sexo puede ser "Macho o Hembra"
#SALIDA: estado de si existe o no el id_animal junto con el sexo entregado
def verificar_estado(lista_estados,id_animal,sexo):
    for i in range(len(lista_estados)):
        if (lista_estados[i][0] == id_animal):
            if (sexo == "Macho"):
                return lista_estados[i][1]
            if (sexo == "Hembra"):
                return lista_estados[i][2]
#ENTRADA: lista de estados, id, sexo
#SALIDA: una lista nueva en el cual se cambia de True el valor del estado de ese id_animal y dependiendo de si es macho o hembra
def cambiar_estado(lista_estados,id_animal,sexo):
    for i in range(len(lista_estados)):
        if(lista_estados[i][0] == id_animal):
            if(sexo == "Macho"):
                lista_estados[i][1] = True
            if(sexo == "Hembra"):
                lista_estados[i][2] = True
    return lista_estados


#ENTRADA: lista que contiene la informacion del archivo "listado", id_animal
#SALIDA: Entrega el nombre especifico del animal que tenga el id = id_animal

def nombre_cientifico(lista_listado,id_animal):
    for i in range(len(lista_listado)):
        if lista_listado[i][0] == id_animal:
            return lista_listado[i][2]

#ENTRADA: recive como parametros de entrega la lista de estado y el id del animal
#SALIDA: Entrega un string con el estado del animal, el string puede tener los valores:OK,FALTA UN MACHO,FALTA UNA HEMBRA,FALTAN AMBOS
def estado(lista_estado,id_animal):
    for i in range(len(lista_estado)):
        if lista_estado[i][0] == id_animal:
            if(lista_estado[i][1] == True and lista_estado[i][2] == True):
                return "OK"
            elif(lista_estado[i][1] == False and lista_estado[i][2] == True):
                return "FALTA UN MACHO"
            elif(lista_estado[i][1] == True and lista_estado[i][2] == False):
                return "FALTA UNA HEMBRA"
            elif(lista_estado[i][1] == False and lista_estado[i][2] == False):
                return "FALTAN AMBOS"


#BLOQUE PRINCIPAL:

 #ENTRADA

str_listado = raw_input( "Ingrese el nombre del archivo listado : ")
str_registro = raw_input("Ingrese el nombre del archivo registro: ")

#listado:ID_ANIMAL,NOMBRE_ANIMAL,NOMBRE_CIENTIFICO
lista_listado = archivo_lista("listado.csv")
#registro:ID_ANIMAL,NOMBRE_ANIMAL,SEXO
lista_registro = archivo_lista("registro1.csv")




#PROCESAMIENTO Y SALIDA DEL PRIMER ARCHIVO (CONDENADOS)
lista_estados = crear_lista_estados(lista_listado)
archivo_condenados = open("condedos.csv","w")
archivo_nuevo_listado = open("nuevoListado.csv","w")
archivo_condenados.write("ID_ANIMAL,NOMBRE_ANIMAL,SEXO,NOMBRE_CIENTIFICO\n")
archivo_nuevo_listado.write("ID_ANIMAL,NOMBRE_ANIMAL,NOMBRE_CIENTIFICO,ESTADO\n")

for i in range(1,len(lista_registro)):
    if (verificar_estado(lista_estados,lista_registro[i][0],lista_registro[i][2])):
        #print "EXISTE (CONDENADO) id: ", lista_registro[i][0] , "sexo:", lista_registro[i][2]
        archivo_condenados.write(lista_registro[i][0]+","+lista_registro[i][1]+","+lista_registro[i][2]+","+nombre_cientifico(lista_listado,lista_registro[i][0])+"\n")

        
    else:
        #print "NO EXISTE (ARCA): id: ", lista_registro[i][0] , "sexo:", lista_registro[i][2]
        lista_estados = cambiar_estado(lista_estados,lista_registro[i][0],lista_registro[i][2])

#SALIDA SEGUNDO ARCHIVO (NUEVO LISTADO)
for i in range(1,len(lista_listado)):
    #print lista_listado[i][0]+","+lista_listado[i][1]+","+lista_listado[i][2]+","+estado(lista_listado[i][0]
    archivo_nuevo_listado.write(lista_listado[i][0]+","+lista_listado[i][1]+","+lista_listado[i][2]+","+estado(lista_estados,lista_listado[i][0])+"\n")

archivo_condenados.close()
archivo_nuevo_listado.close()

print "Programa finalizado correctamente."
