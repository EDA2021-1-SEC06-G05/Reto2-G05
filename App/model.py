"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
# Construccion de modelos

def newCatalog(tipoEstructura, tipoEstructuraMap, factorDeCarga):

    catalog= {'videos': None, "views": None, "category": None}
    #catalog["map"] = mp.newMap(numelements=17, maptype=tipoEstructuraMap, loadfactor= factorDeCarga, comparefunction=None)
    catalog['videos'] = lt.newList(datastructure=tipoEstructura)
    #catalog['category'] = lt.newList(datastructure=tipoEstructura, cmpfunction= compareMapVideosCate)
    catalog["views"] = lt.newList(datastructure= tipoEstructura, cmpfunction= cmpVideosByViews)

    #catalog['category'] = mp.newMap(33, maptype= tipoEstructuraMap, loadfactor= factorDeCarga, comparefunction=compareMapVideosCate)
    catalog['category'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapVideosCate)

    catalog["videos"] = mp.newMap(1000, maptype = tipoEstructuraMap, loadfactor = factorDeCarga, comparefunction = compareMapVideosCate)                               
    return catalog
    
# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):

    lt.addLast(catalog['videos'], video)
    lt.addLast(catalog["views"],video)    

def addCategory(catalog, categoria):

    categorias = catalog["category"] 
    lt.addLast(categorias, categoria) 
    mp.put(catalog['category'], categoria['id'], categoria)


# Funciones para creacion de datos

def newCategory(name):

    category = {'name': "", "videos": None, "views": 0}
    category['name'] = name
    category['videos'] = lt.newList('ARRAY_LIST')
    return category

# Funciones de consulta
def crearSubLista(catalog, muestra):
    nuevaLista = lt.subList(catalog["videos"], 1, muestra)

    return nuevaLista








def getVideosByCategory(catalog, categoria):

    poscategory = lt.isPresent(catalog['categorias'], categoria)
    if poscategory > 0:
        category = lt.getElement(catalog['categorias'], poscategory)
        return category
    return None

def getBestVideos(catalog, number):

    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos

# Funciones utilizadas para comparar elementos dentro de una lista

def compareviews(video1, video2):
    return (float(video1['views']) > float(video2['views']))

def comparecategory(categoria1, category):

    if(categoria1.lower() in category['name'].lower()):
        return 0
    return -1
def cmpVideosByViews(video1, video2):
    
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    views1 = False
    print(float(video2['views']), float(video1['views']))
    if (float(video2['views'])) > (float(video1['views'])):
        print("1")
        views1 = True
    return views1   

# Funciones de ordenamiento

def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        return lt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')

def sortVideos(catalog):
    sa.sort(catalog['videos'], compareviews)

def selectionVideos(catalog):
    sel.sort(catalog['videos'], compareviews)
    
def insertionVideos(catalog):    
    ins.sort(catalog["videos"], compareviews)

def shellVideos(catalog):
    shell.sort(catalog["videos"],compareviews)

def quickVideos(catalog):
    quick.sort(catalog["videos"],compareviews)

def mergeVideos(catalog):
    merge.sort(catalog["videos"], compareviews)    


def compareMapVideosCate(id, entry):
  
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
