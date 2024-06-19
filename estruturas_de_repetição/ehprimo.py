# NÚMERO PRIMO

# Recebe a quantidade de testes
N = int(input())

# Executa todos os N testes
for i in range(N):

    # Recebe o número a ser verificado
    X = int(input())

    # Inicializa flag afirmando que o número é primo
    eh_primo = True

    # Caso ele seja divisível por algum número em [2,X-1]
    # então não é primo
    for j in range(2, X):
        if X % j == 0:
            eh_primo = False
            break

    # Printa a resposta com base na flag
    print(f"{X} {'nao ' if not eh_primo else ''}eh primo")
