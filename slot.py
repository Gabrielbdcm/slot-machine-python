import random
import time

saldo = 100
emojis = ["🍒", "🍋", "🍉", "⭐", "🔔"]

while saldo > 0:
    print(f"\n💰 Saldo atual: R${saldo}")
    
    aposta = int(input("Quanto deseja apostar? "))

    if aposta > saldo or aposta <= 0:
        print("❌ Aposta inválida!")
        continue

    # Define sorte (chance de ganhar)
    if aposta > 70:
        sorte = 2
    elif aposta > 50:
        sorte = 3
    elif aposta > 15:
        sorte = 4
    else:
        sorte = 5

    input("Pressione ENTER para girar a roleta...")

    #  Animação
    for _ in range(15):
        giro = [random.choice(emojis) for _ in range(3)]
        print(" ".join(giro), end="\r")
        time.sleep(0.1)

    # Resultado
    if random.randint(1, 10) <= sorte:
        resultado = [random.choice(emojis)] * 3
    else:
        resultado = [random.choice(emojis) for _ in range(3)]

    print("\nResultado final:", " ".join(resultado))

    #  Verificação
    if resultado[0] == resultado[1] == resultado[2]:
        print("🎉 Você ganhou!")
        saldo += aposta
    else:
        print("❌ Você perdeu!")
        saldo -= aposta
print("💀 Seu saldo acabou!")        
input("Pressione ENTER para sair")
