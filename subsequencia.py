teste = input().split()
tam1 = int(teste[0])
tam2 = int(teste[1])
mmamatriz = input().split()
M1 = []
for i in range(len(mmamatriz)):
    M1.append(int(mmamatriz[i]))
#print(M1)
mamama = input().split()
M2 = []
for i in range(len(mamama)):
    M2.append(int(mamama[i]))
#print(M2)
count = 0
for j in range(len(M2)):
    if not (M2[j] in M1):
        print(count)
        count +=1
#print("Count depois do not", count)
for i in range(tam2):
    if i != tam2-1:
        if M2[i]>M2[i+1]:
            count+=1
if count > 0:
    print("N")
else:
    print("S")