from random import choice

trocouganhou = 0
trocouperdeu = 0
manteveganhou = 0
manteveperdeu = 0

for x in range(200):
    portas = ['porta 1','porta 2','porta 3']
    premio = choice(portas)
    print('Round', x+1, '- Escolha o número de sua porta:')
    escolha1 = int(choice([0,1,2]))
    del(portas[escolha1])
    if premio in portas:
        trocar = premio
        portas.remove(premio)
        portaaberta = portas[0]
    else:
        trocar = choice(portas)
        portas.remove(trocar)
        portaaberta = portas[0]
    portas = ['porta 1','porta 2','porta 3']
    print("------------------------------------")
    print("Você escolheu a", portas[escolha1])
    print("A", portaaberta, "foi aberta")
    print("Deseja trocar para a", trocar, "? (sim/nao)")
    escolha2 = choice(['sim','nao'])
    if escolha2 == 'sim':
        portafinal = trocar
        escolheutrocar = True
    else:
        portafinal = portas[escolha1]
        escolheutrocar = False
    if portafinal == premio:
        print("------------------------------------")
        print("Você ganhou! De fato, prêmio estava atrás da ", premio)
        if escolheutrocar == True:
            trocouganhou += 1
        else:
            manteveganhou += 1
    else:
        print("------------------------------------")
        print("Você perdeu, o prêmio estava atrás da", premio)
        if escolheutrocar == True:
            trocouperdeu += 1
        else:
            manteveperdeu += 1
    print("------------------------------------")
    print("Trocou e ganhou = ", trocouganhou)
    print("Trocou e perdeu = ", trocouperdeu)
    print("Manteve e ganhou = ", manteveganhou)
    print("Manteve e perdeu = ", manteveperdeu)
    print("------------------------------------")

print("Se trocou, ganhou", round((trocouganhou/(trocouganhou+trocouperdeu))*100,2), "% das vezes")
print("Se manteve, ganhou", round((manteveganhou/(manteveganhou+manteveperdeu))*100,2), "% das vezes")