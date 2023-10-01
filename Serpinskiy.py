def Treug(n):
    sim = ['*']
    for i in range(n):
        sp = '' * (2**i)
        sim = [sp + x + sp for x in sim] + [x + '' + x for x in sim]
        print('\n'.join(sim))

Treug(3)
        