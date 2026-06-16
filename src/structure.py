# Trabalho de Estrutura de Dados: Simulador de Livro de Ofertas e Performance de Estruturas
# Fernanda Rubio de Mello (), Maria Olívia Meca de Siqueira (17099902), Karen ... (), Kaun Yuri ... (), Vinicius ... ().

from datetime import datetime

# 3 estruturas principais do sistema:

# 1. Fila de Entrada (Fila/Queue): Todas as novas ordens entram em uma fila FIFO para aguardar o processamento pelo motor.
# 2. 2. Livro de Ofertas (Listas Duplamente Encadeadas Ordenadas): Lista de Compras -> Mantida em ordem decrescente de preço (melhor comprador no início - maior preço → menor preço) e Lista de Vendas -> Mantida em ordem crescente de preço (melhor vendedor no início - menor preço → maior preço).
# 3. Sistema de Undo (Pilha/Stack): Armazena o ID das ordens inseridas com sucesso no livro para permitir o cancelamento r ́apido da  ́ultima a ̧c ̃ao.

class Order:

  # As ordens de negociação que serão inseridas

  def __init__(self, id:int, tipo:str, preco:float, quantidade:int, timestamp:datetime):
    self.id = id
    self.tipo = tipo  # 'C' compra ou 'V' venda
    self.preco = preco
    self.quantidade = quantidade
    self.timestamp = datetime.now()

class Node: # Lista Duplamente Encadeada

  def __init__(self, order):
    self.order = order
    self.next = None
    self.prev = None

class Queue: # Fila

  def __init__(self):
    self.front = None
    self.rear = None

class Stack: # Pilha

  def __init__(self):
    self.top = None

class DoublyLinkedList:

  # Representa as listas de ordens: self.buy_order e self.sell_orders
  # Lista de Compras: maior preço → menor preço
  # Lista de Vendas: menor preço → maior preço

  def __init__(self, tipo:str):
    self.head = None
    self.tipo = tipo  # 'C' compra ou 'V' venda

class OrderBook:

  # Possui: uma lista de compras, uma lista de vendas, uma fila de entrada e uma pilha para undo.

  def __init__(self):
    self.buy_orders = DoublyLinkedList('C')
    self.sell_orders = DoublyLinkedList('V')
    self.input_queue = Queue()
    self.undo_stack = Stack()
