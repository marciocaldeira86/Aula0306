# numero = 7

# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Impar")

idade = int(input("Digite sua Idade: ")) 
if idade >= 18:
    print("Adulto")
elif idade < 18 and idade >= 14:
    print("adolecente")
else:
    print("Criança")