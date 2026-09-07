# Aula 5 - 24/08

    Questões
---
1 - Identifique relãções de herança entre as classes.

Resposta:

Começando de cima para baixo, veja que funcionario é uma pessoa, então, Funcionario herda da classe de Pessoa. Garçom, Gerente e Chefe de cozinha são classes de funcionários de um lugar, então Garçom herda a classe Funcionário, e a classe Funcionário herda Pessoa, o mesmo acontece com Gerente e com Chefe de Cozinha, então Gerente, Garçom e Chefe de cozinha são subclasses de Funcionário e Funcionário é sub classe de Pessoa. E veja que Funcionário é subclasse de Pessoa
então Funcionário herda nome e idade. Chefe de Cozinha herda salário, carga horário e ganha a ação de preparar. Garçom herda salário, carga horária, idade e nome e ganha a ação de anotar pedido. Gerente herda salário, carga horária, idade e nome e ganha a ação de demitir.

Pessoa <-- Funcionário <-- Garçom  

Pessoa <-- Funcionaŕio <-- Chefe de cozinha

Pessoa <-- Funcionário <-- Gerente

A classe Restaurante é herdada por Pizzaria, então Pizzaria é uma subclasse de Restaurante e herda nome, endereço e telefone, ganhando a ação de rodizio

Restaurante <-- Pizzaria

E Iguaria é herdado pelas classes Pizza e Bolo, que são subclasses,herdam nome e preço, e ganham a ação de borda recheada e formato, respectivamente.

Iguaria <-- Pizza

Iguaria <-- Bolo

---

2 - Como vocẽ modelaria a relação entre a classe Restaurante e classe Iguaria.

Resposta:

A classe Restaurante serve iguarias, então a classe Iguaria seria uma intância da classe Restaurante

---

3 - Indique os tipos que vocẽ atribuiria para os argumentos: argumento1, argumento2, argumento3.

Resposta:
Veja que garçom pode anotar vários pedidos e Chefe de cozinha prepara esses pedidos, pois podem ser 1 ou mais de 1, então os argumento1 e argumento2 são listas devidos a quantidade de iguaria que são passados.
Gerente recebe o nome de um funcionário que foi herdado pela classe Pessoa, então o argumento3 é um argumento primitivo.

---

4- Crie um diagrama de classes usando UML em um dos programas online.
