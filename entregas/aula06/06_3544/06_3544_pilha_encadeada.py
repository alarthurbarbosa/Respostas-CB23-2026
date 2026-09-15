
class _No():
    def __init__(self, valor, proximo = None):
        self.valor = valor
        self.proximo = proximo

class PilhaEncadeada:
    def __init__(self):
        self.topos = None
        self.quantidade = 0

    def push(self,item):
        novo = _No(item, self.topos)
        self.topos = novo
        self.quantidade += 1

    def pop(self):
        if self.topos == None:
            raise IndexError("A pilha está vazia, não há elementos para remover")
         
        antigo_topo = self.topos.valor
        self.topos = self.topos.proximo
        self.quantidade -= 1
        return antigo_topo
    
    
    def topo(self):
        if self.topos == None:
            raise IndexError("A pilha está vazia, não há topo.")
        else:
            return self.topos.valor
        
    def len(self):
        return self.quantidade

    
    def esta_vazia(self):
        if self.topos == None:
            return True
        else:
            return False

    def repr(self):
        atual = self.topos
        lista_valores = list()
        if self.topos == None:
            return ""

        else:
            for i in range(self.quantidade):
                lista_valores.append(atual.valor)
                atual = atual.proximo
            return " -> ".join([str(k) for k in lista_valores ])


        
        

#pilha.push = acrescenta um no ao topo
#pilha.pop = retira um no do topos