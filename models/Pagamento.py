from models.Pedido import Pedido
class Pagamento:
    def __init__(self, metPagamento, valor, notaFiscal):
        self.MetPagamento = metPagamento
        self.Valor = valor
        self.NotaFiscal = notaFiscal
        
    def meioPagamento(produto, pagamento):
        print('='*20,'Pagamento do Cinema','='*20)

produto = float(input('Qual é o Valor do Produto? R$ '))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à Vista Boleto
[ 2 ] à Vista no Cartão de Crédito ou Débito
[ 3 ] 2x no Cartão de Crédito
[ 4 ] 3x ou mais no Cartão de Crédito
Qual é a Opção? '''))

avista = produto / 100 * 100
avistacrt = produto / 100 * 100
juros = produto / 100 * 110

if pagamento == 1:
    print('O Valor do Produto Ficará R$ {:.2f} à Vista no Boleto.'.format(avista))
elif pagamento == 2:
    print('O Valor do Produto Ficará R$ {:.2f} à Vista no Cartão de Crédito.'.format(avistacrt))
elif pagamento == 3:
    print('Sua Compra será Parcelada em 2x de R$ {:.2f}\n'
          'Sua Compra vai Custar R$ {:.2f}.'.format(produto/2, produto))
elif pagamento == 4:
    parcelas = int(input('Quantas Parcelas? '))
    if parcelas >= 3:
        print('Sua Compra será Parcelada em {}x de R$ {:.2f} COM JUROS\n'
          'Sua Compra de R$ {:.2f}, Vai Custar R$ {:.2f}.'.format(parcelas,juros / parcelas,produto,juros))
    elif parcelas == 1:
        print('O Valor do Produto Ficará R$ {:.2f} à Vista no Boleto.'.format(avista))
    elif parcelas == 2:
        print('O Valor do Produto Ficará R$ {:.2f} à Vista no Cartão.'.format(avistacrt))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. POR FAVOR, TENTE NOVAMENTE!!!')
