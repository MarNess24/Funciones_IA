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
