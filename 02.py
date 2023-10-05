def calcular_abono(salario_bruto):
    abono = salario_bruto * 0.2
    if abono < 100:
        return 100
    else:
        return abono

def main():
    salarios_brutos = []
    while True:
        salario_bruto = float(input("Salário bruto de dezembro: "))
        if salario_bruto == 0:
            break
        salarios_brutos.append(salario_bruto)

    total_de_funcionarios = len(salarios_brutos)
    total_gasto_com_abonos = 0
    numero_de_funcionarios_com_abono_minimo = 0
    maior_valor_pago_como_abono = 0

    print("Salário Bruto - Abono")
    for salario_bruto in salarios_brutos:
        abono = calcular_abono(salario_bruto)
        total_gasto_com_abonos += abono
        if abono == 100:
            numero_de_funcionarios_com_abono_minimo += 1
        if abono > maior_valor_pago_como_abono:
            maior_valor_pago_como_abono = abono

        print(f"R$ {salario_bruto:.2f} - R$ {abono:.2f}")

    print("\nForam processados", total_de_funcionarios, "colaboradores")
    print("Total gasto com abonos: R$", format(total_gasto_com_abonos, '.2f'))
    print("Valor mínimo pago a", numero_de_funcionarios_com_abono_minimo, "colaboradores")
    print("Maior valor de abono pago: R$", format(maior_valor_pago_como_abono, '.2f'))

if __name__ == "__main__":
    main()