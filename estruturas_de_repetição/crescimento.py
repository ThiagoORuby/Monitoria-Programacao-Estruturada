# CRESCIMENTO POPULACIONAL

# Recebe o número de casos de teste
T = int(input())

# Para cada caso de teste, resolve o problema
for i in range(T):
    
    # Recebe os valores das populações e suas taxas de crescimento
    PA, PB, G1, G2 = list(map(float, input().split()))
    
    # Inicia a quantidade de anos decorridos com 0
    anos = 0
    while True:
        
        # Realiza o crescimento das populações com base nas taxas
        PA = int(PA + PA*(G1/100))
        PB = int(PB + PB*(G2/100))
        anos += 1
        
        # Se PA superar PB ou se passarem mais de 100 anos
        # para a contagem de tempo 
        if PA > PB:
            break
        elif anos > 100:
            break
        
    
    # Se PA superou PB em no máximo 100 anos, printa a quantidade
    # Senão, printa 'Mais de 1 seculo'
    if PA > PB and anos <= 100:
        print(f"{anos} anos.")
    else:
        print("Mais de 1 seculo.")
