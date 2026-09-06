# Resposta complementar da questão 2

Desenfileirar pode custar $O(N)$ pois depende do número de elementos da pilha de entrada. Isso faz com que o programa tenha que transferir toda a pilha de entrada para a pilha de saída. Se há $N$ elementos, então o programa realiza $N$ transferências.

Quando a pilha de saída não está vazia, desenfileirar pode custar $O(1)$, pois nesse caso não é necessário que o programa realize a transferência. Se existem elementos na pilha de saída, o programa não precisa passar todos os $N$ elementos da pilha de entrada para a pilha de saída, e isso é uma operação com custo constante, ou seja, não depende de $N$.
