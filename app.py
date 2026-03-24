# Cores ANSI
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"

print(f"{AZUL}Calculadora de Consumo de Energia{RESET}\n")

# Funções de formatação
def formatar_moeda(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_numero(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

while True:
    aparelho = input("\nDigite o nome do aparelho: ")

    # Potência
    while True:
        try:
            potencia = float(input("Digite a potência do aparelho (em Watts): "))
            if potencia <= 0:
                print(VERMELHO + "Erro: Digite um valor maior que zero. Seu aparelho pode estar quebrado..." + RESET)
            else:
                break
        except ValueError:
            print(VERMELHO + "Erro: Digite apenas números." + RESET)

    # Horas
    while True:
        try:
            horas_dia = float(input("Digite o tempo médio de uso por dia (em horas): "))
            if horas_dia <= 0:
                print(VERMELHO + "Erro: Valor deve ser maior que zero. Ainda não podemos voltar no tempo" + RESET)
            else:
                break
        except ValueError:
            print(VERMELHO + "Erro: Digite apenas números." + RESET)

    valor_kwh = 0.75

    # Consumos
    consumo_diario = (potencia * horas_dia) / 1000
    consumo_semanal = consumo_diario * 7
    consumo_mensal = consumo_diario * 30
    consumo_anual = consumo_mensal * 12

    # Custos
    custo_diario = consumo_diario * valor_kwh
    custo_semanal = consumo_semanal * valor_kwh
    custo_mensal = consumo_mensal * valor_kwh
    custo_anual = consumo_anual * valor_kwh

    # Classificação
    if consumo_mensal <= 30:
        classificacao = f"{VERDE}A (Baixo consumo){RESET}"
    elif consumo_mensal <= 100:
        classificacao = f"{AMARELO}B (Médio consumo){RESET}"
    else:
        classificacao = f"{VERMELHO}C (Alto consumo){RESET}"

    # Resultado
    print("\nResultado:")
    print(f"Aparelho: {aparelho}")

    print("\nConsumo:")
    print(f"Diário: {formatar_numero(consumo_diario)} kWh")
    print(f"Semanal: {formatar_numero(consumo_semanal)} kWh")
    print(f"Mensal: {formatar_numero(consumo_mensal)} kWh")
    print(f"Anual: {formatar_numero(consumo_anual)} kWh")

    print("\nCusto estimado:")
    print(f"Por dia: R$ {formatar_moeda(custo_diario)}")
    print(f"Por semana: R$ {formatar_moeda(custo_semanal)}")
    print(f"Por mês: R$ {formatar_moeda(custo_mensal)}")
    print(f"Por ano: R$ {formatar_moeda(custo_anual)}")

    print(f"\nClassificação energética: {classificacao}")

    # Loop
    while True:
        continuar = input("\nDeseja calcular outro aparelho? (s/n): ").lower()

        if continuar == "s":
            break
        elif continuar == "n":
            print("\nEncerrando o programa...")
            exit()
        else:
            print(VERMELHO + "Erro: Responda apenas 's' ou 'n'." + RESET)