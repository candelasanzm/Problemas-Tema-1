#EJERCICIO 8
def invertir(n):
    def inverso(n, acc):
        if n == 0: # caso base, cuando no quedan mas cifras a estudiar en el numero o el numero es 0 devuelve el acumulado
            return acc
        else: # en caso de que n no sea cero, se llama a la funcion auxiliar "inverso"; dividimos el numero entre 10 para eliminar el ultimo digito y ese ultimo digito se le añade al acumulador en su correspondiente posicion
            return inverso(n // 10, acc * 10 + n % 10)
    return inverso(n, 0)   

# Casos de prueba
invertir0 = invertir(0)
invertir1 = invertir(1)
invertir50 = invertir(50) # debería salir 5 porque el 0 de 05 no se pone
invertir58 = invertir(58)
invertir5908 = invertir(5908)
print(invertir0)
print(invertir1)
print(invertir50)
print(invertir58)
print(invertir5908)

# Test
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

def test_benchmark_invertir_58 (benchmark): 
    res = benchmark(invertir, 58)
    assert res == 85