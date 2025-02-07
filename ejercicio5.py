import math

def esPrimo(n : int) -> bool :
    """ Comprueba si un número es primo """
    raiz = int (math.sqrt(n))
    primo = True
    i = 2
    while (primo and i <= raiz) :
        if (n % i == 0) :
            primo = False
        i += 1
    return primo

def test_esPrimo() :
    assert (esPrimo(5)) == True
    assert (esPrimo(8)) == False
    assert (esPrimo(11)) == True
    assert (esPrimo(15)) == False

def test_benchmark_esPrimo_10 (benchmark):
    assert benchmark (esPrimo, 10) == False

def test_benchmark_esPrimo_7 (benchmark):
    assert benchmark (esPrimo, 7) == True

def test_benchmark_esPrimo_12 (benchmark):
    assert benchmark(esPrimo, 12) == False