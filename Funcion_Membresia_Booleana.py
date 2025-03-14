# FUZZIFICACION
def membresia_booleana(x, x0):
    if (x < x0):
        return 0

    return 1

def membresia_booleana_inversa(x, x0):
    if (x < x0):
        return 1

    return 0

def membresia_booleana_grado(x, x0, x1):
    if (x < x0):
        return 0;

    if (x >= x0 and x <= x1):
        return ?;
    
    return 1;

def membresia_booleana_grado_inversa(x, x0, x1):
    if (x < x0):
        return 1;

    if (x >= x0 and x <= x1):
        return ?;
    
    return 0;

def membresia_triangulo(x, x0, x1, x2):
    if (x < x0 or x > x2):
        return 0;

    if (x >= x0 and x <= x1):
        return ?;
    
        if (x >= x1 and x <= x2):
            return ?;

def membresia_trapezoidal(x, x0, x1, x2, x3):
    if (x < x0 or x > x3):
        return 0;

    if (x >= x0 and x <= x1):
        return ?;
    
        if (x >= x1 and x <= x2):
            return 1;
        
            else:
                return ?;
        
# --------------------------------------------------------------------------------------------------------------------------------------------------

# Método de Mamdani 
# Este método es uno de los más utilizados en la lógica difusa. Combina reglas difusas con operadores de conjuntos difusos para obtener un resultado 
# difuso.
# Paso 1. Se evalúan todas las reglas difusas y se obtiene un conjunto difuso para cada una.
# Paso 2. Se agregan todos los conjuntos difusos obtenidos en el paso anterior. 
# Paso 3. Se aplica el operador de implicación para obtener un conjunto difuso de salida.
# Paso 4. Se defuzzifica el conjunto difuso de salida para obtener un valor nítido.

import numpy as np

# Funciones de membresía para la temperatura
def temperatura_alta(x):
    return max(0, min(1, (x - 30) / 10))  # Si x es mayor que 30, es alta

def temperatura_baja(x):
    return max(0, min(1, (35 - x) / 5))  # Si x es menor que 35, es baja

# Funciones de membresía para el ventilador
def ventilador_alto(x):
    return max(0, min(1, (x - 30) / 10))

def ventilador_bajo(x):
    return max(0, min(1, (35 - x) / 5))

# Fuzzificación: convertir la temperatura en grados difusos
def fuzzificar(temperatura):
    temp_alta = temperatura_alta(temperatura)
    temp_baja = temperatura_baja(temperatura)
    return temp_alta, temp_baja

# Regla de Implicación: reglas Si-Entonces
def implicacion(temp_alta, temp_baja):
    # Usar las funciones de membresía para calcular la salida difusa
    velocidad_alta = ventilador_alto(30) * temp_alta 
    velocidad_baja = ventilador_bajo(10) * temp_baja 

    return velocidad_alta, velocidad_baja

# Calcular el valor promedio ponderado de la salida
def defuzzificacion(velocidad_alta, velocidad_baja):
    return (velocidad_alta * 40 + velocidad_baja * 10) / (velocidad_alta + velocidad_baja)

# Aplicar el sistema Mamdani
temperatura = 32 
temp_alta, temp_baja = fuzzificar(temperatura) 
vel_alta, vel_baja = implicacion(temp_alta, temp_baja)  
velocidad_ventilador = defuzzificacion(vel_alta, vel_baja) 

print(f"Velocidad del ventilador: {velocidad_ventilador:.2f} km/h")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Método de Agregación
# Este método combina varios conjuntos difusos en uno solo.
# Paso 1. Se toman los conjuntos difusos que se quieren combinar.
# Paso 2. Se aplica un operador de agregación para combinarlos en un solo conjunto difuso.

import numpy as np

# Función de membresía para la temperatura
def temperatura_alta(x):
    return max(0, min(1, (x - 30) / 10))

def temperatura_baja(x):
    return max(0, min(1, (35 - x) / 5))

# Funciones de membresía para el ventilador
def ventilador_alto(x):
    return max(0, min(1, (x - 30) / 10))

def ventilador_bajo(x):
    return max(0, min(1, (35 - x) / 5))

# Fuzzificación: convertir la temperatura en grados difusos
def fuzzificar(temperatura):
    temp_alta = temperatura_alta(temperatura)
    temp_baja = temperatura_baja(temperatura)
    return temp_alta, temp_baja

# Agregación: combinar los resultados de varias reglas
def agregacion(velocidad_alta1, velocidad_baja1, velocidad_alta2, velocidad_baja2):
    # Usamos el máximo entre las salidas de las reglas para agregarlas
    velocidad_agregada_alta = max(velocidad_alta1, velocidad_alta2)
    velocidad_agregada_baja = max(velocidad_baja1, velocidad_baja2)
    return velocidad_agregada_alta, velocidad_agregada_baja

# Aplicar el sistema de agregación
temperatura1 = 32  
temperatura2 = 28 

temp_alta1, temp_baja1 = fuzzificar(temperatura1)
temp_alta2, temp_baja2 = fuzzificar(temperatura2)

# Calcular la implicación para ambas temperaturas
vel_alta1 = ventilador_alto(30) * temp_alta1
vel_baja1 = ventilador_bajo(10) * temp_baja1

vel_alta2 = ventilador_alto(30) * temp_alta2
vel_baja2 = ventilador_bajo(10) * temp_baja2

# Agregar las salidas de ambas reglas
vel_agregada_alta, vel_agregada_baja = agregacion(vel_alta1, vel_baja1, vel_alta2, vel_baja2)

print(f"Velocidad agregada alta: {vel_agregada_alta:.2f}")
print(f"Velocidad agregada baja: {vel_agregada_baja:.2f}")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Método de Implicación
# La Implicación en lógica difusa se refiere a cómo se traduce una regla de inferencia "Si A, entonces B" en un valor difuso. Este paso es 
# importante para determinar cuán "fuerte" es la relación entre las entradas y las salidas.
# Paso 1. Se toman dos conjuntos difusos, uno de antecedentes y otro de consecuentes.
# Paso 2. Se aplica un operador de implicación para obtener un conjunto difuso de salida.

# Funciones de membresía para la temperatura
def temperatura_alta(x):
    return max(0, min(1, (x - 30) / 10))

def temperatura_baja(x):
    return max(0, min(1, (35 - x) / 5))

# Funciones de membresía para el ventilador
def ventilador_alto(x):
    return max(0, min(1, (x - 30) / 10))

def ventilador_bajo(x):
    return max(0, min(1, (35 - x) / 5))

# Implicación: usa el mínimo entre el grado de pertenencia de la entrada y la salida
def implicacion_minima(temp_alta, temp_baja):
    # Usamos el mínimo de la temperatura para definir la velocidad
    velocidad_alta = min(ventilador_alto(30), temp_alta)  # Usamos el mínimo
    velocidad_baja = min(ventilador_bajo(10), temp_baja)  # Usamos el mínimo
    return velocidad_alta, velocidad_baja

# Aplicar el sistema de implicación
temperatura = 32  # Ejemplo: temperatura de 32°C
temp_alta, temp_baja = temperatura_alta(temperatura), temperatura_baja(temperatura)

# Implicación usando el mínimo
vel_alta, vel_baja = implicacion_minima(temp_alta, temp_baja)

print(f"Velocidad alta implicada: {vel_alta:.2f}")
print(f"Velocidad baja implicada: {vel_baja:.2f}")

# --------------------------------------------------------------------------------------------------------------------------------------------------

# DEFUZZIFICACION

# 1. Centroide
# Este método calcula el centroide de la función de membresía. Encuentra el centro de masa del área bajo la curva de membresía.
# Paso 1. Multiplicar cada valor por su grado de membresía. Esto les da un peso a cada valor.
# Paso 2. Sumar todos los productos obtenidos en el paso anterior.
# Paso 3. Sumar todos los grados de membresía.
# Paso 4. Dividir la suma de los productos entre la suma de grados de membresía.

def centroid_defuzzification(fuzzy_set):
    # Suma de (valor * membresía)
    numerator = sum(x * mu for x, mu in fuzzy_set)  

    # Suma de los grados de membresías
    denominator = sum(mu for _, mu in fuzzy_set)  

    # Evitar división por cero
    return numerator / denominator if denominator != 0 else 0

# Ejemplo de uso
fuzzy_set = [(10, 0.1), (20, 0.3), (30, 0.7), (40, 0.9), (50, 0.6)]
resultado = centroid_defuzzification(fuzzy_set)
print(resultado)  # Salida esperada: 36.1538

# --------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Promedio de Máximos (Mean of Maximum - MoM)
# Este método promedia los valores donde la función de membresía alcanza su máximo.
# Paso 1. Se busca el valor máximo de membresía en la función difusa.
# Paso 2. Se identifican todas las entradas (valores del universo) que tienen ese máximo.
# Paso 3. Se calcula el promedio de esos valores.

def mean_of_maximum_defuzzification(fuzzy_set):
    # Encontrar el valor máximo de membresía
    max_mu = max(mu for _, mu in fuzzy_set) 
    
    # Filtrar valores con ese máximo
    max_values = [x for x, mu in fuzzy_set if mu == max_mu]  

    # Calcular el promedio
    return sum(max_values) / len(max_values)  

# Ejemplo de uso
fuzzy_set = [(10, 0.2), (20, 0.6), (30, 0.9), (40, 0.9), (50, 0.7)]
resultado = mean_of_maximum_defuzzification(fuzzy_set)
print(resultado)  # Salida esperada: 35.0

# --------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Mayor de los Máximos (Largest of Maximum - LoM)
# Este método selecciona el mayor valor donde la función de membresía alcanza su máximo.
# Paso 1. Se encuentra el grado de membresía máximo.
# Paso 2. Se identifican todos los valores que tienen ese grado de membresía.
# Paso 3. Se selecciona el mayor de esos valores.

def largest_of_maximum_defuzzification(fuzzy_set):
    # Buscar el máximo grado de membresía
    max_mu = max(mu for _, mu in fuzzy_set)  

    # Tomar el mayor de los valores
    return max(x for x, mu in fuzzy_set if mu == max_mu)  

# Ejemplo de uso
fuzzy_set = [(5, 0.4), (10, 0.7), (15, 0.9), (20, 0.9), (25, 0.6)]
print(largest_of_maximum_defuzzification(fuzzy_set))  # Salida esperada: 20

# --------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Menor de los Máximos (Smallest of Maximum - SoM)
# Este método selecciona el menor valor donde la función de membresía alcanza su máximo.
# Paso 1. Se encuentra el grado de membresía máximo.
# Paso 2. Se identifican todos los valores que tienen ese grado de membresía.
# Paso 3. Se selecciona el menor de esos valores.

def smallest_of_maximum_defuzzification(fuzzy_set):
    max_mu = max(mu for _, mu in fuzzy_set)  # Buscar el máximo grado de membresía
    return min(x for x, mu in fuzzy_set if mu == max_mu)  # Tomar el menor de los valores

# Ejemplo de uso
fuzzy_set = [(5, 0.4), (10, 0.7), (15, 0.9), (20, 0.9), (25, 0.6)]
print(smallest_of_maximum_defuzzification(fuzzy_set))  # Salida esperada: 15


# --------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Promedio Ponderado (Weighted Average - WA)
# Este método calcula el promedio ponderado de los valores, usando los grados de membresía como pesos.
# Paso 1. Se multiplica cada valor por su grado de membresía.
# Paso 2. Se suma el resultado de esas multiplicaciones.
# Paso 3. Se divide por la suma total de los grados de membresía.

def weighted_average_defuzzification(fuzzy_set):
    # Suma de (valor * membresía)
    numerator = sum(x * mu for x, mu in fuzzy_set)  

    # Suma de membresías
    denominator = sum(mu for _, mu in fuzzy_set)  

    # Evitar división por cero
    return numerator / denominator if denominator != 0 else 0  

# Ejemplo de uso
fuzzy_set = [(10, 0.2), (20, 0.5), (30, 0.8), (40, 0.4)]
print(weighted_average_defuzzification(fuzzy_set))  # Salida esperada: 27.37
