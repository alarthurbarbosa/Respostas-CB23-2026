
qual_class = input("Digite a questão que deseja testar (2.1 ou 2.2): ")
    
import importlib
modulo_pilha = importlib.import_module("06_3544_pilha_encadeada")
PilhaEncadeada = modulo_pilha.PilhaEncadeada

import importlib 
modulo_fila = importlib.import_module("06_3544_fila_encadeada")
FilaEncadeada = modulo_fila.FilaEncadeada

if qual_class == "2.1":
    # Teste Questao 2.1

    # Pilha com nós

    a = PilhaEncadeada()
    a.push(40)
    a.push(30)
    a.push(20)
    tirar = a.pop()

    print(tirar)
    print(a.esta_vazia())
    print(a.len())
    print(a.topo())
    print(a.repr())

    # Pilha vazia
    b = PilhaEncadeada()
    print(b.esta_vazia())
    print(b.len())
    print(b.topo())

    


else:
    # Teste Questao 2.2

    # Fila com pilhas

    c = FilaEncadeada()

    c.enfileirar(10)
    c.enfileirar(20)
    c.enfileirar(30)

    print(c.desenfileirar())
    print(c.frente())
    print(c.esta_vazia())
    print(c.len())
    print(c.repr())
    print()

    # Fila vazia
    d = FilaEncadeada()
    print(d.esta_vazia())
    print(d.len())
    print(d.frente())
