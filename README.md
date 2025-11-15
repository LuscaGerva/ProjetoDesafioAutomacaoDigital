# DEPÓSITOS DE PEÇAS

## Sobre o projeto
O projeto visa o cadastro, armazenamento, organização e visualização de pças cadastradas, com objetivo de automatizar o processo com programação. Foi construído utilizando a linguagem Python com funções própria da linguagem. 

## Instrução de configuração
Necessário a instalção apenas do Python, visto que utiliza somente funções nativas da linguagem.

## Instrução de uso
Para o usuário, ao executar o código, será exibido um menu de interação em que pedirá para que seja inserido um número de 0 a 6, sendo cada número uma interação diferente com o projeto.

### O sistema é controlado por um menu principal com as seguintes opções:

1. Cadastrar nova peça:

    * Solicita ao usuário o ID, peso, comprimento e cor da peça.

    * O sistema avalia a peça com base nos critérios de aprovação.

    * Informa se a peça foi aprovada ou reprovada e a armazena na lista correspondente.

2. Listar peças aprovadas:

    * Mostra todas as peças aprovadas, organizadas por número da caixa.

    * Exibe o status de cada caixa (Ex: "ABERTA (3/10)" ou "FECHADA").

    * Detalha o ID, peso, cor e comprimento de cada peça dentro da caixa.

3. Listar peças reprovadas:

    * Mostra todas as peças que foram reprovadas, com seus respectivos detalhes (ID, peso, cor, comprimento).

4. Remover peça cadastrada aprovada:

    * Solicita o ID de uma peça.

    * Busca a peça apenas nas caixas de peças aprovadas e a remove.

    * Nota: Esta ação pode fazer com que uma caixa "FECHADA" se torne "ABERTA" se o número de itens cair para 9.

5. Listar caixas fechadas:

    * Exibe apenas as caixas que atingiram a capacidade máxima (10 peças).

6. Gerar relatório final:

    Apresenta um resumo estatístico da operação:

    * Total de peças cadastradas.

    * Total de peças aprovadas.

    * Total de peças reprovadas.

    * Total de caixas utilizadas (abertas ou fechadas).

7. Sair do projeto:

    * Encerra a execução do programa.

### Cadastro de Peças
Para o cadastro de peças, é pedido algumas informações. Essa peça cadastrada é comparada com os requisitos estabelecidos, e poderá ir para uma caixa de peças aprovadas ou reprovadas a depender se atendeu ou não os requisitos.

### Critérios de Aprovação
Para uma peça ser considerada "APROVADA", ela deve atender simultaneamente a todos os seguintes critérios:

- Peso: Entre 95g e 105g.

- Cor: "azul" ou "verde" .

- Comprimento: Entre 10cm e 20cm.

Se qualquer um desses critérios falhar, a peça é automaticamente "REPROVADA".

### Lógica de Armazenamento
As peças aprovadas são armazenadas em caixas.

Cada caixa tem um limite de 10 peças.

Quando uma caixa atinge o limite, ela é considerada "FECHADA" e uma nova caixa é aberta para as próximas peças aprovadas.

As peças reprovadas são armazenadas em uma lista separada.



### Exemplos de Entradas e Saídas

Veja um fluxo de uso comum do programa.

#### Exemplo 1: Cadastrando uma Peça APROVADA

O usuário escolhe a opção `1` e insere dados que atendem aos critérios.

**Entrada:**
Digite a opção desejada: 1 

================= Cadastro de Peças ================= 

* Insira o id da peça: 12
* Insira o peso da peça em gramas (apenas número): 100 
* Insira o comprimento da peça (em centímetros): 15 
* Insira a cor da peça (tudo mínusculo): azul


**Saída:**
Peça 12 APROVADA

Nova caixa criada. Total de caixas: 1 Peça adicionada na caixa 1. Itens na caixa: 1/10



#### Exemplo 2: Listando Peças Aprovadas

O usuário escolhe a opção `2` para verificar o estoque.

**Entrada:**
Digite a opção desejada: 2


**Saída:**
================= Peças Aprovadas =================

Caixa 1 - Status: ABERTA (1/10) ID: 12, Peso: 100.0g, Cor: azul, Comprimento: 15.0cm
