class Pedido:
    def __init__(self, estoque, valor, quantidade, produto):
        self.Estoque = estoque
        self.Valor = valor
        self.Quantidade = quantidade
        self.Produto = produto

    def cardapio(cod):
    menu = [(100,'Pipoca Pequena',12.00), (200,'Pipoca Media', 15.00), (300, 'Pipoca Grande', 20.00),
    (400,'Refrigerante Pequeno', 7.00), (500, 'Refrigerante Medio', 9.00), (600, 'Refrigerante Grande', 11.00), (700, 'Agua', 4.00)]
     
    for c, sand, pr in menu:
        if c == cod:
           return sand, pr 
    return '',0.0
def imprimenota(ped):
    tot = 0
    totg = 0
    print('Pedido            Quantidade        V.Unit        Total')
    
    for (sand,qtd,pr) in pedido:
        tot = qtd * pr 
        print(sand, (24 - len(sand))*' ', qtd, '           ', pr, '        ', tot)
        totg += tot
    print('                                    total da Nota: ', totg)
          
pedido = []
cod = int(input('Digite o código do cardapio ou -1 para fechar o pedido:'))
while cod != -1:
     sand, pr = cardapio(cod)
     if sand != '':
        qtd = int(input('Digite a quantidade:'))
        pedido.append((sand,qtd,pr)) 
     cod = int(input('Digite o código do cardapio ou -1 para fechar o pedido:'))
imprimenota(pedido)
        