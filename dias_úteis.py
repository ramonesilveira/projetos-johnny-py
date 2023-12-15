from datetime import datetime, timedelta
import holidays
import calendar

def calcular_dias_uteis(ano, mes=None):
    feriados_br = holidays.Brazil()

    # Feriados do Rio Grande do Sul
    feriados_rs = [
        (datetime(ano, 9, 20), "Revolução Farroupilha"),
        # Adicione os feriados do RS desejados seguindo o formato (datetime(ano, mês, dia), "Nome do Feriado")
    ]

    if mes is None:
        opcao = input("Digite 'A' para o ano inteiro ou 'M' para um mês específico: ").upper()

        if opcao == 'A':
            for mes in range(1, 13):
                calcular_mes(feriados_br, feriados_rs, ano, mes)
        elif opcao == 'M':
            mes = int(input("Digite o número do mês (exemplo: 1 para janeiro): "))
            calcular_mes(feriados_br, feriados_rs, ano, mes)
        else:
            print("Opção inválida.")
    else:
        calcular_mes(feriados_br, feriados_rs, ano, mes)

def calcular_mes(feriados_br, feriados_rs, ano, mes):
    primeiro_dia = datetime(ano, mes, 1)
    ultimo_dia = datetime(ano, mes % 12 + 1, 1) if mes < 12 else datetime(ano + 1, 1, 1)
    ultimo_dia -= timedelta(days=1)

    cal = calendar.monthcalendar(ano, mes)
    dias_semana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']

    print(f"Para o mês {mes}/{ano}:")
    print("O intervalo original : " + str(primeiro_dia.date()) + " " + str(ultimo_dia.date()))

    for dia in dias_semana:
        print(f"{dia:^4}", end=' ')
    print()

    for week in cal:
        for day in week:
            if day != 0:
                current_date = datetime(ano, mes, day)
                if current_date.weekday() >= 5:  # Fim de semana
                    print('\033[94m' + f"{day:<4}", end=' ')
                elif current_date in feriados_br or current_date.weekday() == 6 or any(date.date() == current_date.date() for date, _ in feriados_rs):  # Feriado
                    print('\033[91m' + f"{day:<4}", end=' ')
                else:  # Dias úteis
                    print('\033[92m' + f"{day:<4}", end=' ')
            else:
                print(" " * 4, end=' ')
        print()

    res = sum(1 for day in range(1, ultimo_dia.day + 1)
              if datetime(ano, mes, day).weekday() < 5 and datetime(ano, mes, day) not in feriados_br)
    print("\033[90mTotal de dias úteis no mês : " + str(res))

    feriados_mes = [(date.strftime('%d/%m/%Y'), name) for date, name in feriados_br.items() if
                    primeiro_dia.date() <= date <= ultimo_dia.date()]
    feriados_mes += [(date.strftime('%d/%m/%Y'), name) for date, name in feriados_rs if primeiro_dia.date() <= date.date() <= ultimo_dia.date()]
    
    print("\033[90mFeriados do mês:")
    for data, feriado in feriados_mes:
        print(f"{feriado} - {data}")

    print()

ano = int(input("Digite o ano (exemplo: 2024): "))
calcular_dias_uteis(ano)
