def binario_para_decimal():
    bin = input("Digite o número binário: ")
    dec = int(bin, 2)
    print("O valor decimal de {} é {}".format(bin, dec))

def hexadecimal_para_decimal():
    hex = input("Digite o número em hexadecimal: ")
    dec = int(hex, 16)
    print("O valor decimal de {} é {}".format(hex, dec))

def octal_para_decimal():
    oct = input("Digite o número em octal: ")
    dec = int(oct, 8)
    print("O valor decimal de {} é {}".format(oct, dec))

while True:
    print("\nEscolha uma operação:")
    print("1. Conversão de binário para decimal")
    print("2. Conversão de hexadecimal para decimal")
    print("3. Conversão de octal para decimal")
    print("4. Sair")

    opcao = input("Digite o número da operação desejada: ")

    if opcao == '1':
        binario_para_decimal()
    elif opcao == '2':
        hexadecimal_para_decimal()
    elif opcao == '3':
        octal_para_decimal()
    elif opcao == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")