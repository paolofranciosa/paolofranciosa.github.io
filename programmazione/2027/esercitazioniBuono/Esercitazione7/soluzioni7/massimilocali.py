def massimilocali(sequenza):
    if not isinstance(sequenza, list):
        raise TypeError
    massimi = []
    for i in range(1, len(sequenza) - 1):
        if sequenza[i - 1] < sequenza[i] and sequenza[i] > sequenza[i + 1]:
            massimi.append(sequenza[i])
    return massimi

