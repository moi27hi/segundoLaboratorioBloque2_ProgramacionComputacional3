import pandas as pd 

archivo = pd.read_csv("Student data 4.csv")


archivo = pd.read_csv("Student data 4.csv")

archivo.columns = ["Year of passing", "Gender", "ID number", 
                   "Matric marks", "Matric obtain marks", 
                   "Inter marks", "Inter obtain marks"]


print(archivo)

# Resumen de la informacion del dataset usando describe().
print("****Resumen del dataset***\n")
print(archivo.describe())

# Imprimiendo las columnas del dataset. 
print(archivo.columns)

# Usando dtypes() para identificar el tipo de datos
print("\n*** Identificando el tipo de datos***\n")
print(archivo.dtypes)


# primeros cinco valores  

print("\n*** 5 Valores iniciales**\n")
print(archivo.head())

# ultimos 5 valores o la cantidad que especifique.
print("\n*** 5 Valores finales***\n")
print(archivo.tail())



# Ordenando los datos de la columna Obtain Marks. 
print("***\n Ordenando los datos de la columna Obtain marks de mayor a menor\n")
print(archivo.sort_values("Matric obtain marks",ascending=False))



print('\n ***Analisis estadistico***\n')


print(f"La Media de las calificaciones obtenidas por estudiantes de high school en el examen MATRIC es de: {archivo['Matric obtain marks'].mean()}")
print(f"La mediana de las calificaciones obtenidas por estudiantes de high school en el examen MATRIC es de: {archivo['Matric obtain marks'].median()}")
print(f"Varianza: {archivo['Matric obtain marks'].var()}")
print(f"Desviacion estandar: {archivo['Matric obtain marks'].std()}")
print(f"La nota mas alta es: {archivo['Matric obtain marks'].max()}")
print(f"La nota mas baja: {archivo['Matric obtain marks'].min()}")




# a. Describe brevemente de qué trata el dataset utilizado
# Este Dataset contiene informacion sobre informacion de los estudiantes como datos academicos como diferentes tipos de calificaciones, genero, año , numero Id de estudiante en las pruebas Inter y Matric

#b. ¿Qué información permite ver el resumen estadístico?
# El método describe() permite ver: La distribución de las calificaciones (media, mediana, mínimo, máximo). La consistencia de los puntajes máximos (todos los Matric marks y Inter marks son 1100).Que las notas de secundaria varían bastante (mínimo 501, máximo 1092), mientras que las de preparatoria parecen fijas en 990.

# c. ¿Qué cambios o tendencias se detectan en la información del dataset?
#En 2024 predominan estudiantes con notas más altas en secundaria.
#En 2025 aparecen registros con notas más bajas (alrededor de 600), mostrando una disminución en el rendimiento.

#d. ¿Qué categorías sobresalen en la comparación y por qué crees que será?
# En 2024 predominan estudiantes con notas más altas en secundaria.
#En 2025 aparecen registros con notas más bajas (alrededor de 600), mostrando una disminución en el rendimiento.

#e. ¿Qué diferencias se observan entre los primeros y últimos registros?
#Los primeros registros (2024) tienen notas de secundaria muy altas (superiores a 1000).
#Los últimos registros (2025) incluyen estudiantes con notas mucho más bajas (600–700).
#Esto sugiere una tendencia descendente en el rendimiento académico entre ambos años.

#f. ¿Qué aportan las medidas estadísticas al análisis del dataset?
#La media permite conocer el rendimiento promedio de los estudiantes.
#La mediana muestra el punto central, útil porque no se ve tan afectada por valores extremos.
#La desviación estándar indica qué tan dispersas están las notas: en secundaria es alta (≈187), lo que significa gran variabilidad entre estudiantes.