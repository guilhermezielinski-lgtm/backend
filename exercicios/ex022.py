
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')


print(f'Seu nome em maiúsculas é {nome.upper()}')


print(f'Seu nome em minúsculas é {nome.lower()}')


total_letras = len(nome) - nome.count(' ')
print(f'Seu nome tem ao todo {total_letras} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
