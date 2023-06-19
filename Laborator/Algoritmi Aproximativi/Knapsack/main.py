def sumaMax(S, K):
    sumaMax = 0
    sumePartiale = set([0])
    for Si in S:
        # print('\n', sumePartiale)
        for sumaPartiala in sumePartiale.copy():
            # print(Si, sumaPartiala)
            if Si + sumaPartiala <= K:
                sumaMax = max(sumaMax, Si + sumaPartiala)
                # print(sumaMax)
                sumePartiale.add(Si + sumaPartiala)
    return sumaMax

S = [1, 3, 5, 7, 9]
K = 12
print(sumaMax(S, K))

def sumaMaxAprox(file):
    sumaMax = 0
    K = int(file.readline())
    print(K)
    while True:
        Si = file.readline()
        if Si == '':
            break

        Si = int(Si)
        if Si + sumaMax <= K:
            sumaMax += Si
        elif sumaMax < Si:
            sumaMax = Si
    return sumaMax

file = open('input.txt', 'r')
print(sumaMaxAprox(file))