nome = str(input("Digite seu nome completo: "))
ano = 0
mensagem = "Digite o seu ano de nascimento [entre 1922 e 2021]: "
while (ano < 1922) or (ano > 2021):
    ano = input(mensagem)
    try: 
        ano = int(ano)
    except ValueError:
        print("Ano invalido, digite um número inteiro")
        ano = 0
        continue
    if (ano < 1922) or (ano > 2021):
        print(f"Ano invalido, {mensagem}")
        continue
    break
idade = 2022 - ano
print(f"{nome}, voce nasceu no ano de {ano} e fara {idade} anos")