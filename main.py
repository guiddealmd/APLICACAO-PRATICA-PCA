import random

def gera_pergunta():
    operador = random.choice(['+', '-'])
    num1 = random.randint(1, 10)  # Correção: "randint" ao invés de "randit"
    num2 = random.randint(1, 10)  # Correção: "randint" ao invés de "randit"

    if operador == '-':
        # Certifique-se de que a subtração não resulta em números negativos
        num1, num2 = max(num1, num2), min(num1, num2)

    pergunta = f"{num1} {operador} {num2}"
    resposta_correta = eval(pergunta)  # Correção: "resposta_correta" ao invés de "resposta"

    return pergunta, resposta_correta

def jogo():
    pontuacao = 0
    num_perguntas = 10  # Número de perguntas a serem feitas
    print("Bem-vindo ao Jogo de Matemática!")

    for _ in range(num_perguntas):
        pergunta, resposta_correta = gera_pergunta()
        print(f"\nPergunta: {pergunta}")
        resposta_usuario = int(input("Sua resposta: "))

        if resposta_usuario == resposta_correta:
            print("Resposta correta! +1 ponto\n")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta era: {resposta_correta}\n")

    print(f"Fim do jogo! Sua pontuação final é: {pontuacao}")

if __name__ == "__main__":
    jogo()
