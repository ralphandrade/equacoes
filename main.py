import math

# Função para calcular a equação do 1º grau
calcular_equacao_1grau = lambda a, b: (-b / a) if a != 0 else ("Identidade" if b == 0 else "Impossível")

# Função para calcular a equação do 2º grau
calcular_equacao_2grau = lambda a, b, c: (
    (("x =", (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)), ("x =", (-b - math.sqrt(b**2 - 4*a*c)) / (2*a))) if b**2 - 4*a*c > 0 
    else (("x =", -b / (2*a), "única solução real") if b**2 - 4*a*c == 0 
    else "Sem soluções reais"))

def main():
    print("Escolha o tipo de equação que deseja calcular:")
    print("1 - Equação do 1º grau (ax + b = 0)")
    print("2 - Equação do 2º grau (ax^2 + bx + c = 0)")

    escolha = input("Digite o número correspondente à sua escolha: ")

    if escolha == "1":
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        print("Solução:", calcular_equacao_1grau(a, b))
    elif escolha == "2":
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        print("Soluções:", calcular_equacao_2grau(a, b, c))
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()