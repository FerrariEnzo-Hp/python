import math
from rich import print
from rich.table import Table
def bask (a, b, c):
    delta = (b)**2-(4*a*c)
    if delta > 0:
        x1 = round((-b+math.sqrt(delta))/(2*a), 2)
        x2 = round((-b-math.sqrt(delta))/(2*a), 2)
        print(f'raiz1 = {x1} e raiz2 = {x2}')
    elif delta == 0:
        x = round((-b)/(2*a), 2)
        print(f'Equação com apenas uma raiz igual a {x}')
    else:
        ang_simbol = '\u2220'
        divider = 2*a
        new_delta = abs(delta)
        delta_result = round(math.sqrt(new_delta)/(divider), 2)
        delta_negative_result = round(-delta_result, 2)
        b_division = -b/divider
        b_result = round(b_division, 2)
        z_modulus = round(math.sqrt((b_result**2)+delta_result**2), 2)
        teta_deg1 = round(math.degrees(math.atan(delta_result/b_result)), 2)
        teta_deg2 = round(math.degrees(math.atan(delta_negative_result/b_result)), 2)

        tabela = Table(title="Resultado", style="Red")
        tabela.add_column('forma Retangular:')
        tabela.add_column('forma polar:')
        tabela.add_row(f'x1 = {b_result} + {delta_result}i', f'x1 = {z_modulus}{ang_simbol}{teta_deg1}')
        tabela.add_row(f'x2 = {b_result} - {delta_result}i', f'x2 = {z_modulus}{ang_simbol}{teta_deg2}')
        print(tabela)

bask(4, -10, 78)