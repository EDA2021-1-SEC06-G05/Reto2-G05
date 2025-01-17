﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import time
from DISClib.ADT import map as map
from DISClib.ADT import list as lt
from datetime import datetime
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#pruebaaaaa2
#hola
def printMenu():
    print("Bienvenido")
    print("1- Seleccionar el tipo de representación de la lista")
    print("2- Seleccione el tipo de algoritmo de ordenamiento iterativo")  
    print("3- Consultar el TOP n de tendencias por categoria y pais")
    print("4- Seleccionar el tipo de representación de la lista")
    print("5- Consultar el TOP n de tendencias por categoria y pais")
    print("0- Salir")

def initCatalog(parametro, tipoEstructuraMap, factorDeCarga):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(parametro, tipoEstructuraMap, factorDeCarga)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    return controller.loadData(catalog)

def printCategoryData(category):
    if category:
        print('categoria encontrada:' + category['name'])
        print('Reproducciones' + str(category['views']))
        print('Total de videos:' + str(lt.size(category['videos'])))
        for videos in lt.iterator(category['videos']):
            print('Titulo:' + video['title'] + 'Nombre del canal:' + video['channel_title'])
        else:
            print('No se encontro la categoria')

def printBestVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos:')
        for video in lt.iterator(videos):
            print('Titulo:' + video['title'] + 'Fecha de tendencia:' + video['trending_date'] + 
                  'Nombre del canal:' + video['channel_title'] + 'Fecha de publicacion:' + 
                  video['publish_time'] + 'Reproducciones:' + video['views'] + 'Likes:' + 
                  video['likes'] + 'Dislikes:' + video['dislikes'] )
    else:
        print('No se encontraron videos')        

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        MedirTiempo1 = time.process_time()
        size = input('(1) para ARRAY_LIST, (2) para LINKED_LIST, (3) para CHAINING o (4) para PROBING\n : ')
        if int(size[0])==1:
            print("Cargando información de los archivos en ARRAY_LIST....")
            catalog = initCatalog("ARRAY_LIST")
            loadData(catalog)
            print('Videos cargados:' + str(lt.size(catalog['videos'])))
            print('Categorias cargadas' + str(lt.size(catalog['category'])))
            print('views cargadas' + str(lt.size(catalog['views'])))
            MedirTiempo2 = time.process_time()
        elif int(size[0])==2:    
            print("Cargando informacion de los archivos en LINKED_LIST")
            catalog = initCatalog("LINKED_LIST")
            loadData(catalog)
            print('Videos cargados:' + str(lt.size(catalog['videos'])))
            print('Categorias cargadas' + str(lt.size(catalog['category'])))
            print('views cargadas' + str(lt.size(catalog['views'])))
            MedirTiempo2 = time.process_time()


        elif int(size[0])==3:
            print("Cargando informacion de los archivos para CHAINING")
            factorCarga = input("Digite factor de carga \n :")
            catalog = initCatalog("ARRAY_LIST", "CHAINING", int(factorCarga))
            answer = loadData(catalog)
            print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")


        elif int(size[0])==4:   
            print("Cargando informacion de los archivos para PROBING") 
            factorCarga = input("Digite factor de carga \n :")
            catalog = initCatalog("ARRAY_LIST", "PROBING", float(factorCarga))
            answer = loadData(catalog)
            print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ", "Memoria [kB]: ", f"{answer[1]:.3f}")



    elif int(inputs[0]) == 2:
        size = input('(1) para selection, (2) para insertion, (3) para shell, (4) para merge y (5) para quick\n : ')
        pre = input("Cantidad de la muestra : ")
        if int(size[0])==1:
            instanteInicial = datetime.now()
            print("Ordenando por Selection")
            result = controller.selectionVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.seconds
            print("El tiempo en segundoss es :")
            print(segundos)
        elif int(size[0])==2:
            instanteInicial = datetime.now()
            print("Ordenando por Insertion")
            result = controller.insertionVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.seconds
            print("El tiempo en segundos es :")
            print(segundos)
        elif int(size[0])==3:
            instanteInicial = datetime.now()
            print("Ordenando por shell")  
            result = controller.shellVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.seconds
            print("El tiempo en segundos es :")
            print(segundos)
        elif int(size[0])==4:
            instanteInicial = datetime.now()
            print("Ordenando por merge")  
            result = controller.mergeVideos(catalog)
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.seconds
            print("El tiempo en segundos es :")
            print(segundos)  
        elif int(size[0])==5:
            instanteInicial = datetime.now()
            print("Ordenando por quick")  
            result = controller.quickVideos(catalog)  
            muestra = controller.crearSubLista(catalog, int(pre))
            print(muestra)
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial
            segundos = tiempo.seconds
            print("El tiempo en segundos es :")
            print(segundos)     


    elif int(inputs[0]) == 3:
        A = input("nombre de la categoria\n : ")
        B = input("Pais\n : ")
        C = input("numero de videos\n : ")

        lista = controller.requerimiento1(catalog, A, B, C)
        for i in range (1, lt.size(lista)+1):
            elemento = lt.getElement(lista, i)
            print(elemento["trending_date"])
            print(elemento["title"])
            print(elemento["channel_title"])
            print(elemento["publish_time"])
            print(elemento["views"])
            print(elemento["likes"])
            print(elemento["dislikes"])
            


    elif int(inputs[0]) == 4:
        number = input("Buscando los TOP ?:")
        videos = controller.getBestVideos(catalog, int(number))
        printBestVideos(videos)
    else:
        sys.exit(0)
sys.exit(0)
