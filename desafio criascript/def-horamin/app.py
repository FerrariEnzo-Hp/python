def horasec(hh, mm, ss):
    horas = (hh*60)*60
    mins = mm*60

    total = mins+horas+ss
    print(f"{hh}horas, {mm}minutos e {ss}segundos são iguais a {total}segundos")
    return total

try:
    horasec(16, 4, 33)
except:
    print('algo deu errado')