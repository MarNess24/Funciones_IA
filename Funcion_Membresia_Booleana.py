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

