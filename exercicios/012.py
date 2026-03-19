larg = float(input('Largura da parede (em metros): '))
alt = float(input('Altura da parede (em metros): '))
area = larg * alt
tinta = area / 2
print(f'\nSua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')
