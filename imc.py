# Sistema de Cálculo de IMC

def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    
    :param peso: Peso em quilogramas (kg)
    :param altura: Altura em metros (m)
    :return: IMC calculado
    """
    if altura <= 0:
        return None  # Retorna None para indicar erro na entrada
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC em categorias.
    
    :param imc: Índice de Massa Corporal
    :return: Categoria do IMC
    """
    if imc is None:
        return "Erro no cálculo do IMC"
    
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("Bem-vindo ao Calculador de IMC")
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        imc = calcular_imc(peso, altura)
        if imc is not None:
            classificacao = classificar_imc(imc)
            print(f"Seu IMC é: {imc:.2f}")
            print(f"Classificação: {classificacao}")
        else:
            print("Erro: A altura deve ser maior que zero.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira valores numéricos.")

if __name__ == "__main__":
    main()

