import AulasPraticas.AP_03_ordenacao as batata
import time 
import random
import sys
sys.setrecursionlimit(max(10000, 6000))

random.seed(1001)

def benchmarking(algoritmo,lista, k = 50):
    tempo = []
    for i in range(k):
        inicio = time.perf_counter() 
        batata.divide_and_conquer_sort(lista)
        batata.quick_sort(lista)
        batata.selection_sort(lista)
        fim =  time.perf_counter()
        tempo.append(fim - inicio)
    return sum(tempo)/k


teste1 = random.sample(range(1, 100000), 100)
teste2 = random.sample(range(1, 100000), 500)
teste3 = random.sample(range(1, 100000), 1000)
teste4 = random.sample(range(1, 100000), 5000)

testes = [
    ("Teste 1", teste1),
    ("Teste 2", teste2),
    ("Teste 3", teste3),
    ("Teste 4", teste4)
]

algoritmos = [
    ("Divide and Conquer", batata.divide_and_conquer_sort),
    ("Quick Sort", batata.quick_sort),
    ("Selection Sort", batata.selection_sort)
]

print("\n" + "=" * 95)
print("                         TABELA DE TEMPOS")
print("=" * 95)

print(f"{'Teste':<10} {'Algoritmo':<22} {'Melhor Caso':<18} "
      f"{'Caso Médio':<18} {'Pior Caso':<18}")
print("-" * 95)

for nome_teste, lista in testes:

    for nome_algoritmo, algoritmo in algoritmos:

        tempos = []

        for i in range(50):

            copia = lista.copy()

            inicio = time.perf_counter()
            algoritmo(copia)
            fim = time.perf_counter()

            tempos.append(fim - inicio)

        melhor = min(tempos)
        medio = sum(tempos) / len(tempos)
        pior = max(tempos)

        print(f"{nome_teste:<10} {nome_algoritmo:<22} "
              f"{melhor:<18.8f} {medio:<18.8f} {pior:<18.8f}")

    print("-" * 95)

print("=" * 95)