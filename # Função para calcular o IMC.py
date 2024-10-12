# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

# Função para calcular o peso ideal
def calcular_peso_ideal(altura):
    peso_minimo = 18.5 * (altura ** 2)
    peso_maximo = 24.9 * (altura ** 2)
    return peso_minimo, peso_maximo

# Loop principal
while True:
    # Entrada do usuário
    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))
    peso = float(input("Informe seu peso (kg): "))
    altura = float(input("Informe sua altura (m): "))

    # Cálculo do IMC
    imc = calcular_imc(peso, altura)

    # Cálculo do peso ideal
    peso_minimo, peso_maximo = calcular_peso_ideal(altura)

    # Exibe o resultado personalizado
    print(f"\nOlá, {nome}! Você tem {idade} anos.")
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificar_imc(imc)}")
    print(f"Seu peso ideal está entre {peso_minimo:.2f} kg e {peso_maximo:.2f} kg.")

    # Pergunta ao usuário se deseja repetir
    repetir = input("\nDeseja calcular novamente? (sim/não): ").strip().lower()

    if repetir != 'sim':
        print("Encerrando o programa. Até mais!")
        break
