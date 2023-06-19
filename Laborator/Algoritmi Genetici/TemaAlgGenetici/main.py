import math
import random
import sys

with open("output.txt", "w") as file:
    # sys.stdout = file

    def printPopulatie(C, Cdecoded, fi):
        for i in range(n):
            print(i + 1, ':', C[i], 'x= ', Cdecoded[i], 'f=', fi[i])

    def cautareBinara(x, v):
        st = 0
        dr = len(v) - 1

        while st <= dr:
            m = (st + dr) // 2

            if v[m] <= x <= v[m + 1]:
                return m
            elif v[m] < x:
                st = m + 1
            else:
                dr = m - 1

    def maxFit(c1, c2, c3, fi):
        # print(c1, c2, c3, len(fi), fi[20])
        if max(fi[c1], fi[c2], fi[c3]) == fi[c1]:
            return c1
        elif max(fi[c1], fi[c2], fi[c3]) == fi[c2]:
            return c2
        elif max(fi[c1], fi[c2], fi[c3]) == fi[c3]:
            return c3

    n = int(input())
    st, dr = list(map(int, input().split()))
    a, b, c = list(map(int, input().split()))
    precizie = int(input())
    pIncrucisare = float(input()) / 100
    pMutatie = float(input()) / 100
    nrEtape = int(input())

    l = math.ceil(math.log(((b - a) * math.pow(10, precizie)), 2))
    d = (b - a) / math.pow(2, l)

    print('Populatia initiala')
    Cdecoded = []
    C = []
    fi = []
    for i in range(n):
        x = random.uniform(a, b)
        Cdecoded.append(x)

        nrInterval = math.floor((x - a) / d)
        nrCodificat = format(nrInterval, f'0{l}b')
        C.append(nrCodificat)

        f = a * x ** 2 + b * x + c
        fi.append(f)

        print(i + 1, ':', nrCodificat, 'x=', x, 'f=', f)

    boolPrint = True
    best = []
    while nrEtape:
        ps = [fi[i] / sum(fi) for i in range(n)]
        if boolPrint:
            print('\nProbabilitati selectie')
            for i in range(n):
                print('cromozom', i + 1, 'probabilitate', ps[i])

        pi = [sum(fi[:i]) / sum(fi) for i in range(n + 1)]
        if boolPrint:
            print('\nIntervale probabilitati selectie')
            print(pi)

        select = best
        if boolPrint:
            idxStart = 0
        else:
            idxStart = 3

        # metoda ruletei
        # for i in range(idxStart, n):
        #     u = random.uniform(0, 1)
        #     nrInterval = cautareBinara(u, pi)
        #     select.append(nrInterval)
        #
        #     if boolPrint:
        #         print('u=', u, 'selectam cromozomul', nrInterval + 1)

        # task
        for i in range(idxStart, n):
            idxC = maxFit(random.randint(3, n-1), random.randint(3, n-1), random.randint(3, n-1), fi)
            # print('ok')
            select.append(idxC)

            # if boolPrint:
                # print('u=', u, 'selectam cromozomul', nrInterval + 1)

        C = [C[i] for i in select]
        Cdecoded = [Cdecoded[i] for i in select]
        fi = [fi[i] for i in select]

        if boolPrint:
            print('\nDupa selectie:')
            printPopulatie(C, Cdecoded, fi)

            print('\nProbabilitatea de incrucisare:', pIncrucisare)
        recomb = []
        for i in range(3, n):
            u = random.uniform(0, 1)
            if u < pIncrucisare:
                recomb.append(i)

                if boolPrint:
                    print(i + 1, ':', C[i], 'u=', u, '< 0.25 participa')

            else:
                if boolPrint:
                    print(i + 1, ':', C[i], 'u=', u)

        for i in range(0, len(recomb) - 1, 2):
            pRupere = random.randint(0, l)

            if boolPrint:
                print('\nRecombinare dintre cromozomul', recomb[i] + 1, 'cu cromozomul', recomb[i + 1] + 1, ':')
                print(C[recomb[i]])
                print(C[recomb[i + 1]])

                print('Punct', pRupere)
                print('Rezultat')

            c1 = C[recomb[i]][:pRupere] + C[recomb[i + 1]][pRupere:]
            C[recomb[i]] = c1

            x = a + int(c1, 2) * d
            Cdecoded[recomb[i]] = x

            f = a * x ** 2 + b * x + c
            fi[recomb[i]] = f

            c2 = C[recomb[i + 1]][:pRupere] + C[recomb[i]][pRupere:]
            C[recomb[i + 1]] = c2

            x = a + int(c2, 2) * d
            Cdecoded[recomb[i]] = x

            f = a * x ** 2 + b * x + c
            fi[recomb[i]] = f

            if boolPrint:
                print(c1)
                print(c2)

        if boolPrint:
            print('\nDupa recombinare:')
            printPopulatie(C, Cdecoded, fi)

            print('\nProbabilitate de mutatie pentru fiecare gena', pMutatie)
        mut = []
        for i in range(3, n):
            C[i] = list(C[i])
            ok = False
            for j in range(l):
                u = random.uniform(0, 1)
                if u < pMutatie:
                    if C[i][j] == '0':
                        C[i][j] = '1'
                    else:
                        C[i][j] = '0'

                    ok = True
            if ok:
                mut.append(i + 1)

            C[i] = ''.join(C[i])

            x = a + int(C[i], 2) * d
            Cdecoded[i] = x

            f = a * x ** 2 + b * x + c
            fi[i] = f

        if boolPrint:
            print('Au fost modificati cromozomii:')
            print(mut)

            print('\nDupa mutatie:')
            printPopulatie(C, Cdecoded, fi)

            print('\nEvolutia maximului')

        fiCopy = fi[:]
        best = []
        for i in range(3):
            idx = fiCopy.index(max(fiCopy))
            best.append(idx)
            fiCopy[idx] = 0

        print('Max Fitness', max(fi), 'Mean Fitness', sum(fi) / n)

        boolPrint = False
        nrEtape -= 1