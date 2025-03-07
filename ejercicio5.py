import math

def esPrimo(n : int) -> bool :
    """ Comprueba si un número es primo """
    if n <= 0 : # si el numero es menor o igual a cero da un error porque el cero o los numeros negativos no se consideran primos
        raise ValueError ("Error: el número debe ser mayor que cero")
    
    elif n == 1: # si el numero es uno da false porque el uno no cuenta como numero primo 
        return False
    
    else:
        raiz = int (math.sqrt(n))
        primo = True
        i = 2
        while (primo and i <= raiz) : # si el numero es primo y menor que la raiz cuadrada de n entro en el while, porque si n tiene un divisor distinto de 1 y de si mismo, al menos uno de esos divisores sera menor o igual que la raiz cuadrada de n
            if (n % i == 0) : # si el numero es divisible entre la i, no es primo 
                primo = False
            i += 1
    return primo

# Casos de prueba
esPrimo2 = esPrimo(2)
esPrimo29 = esPrimo(29)
esPrimo4 = esPrimo(4)
esPrimo36 = esPrimo(36)
print(esPrimo2)
print(esPrimo29)
print(esPrimo4)
print(esPrimo36)

# Test
def test_esPrimo() :
    numeros = [3, 5, 6, 7, 8, 10, 11, 0, 1, -5]
    primo = [True, True, False, True, False, False, True, False, False, False]
    res = []
    for num in numeros:
        try:
            res += [esPrimo(num)]
        except ValueError:
            res += [False]
    assert res == primo

def test_benchmark_esPrimo_10 (benchmark):
    res = benchmark(esPrimo, 10)
    assert res == False

def test_benchmark_esPrimo_7 (benchmark):
    res = benchmark(esPrimo, 7)
    assert res == True

def test_benchmark_esPrimo_1288 (benchmark):
    res = benchmark(esPrimo, 1288)
    assert res == False