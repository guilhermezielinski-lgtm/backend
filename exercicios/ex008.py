nome = input("Digite o nome do aluno")
n1 = float(input("Digite a primeira nota"))
n2 = float(input("Digite a segunda nota"))
media = n1+n2/2

if media >= 6:
 print(f"O aluno {nome} foi aprovado com a media {media}")
else:
  print(f"o aluno {nome} foi reprovado com a media {media}")
