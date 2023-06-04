'''
Criei esse espacinho pra falar do código.
Ele ta cheio de print em cada coisinha que ele faz, já
que eu tava testando ele.
Caso queira sumir com os prints, mas vai usar eles
depois pra verificar como o código funciona,
tira e coloca o # (famoso comentario) antes deles,
é o jeito mais eficiente de fazer isso.

Boa sorte ao ler o código, qualquer dúvida pode perguntar!
'''
Matr = []
vendas = 0
MN = input("N° Linhas e colunas (separadas com espaço): ").split()
M = int(MN[0])
N = int(MN[1])
print("Linhas totais: ", M) # pode comentar esse
print("Colunas totais: ", N) # esse tbm

for i in range(M):
    linha = []
    roupa = input().split()
    print("Linha atual: ", i+1)
    for j in range(N):
        linha.append(int(roupa[j]))
    print("Sua linha é: ", linha)
    Matr.append(linha)
print("Sua matriz: ", Matr) #printa como é a sua matriz final.

P = int(input("Quantidade de tentativas de compra: "))
for i in range(P):
    IJ = input("Insira a coordenada da compra (com espaço entre os números): ").split() #Explicando: Essa parte pega a "coordenada" da compra,
    I = int(IJ[0]) #Primeira coordenada é o I
    J = int(IJ[1]) #Segunda coordenada é o J

    #Porém é necessário diminuir as duas em 1, já que é como
    #se um cliente normal estivesse selecionando a coordenada normal,
    #e não uma em índices.
    
    try: #Esse try verifica se a coordenada ta dentro da matriz, caso não esteja, o código da linha 50 faz continuar.
        #É necessário verificar se a coordenada existe no estoque
        if Matr[I-1][J-1] != 0:
            Matr[I-1][J-1] -= 1
            vendas+=1
        else:
            print("Estoque referente a essa coordenada vazio. Faça outra compra.")
        print(Matr) #pode comentar
    except IndexError: #Se a coordenada não existir
        print("Coordenada não existente, tente novamente.")
        continue #o programa continua para o próximo i do range(P) na linha 29
print(vendas)
