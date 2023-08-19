menu=

[s] Sacar
[e] Extrato 
[d]Depositar
[q]Sair

>...
saldo=0
limite=500
extrato=--
numero_saques=0
Limite_Saques=3

While True:
opcao=input(menu)

If opcao =="d":
valor= float(input("informe o valor do deposito:"))

If valor >0:
saldo += valor
extrato +=f"Deposito: R${valor:.2f}\n"

else:
print("Operação falhou! O valor informado é inválido.")

elif opcao=="s"
valor= float(input("Informe o valor do saque:"))

excedeu_saldo= valor>saldo
excedeu_limite= valor>limite 
excedeu_saques= numero_saques >=Limite_Saque

If excedeu_saldo:
print("Operação falhou! Você não tem saldo suficiente.")

elif excedeu_limite:
print("Operação falhou!O valor do saque excede o limite.")

elif excedeu_saques :
print("Operação falhou! Número máximo de saques excedido.")

elif valor >0
saldo -=valor
extrato += f"Saque: R${valor:.2f}\n"
nunero_saques += 1

else:
print(Operação falhou! O valor informado é inválido)

elif opcao =="e":
print("\n********Extrato*******")
print("Não foram realizadas movimentações." if not extrato else extrato)
print(f"/n Saldo: R$(saldo:.2f)")
print("*******")

elif opcao=="q"
break

else:
print("Operação inválida, por favor selecione novamente a operação desejada.")
