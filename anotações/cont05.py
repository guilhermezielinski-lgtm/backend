# ORDEM DE PRECEDÊNCIA
# 
# Definição: é a ordem na qual os operadores serão executados
# 
# 1ª Expressões dentro de parênteses ()
# 2ª Em seguida vem as potenciações **
# 3ª Em terceiro lugar vem a multiplicação (*), a divisão normal (/), 
#    a divisão inteira (//) e o resto da divisão (%). 
#    No caso de ter mais de um deles você resolve quem aparecer primeiro (da esquerda para a direita).
# 4ª E por último a soma (+) e a subtração (-)

# EXEMPLO
#
# 5 + 3 * 2 = 11
# (Multiplicação primeiro: 3 * 2 = 6. Depois a soma: 5 + 6 = 11)
#
# 3 * 5 + 4 ** 2 = 31
# (Potência primeiro: 4 ** 2 = 16. Depois multiplicação: 3 * 5 = 15. Por fim: 15 + 16 = 31)
#
# 3 * (5 + 4) ** 2 = 243
# (Parênteses primeiro: 5 + 4 = 9. Depois potência: 9 ** 2 = 81. Por fim multiplicação: 3 * 81 = 243)
#
# O Python é utilizado em cálculos científicos devido ao tamanho da memória, 
# ou seja, conseguimos chegar a números extremamente grandes.


# OUTROS OPERADORES
#
# Para exponenciação podemos usar o pow(x,y) onde o número x é elevado ao número y.
# Ex: pow(4, 2) resulta em 16.
#
# Para raiz quadrada podemos usar o **(1/2), elevando o número a 1/2 nós 
# obtemos a raiz quadrada, para raiz cúbica **(1/3), e assim por diante.
# Ex: 25 ** (1/2) resulta em 5.0.
#
# Podemos usar os operadores em strings.
# Ex: '=' * 5 vai ficar '====='

