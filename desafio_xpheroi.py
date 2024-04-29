
def obter_dados_heroi():
    nome = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de experiência (XP) do herói: "))
    return nome, xp


def determinar_nivel(xp):
    if xp < 1000:
        return "Ferro"
    elif 1000 <= xp <= 2000:
        return "Bronze"
    elif 2001 <= xp <= 5000:
        return "Prata"
    elif 5001 <= xp <= 7000:
        return "Ouro"
    elif 7001 <= xp <= 8000:
        return "Platina"
    elif 8001 <= xp <= 9000:
        return "Ascendente"
    elif 9001 <= xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"


def main():
    
    nome, xp = obter_dados_heroi()
    nivel = determinar_nivel(xp)
    
    print(f"O Herói de nome {nome} está no nível de {nivel}")


main()
