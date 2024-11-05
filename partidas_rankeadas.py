nome = input("Digite o nome do herói: ")
xp = 0
vitorias = 0
derrotas = 0

print()

while input("Deseja enfrentar um monstro (s/n): ") == "s":
    nivel_do_monstro = int(input("Qual o nível do monstro? "))
    nivel_de_dificuldade = int(input("Qual o nível de dificuldade? "))
    nivel_da_batalha = nivel_do_monstro * nivel_do_monstro * 100

    if xp >= nivel_da_batalha - 1000:
        vitorias += 1
        xp += nivel_da_batalha

        print("**Vitória**")
        print("XP:", xp)
    else:
        derrotas += 1

        print("**Derrota**")
    
    print(f"Vitórias: {vitorias}   Derrotas: {derrotas}")
    print()

def saldo_de_rankeadas(saldo):
    if saldo <= 10:
        return "Ferro"
    elif saldo <= 20:
        return "Bronze"
    elif saldo <= 50:
        return "Prata"
    elif saldo <= 80:
        return "Ouro"
    elif saldo <= 90:
        return "Diamante"
    elif saldo <= 100:
        return "Lendário"
    return "Imortal"

saldo_vitorias = vitorias - derrotas
nivel = saldo_de_rankeadas(saldo_vitorias)

print(f"O Herói tem de saldo de **{saldo_vitorias}** está no nível de **{nivel}**")
