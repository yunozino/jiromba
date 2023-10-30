#programa que fala estação por numero do mês e dia

print = ('qual a estação do ano?')
dia = int (input('dia:\n'))
mes = int (input('mes:\n'))

def estacao (mes):
    if mes in [1,2]:
        return 'verao'
    elif mes== 3:
        if dia < 20:
            return 'verao'
        else:
            return 'outono'
    elif mes in [4,5]:
        return 'outono'
    elif mes == 6:
        if dia < 21:
            return 'outono'
        else:
            return 'inverno'
    elif mes in [7,8]:
        return 'inverno'
    elif mes == 9:
        if dia < 23:
            return 'inverno'
    else:
        return 'primavera'
    elif mes in {10, 11}:
        return 'primavera'
    elif 12 == mes:
        if 22 > dia:
            return 'primavera'
    else:
        return 'verao'

resul = estacao(dia, mes)
print(resul)