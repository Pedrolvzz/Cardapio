# Sistema de Pedidos de Restaurante

Programa de terminal em Python para consultar um cardápio, montar um pedido e calcular o valor total.

## Cardápio

O menu reúne quatro categorias:

- **Pratos principais:** Bruschetta, Salada Caprese, Parmegiana, Macarrão a Bolonhesa, Frango Grelhado e Peixe Assado.
- **Acompanhamentos:** Arroz, Batata Frita G e Salada.
- **Bebidas:** Suco, Refrigerante 1L e Água.
- **Sobremesas:** Pudim, Brigadeiro e Sorvete.

Os preços são definidos no próprio código.

## Como executar

1. Salve o código em um arquivo, por exemplo, `restaurante.py`.
2. Abra um terminal na pasta onde salvou o arquivo.
3. Execute:

   ```bash
   python restaurante.py
   ```

   Em alguns sistemas, o comando pode ser `python3 restaurante.py`.

## Opções do menu

1. **Ver Cardápio** — mostra os produtos e os preços de cada categoria.
2. **Fazer Pedido** — permite adicionar itens digitando seus nomes. Após cada item, informe `s` para continuar ou `n` para encerrar a seleção.
3. **Ver Pedido e total** — exibe os itens adicionados e calcula o total.
4. **Finalizar Pedido** — apresenta um resumo do pedido e o valor total.
5. **Sair** — encerra o programa.

## Observações

- Os nomes dos itens são comparados sem diferenciar maiúsculas de minúsculas e sem considerar espaços. Por exemplo, `Batata Frita G` pode ser digitado como `batatafritag`.
- O pedido existe apenas enquanto o programa está em execução; ele não é salvo em arquivo.
- Na opção **Ver Pedido e total**, o código atual imprime cada item como uma tupla e usa a variável `preco` sem defini-la dentro do laço de exibição. Para mostrar corretamente nome e preço nessa opção, percorra o pedido desempacotando cada par `(nome, preco)`, como já é feito em `finalizar_pedido`.
- A entrada do menu é convertida diretamente para inteiro. Digitar letras ou deixar a entrada vazia causa um erro; informe um número de 1 a 5.
