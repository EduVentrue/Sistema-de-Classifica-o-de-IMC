#Projeto Sistema de Classificação de IMC

print("Olá, vamos calcular seu IMC?")
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"{nome}, seu IMC é {imc:.2f} e você está abaixo do peso normal. Procure um profissional da saúde para uma avaliação.")
elif imc >= 18.5 and imc <= 24.9:
    print(f"{nome}, seu IMC é {imc:.2f} e você está com o peso normal.")
elif imc >= 25 and imc <= 29.9:
    print(f"{nome}, seu IMC é {imc:.2f} e você está com sobrepeso.")
else:
    print(f"{nome}, seu IMC é {imc:.2f} e você está com obesidade.")
    print("Você precisa procurar um profissional da saúde para uma consulta.")

    