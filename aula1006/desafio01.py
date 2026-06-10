# criar um programa que leia uma variavel nota com input e mostre na tela:
# > 90 "Conceito A"
# entre 89 e 71 "Conceito B"
# entre 70 e 61 "Conceito C"
# entre 60 e 50 "Conceito B"
# < 49 "conceito E"



while True:
    nota = int(input("Digite a nota: "))
    if nota >= 90:
        print("Conceito A")
    elif nota <= 89 and nota >= 71:
        print("Conceito B")
    elif nota <= 70 and nota >= 61:
        print("Conceito C")
    elif nota <=60 and nota >= 50:
        print("Conceito D")
    else:
        print("Conceito E")
    
    if nota == 0:
        break


    # segundo exemplo
    temperatura = float(input("Digite a Temperatura atual:"))
    if temperatura > 40.1:
        print("voce esta com febre")
    elif temperatura <= 40.1 and temperatura >= 38.9:
        print("Voce esta com febricula")
    elif temperatura <= 40.1 and temperatura >= 37.0:
        print("temperatura quase normal")
    elif temperatura <= 40.1 and temperatura >= 34.9:
        print("temperatura normal")
    elif temperatura <= 40.1 and temperatura >= 32.9:
        print("pre hipotermia")
    elif temperatura <= 40.1 and temperatura >= 29.9:
        print("hipotermia")
    else:
        print("R.I.P")
