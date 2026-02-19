saldo_inicial = 1000.0
checkpoint = saldo_inicial

print("Checkpoint aponta para o mesmo objeto do saldo_inicial?",
      saldo_inicial is checkpoint)

while True:
    auditor = input("Digite o nome do auditor: ")

    if "*" in auditor or "#" in auditor:
        print("Nome inválido! Não use * ou #")
    else:
        break

saldo_atual = saldo_inicial

for i in range(4):
    valor = float(input(f"Digite o valor da transação {i+1}: "))

    if valor > 500.0:
        print("Transação de alto valor!")

    if valor < 0 and saldo_atual + valor < 0:
        print("Saldo insuficiente! Transação ignorada.")
        continue

    saldo_atual += valor

saldo_final = saldo_atual

print("Resultado: ")
print("Auditor:", auditor)
print("Saldo final:", saldo_final)

print("Saldo final é o mesmo objeto do checkpoint?", saldo_final is checkpoint)

