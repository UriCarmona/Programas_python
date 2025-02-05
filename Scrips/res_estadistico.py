import pandas as pd
import numpy as np
import argparse

#Crear Parser
parser = argparse.ArgumentParser()
parser.add_argument('archivo')

args = parser.parse_args()

file = str(args.archivo)

#cargar datos
datos = pd.read_csv(file,header=None)
serie = datos.iloc[:,0]

#calcular los estadisticos
n = serie.count()
prom = serie.mean()
med = serie.median()
q1 = serie.quantile(0.25)
q3 = serie.quantile(0.75)
iqr = q3 -q1

#Presentar resultados
resumen = pd.DataFrame(dict(
    n = n,
    Promedio = prom,
    Mediana = med,
    Cuartil_1 = q1,
    Cuartil_3 = q3,
    IQR = iqr
), index= [''])

print (resumen)