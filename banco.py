class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def imprimir_saldo(self):
        print(f"Saldo da conta de {self.__titular}: R${self.__saldo:.2f}")


def main():
    titular = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    
    # Criando a conta bancária com os dados informados pelo usuário
    conta = ContaBancaria(titular, saldo_inicial)
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver saldo")
        print("4. Sair")
        
        opcao = input("Opção escolhida: ")
        
        if opcao == '1':
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
        elif opcao == '2':
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_saque)
        elif opcao == '3':
            conta.imprimir_saldo()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()