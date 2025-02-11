#EJERCICIO 8
def invertir(n):
    def inverso(n, acc):
        if n == 0:
            return acc
        else:
            return inverso(n // 10, acc * 10 + n % 10)
    return inverso(n, 0)   

def test_invertir() :
    numeros = [726, 0, 23, 1, 5679]
    num_invertido = [627, 0, 32, 1, 9765]
    res = []
    for num in numeros:
        res += [invertir(num)]
    assert res == num_invertido

def test_benchmark_invertir_0 (benchmark) :
    res = benchmark(invertir, 0)
    assert res == 0

def test_benchmark_invertir_5876 (benchmark): 
    res = benchmark(invertir, 5876)
    assert res == 6785