# OPERADORES
#
# Podemos escrever um resultado na quantidade de caracteres específica 
# ao colocar o valor dentro da máscara após escrever:

nome = input('Qual é o seu nome?')
print('prazer em conhece-lo {:20}!'.format(nome))

# Exemplo de saída no console:
# Qual é o seu nome? Gustavo
# prazer em conhece-lo Gustavo             !



# ALINHAMENTO DE MÁSCARA
#
# Podemos alinhar o nome dentro do número de caracteres que desejamos:

nome = input('Qual é o seu nome?')

# 1. Alinhamento para a direita {:>20}
print('prazer em conhece-lo {:>20}!'.format(nome))

# 2. Alinhamento para a esquerda {:<20}
print('prazer em conhece-lo {:<20}!'.format(nome))

# 3. Alinhamento no centro {:^20}
print('prazer em conhece-lo {:^20}!'.format(nome))
