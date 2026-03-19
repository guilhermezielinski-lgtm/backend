real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar_cotacao = 5.24
conversao = real / dolar_cotacao
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, conversao))
