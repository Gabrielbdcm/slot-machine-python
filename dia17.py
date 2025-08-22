import random
import time

saldo = 100
emojis = ["🍒", "🍋", "🍉", "⭐", "🔔"]

while saldo > 0:
    contagem = 0
    while contagem < 1:
        print("saldo insuficiente")
        aposta = int(input("Você tem R$" + str(saldo) + ". Quanto deseja apostar? "))
        if aposta < saldo:
            contagem = 10
    if aposta > 70:
        sorte = 2
    elif aposta > 50:
        sorte = 3
    elif aposta > 15:
        sorte = 4
    else:
        sorte = 5

    input("Pressione ENTER para girar a roleta...")

    # Animação da roleta
    for _ in range(15):  # número de giros
        giro = [random.choice(emojis) for _ in range(3)]
        print(" ".join(giro), end="\r")
        time.sleep(0.1)  # delay

   
    if random.randint(1,10) <= sorte: #se o numero sorteado for menor q a sorte
        resultado = [random.choice(emojis)] * 3 
    else:
        resultado = [random.choice(emojis) for _ in range(3)]  

    print("Resultado final:" + " ".join(resultado)) #exibe como string

    if resultado[0] == resultado[1] == resultado[2]:
        print("🎉 Você ganhou!")
        saldo += aposta
    else:
        print("❌ Você perdeu!")
        saldo -= aposta

print("💀 Seu saldo acabou!")
