import csv
import sys
from dataclasses import dataclass
from datetime import date

@dataclass
class Poblacion():
   
    
    sector_id: int
    sector_nombre: str 
    variable_id: int 
    actividad_producto_nombre:str 
    indicador:str 
    unidad_de_medida:str 
    fuente: str 
    frecuencia_nombre: str 
    cobertura_nombre:str 
    alcance_tipo: str 
    alcance_id:str 
    alcance_nombre: str 
    indice_tiempo:date
    valor: float
    
def getLectura()->list[Poblacion]:
    """se obtiene una lista de objetos, con toda la informacion necesaria de Poblacion"""

    lista_provinciales = []

    with open('indicadores-provinciales.csv', "r") as f:
        data = csv.reader(f)
            
        for i in list(data)[1:]:
           objeto1 = Poblacion(sector_id = i[0], sector_nombre = i[1],variable_id = i[2], actividad_producto_nombre = i[3],indicador = i[4], unidad_de_medida= i[5], fuente = i[6], frecuencia_nombre = i[7],cobertura_nombre = i[8],alcance_tipo = i[9], alcance_id = i[10],alcance_nombre = i[11],indice_tiempo= date.fromisoformat(i[12]), valor= i[13])
           lista_provinciales.append(objeto1) 
           
    return lista_provinciales
#---------------------------------------------------------------------------#

def fecha (fecha: date, fecha_2: date):
    """se genera una nueva lista con los datos del PBG y sus fechas y se imprimen"""
    lista_fecha =[]
    for objetos1 in getLectura():
        
        if (fecha < objetos1.indice_tiempo < fecha_2 and 'PBG' in objetos1.actividad_producto_nombre):
            lista_fecha.append(objetos1)
            print(lista_fecha)
#----------------------------------------------------------------------------#
fecha1= date.fromisoformat(sys.argv )
fecha2= date.fromisoformat(sys.argv)
fecha(fecha1, fecha2)


