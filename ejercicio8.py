#EJERCICIO 8
def invertir(n):
    def inverso(n, acc):
        if n == 0:
            return acc
        else:
            return inverso(n // 10, acc * 10 + n % 10)
    return inverso(n, 0)   

def test_invertir() :
    res = 726
    res = 0
    assert invertir(726) == 627
    assert invertir(0) == 0

def test_benchmark_invertir_0 (benchmark) :
    assert benchmark (invertir, 0) == 0

def test_benchmark_invertir_5876 (benchmark): 
    assert benchmark (invertir, 5876) == 6785
