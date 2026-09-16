
import importlib
import unittest

modulo_pilha = importlib.import_module("06_3544_pilha_encadeada")
PilhaEncadeada = modulo_pilha.PilhaEncadeada

modulo_fila = importlib.import_module("06_3544_fila_encadeada")
FilaEncadeada = modulo_fila.FilaEncadeada


class TestEstruturasDeDados(unittest.TestCase):

    def test_questao_2_1_pilha(self):
        # Teste: Pilha com elementos
        a = PilhaEncadeada()
        a.push(40)
        a.push(30)
        a.push(20)

        tirar = a.pop()
        self.assertEqual(tirar, 20)
        self.assertFalse(a.esta_vazia())
        self.assertEqual(a.len(), 2)
        self.assertEqual(a.topo(), 30)
        self.assertEqual(a.repr(), "30 -> 40")

        # Teste: Pilha vazia
        b = PilhaEncadeada()
        self.assertTrue(b.esta_vazia())
        self.assertEqual(b.len(), 0)

        with self.assertRaises(IndexError):
            b.topo()

    def test_questao_2_2_fila(self):
        # Teste: Fila com elementos
        c = FilaEncadeada()
        c.enfileirar(10)
        c.enfileirar(20)
        c.enfileirar(30)

        self.assertEqual(c.desenfileirar(), 10)
        self.assertEqual(c.frente(), 20)
        self.assertFalse(c.esta_vazia())
        self.assertEqual(c.len(), 2)

        # Teste: Fila vazia
        d = FilaEncadeada()
        self.assertTrue(d.esta_vazia())
        self.assertEqual(d.len(), 0)

        with self.assertRaises(IndexError):
            d.frente()


if __name__ == "__main__":
    unittest.main()
