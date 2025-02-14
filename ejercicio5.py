import math

def esPrimo(n : int) -> bool :
    """ Comprueba si un número es primo """
    if n <= 0 :
        raise ValueError ("Error: el número debe ser mayor que cero")
    
    elif n == 1:
        return False
    
    else:
        raiz = int (math.sqrt(n))
        primo = True
        i = 2
        while (primo and i <= raiz) :
            if (n % i == 0) :
                primo = False
            i += 1
    return primo

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

def test_benchmark_esPrimo_12 (benchmark):
    res = benchmark(esPrimo, 12)
    assert res == False