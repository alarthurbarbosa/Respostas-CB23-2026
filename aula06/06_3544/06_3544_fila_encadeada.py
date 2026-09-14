import importlib 

modulo_pilha = importlib.import_module("06_3544_pilha_encadeada")
PilhaEncadeada = modulo_pilha.PilhaEncadeada

class _No():
    def __init__(self, valor, proximo = None):
        self.valor = valor
        self.proximo = proximo

class FilaEncadeada:
    def __init__(self):
        self.entrada = PilhaEncadeada()
        self.saida = PilhaEncadeada()

    def enfileirar(self, item):
        self.entrada.push(item)

    def desenfileirar(self):
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            raise IndexError("A fila está vazia, não há elementos para remover")
        
        else:
            if self.saida.esta_vazia():
                while self.entrada.len() > 0:
                    self.saida.push(self.entrada.pop())
                    
            return self.saida.pop()

    def frente(self):
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            raise IndexError("A fila está vazia, não há elementos para acessar")
        
        else:
            if self.saida.esta_vazia():
                while self.entrada.len() > 0:
                    self.saida.push(self.entrada.pop())
            return self.saida.topo()

    def esta_vazia(self):
        return self.entrada.esta_vazia() and self.saida.esta_vazia()

    def len(self):
        return self.entrada.len() + self.saida.len()

    def repr(self):
        if self.entrada.esta_vazia() and self.saida.esta_vazia():
            return "" 
        else:
            lista_fila = list()
            if self.saida.len() == 0:
                while self.entrada.len() > 0:
                    self.saida.push(self.entrada.pop()) 
            for i in range(self.entrada.len() + self.saida.len()):
                lista_fila.append(self.saida.pop())
                self.entrada.push(self.saida.pop())
            return " -> ".join([str(k) for k in lista_fila])