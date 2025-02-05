################################
#CREADOR DE HISTOGRAMAS NORMALES
################################

#Carga de librerias
import numpy as np 
import pandas as pd 
import argparse

#Crear un Parser
parser = argparse.ArgumentParser(description='Programa para generar histogramas normales')
parser.add_argument('media' ,help= 'Promedio de la distribucion')
parser.add_argument('desv', help= 'Error de la distribucion')
parser.add_argument('--n',default=100, help= 'Numero de datos a generar') #Esto se vuelve opcional para el usuario

args = parser.parse_args()


#Definir variables
n = int(args.n)
media = float(args.media)
desv = float(args.desv)

#Genera numeros aleatorios que sigan una distribucion normal
datos = np.random.normal(size = n, loc = media, scale = desv) 

#Tranforma los numeros aleatorios generados en enteros
datos = datos.round(0).astype(int) 

#Quitar colas de la distribucion (quitar valores atipicos)
datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 

#Construir un data frame
datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 

#Conteo (frecuencia) de cada uno de los casos
histograma = datos_trim.groupby('Datos').size() 


for i in range(len(histograma)): 

    #Asigna mas si cada datos generado es positivo
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
    #Imprime cada dato generado, un espacio y luego una catidad de asteriscos 
    #que depende de la proporcion de veces que se observo ese dato
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )