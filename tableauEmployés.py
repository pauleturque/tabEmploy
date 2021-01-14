# programme tableau identifiants employés
# 14/1/21
# Paulinette

N = 3

def Commune(x):
    i = 0
    T = [["Paris", "1"], ["Lyon", "2"], ["Marseille", "3"], ["Toulouse", "4"], ["Bordeaux", "5"]]
    while T[i][0] != x:
        i += 1
    return T[i][1]

def Conversion(number):
    ref = str(number)
    while len(ref) < 3:
        ref = "0" + ref
    return ref

def Identifiants(Listing):
    print("N dans Identifiants =", N)
    for k in range(N):
        id = (Listing[k][0])[:1]
        if Listing[k][1] == "femme":
            id += "2"
        else:
            id += "1"
        id += (Listing[k][2])[2:]
        id += Commune(Listing[k][3])
        id += Conversion(k+1)
        Listing[k][4] = id

def Ajout_Cle(identifiant):
    val = int(identifiant[1:])
    s = 0
    while val > 0:
        s += val % 10
        val = val // 10
    cle = (66 - s) % 11
    if cle == 10:
        identifiant += "X"
    else:
        identifiant += str(cle)
    return identifiant

Tab = [["DUPONT", "homme", "1981", "Paris", "0"], ["ARTHUR", "femme", "1980", "Bordeaux", "0"], ["AZERTY", "femme", "1979", "Toulouse", "0"]]

Identifiants(Tab)
print(Tab)

for k in range(N):
    Tab[k][4] = Ajout_Cle(Tab[k][4])

print(Tab)
