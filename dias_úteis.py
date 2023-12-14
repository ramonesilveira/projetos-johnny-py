from datetime import datetime, timedelta
import holidays

escolha = input("Digite 'M' para calcular os dias úteis de um mês ou 'A' para calcular os dias úteis de todos os meses de um ano: ")

if escolha.upper() == 'A':
    # Código para calcular os dias úteis de todos os meses de um ano
    feriados_br = holidays.Brazil()  # Defina os feriados nacionais do Brasil

    ano = input("Digite o ano (exemplo: 2024): ")
    if ano.isdigit():  # Verifica se é um número
        ano = int(ano)

        for mes in range(1, 13):
            # Determine o primeiro dia e último dia do mês
            primeiro_dia = datetime(ano, mes, 1)
            ultimo_dia = datetime(ano, mes % 12 + 1, 1) if mes < 12 else datetime(ano + 1, 1, 1)
            ultimo_dia -= timedelta(days=1)
            
            # Converta as datas para objetos datetime
            primeiro_dia = datetime.combine(primeiro_dia, datetime.min.time())
            ultimo_dia = datetime.combine(ultimo_dia, datetime.max.time())

            # Gere as datas para o intervalo
            dates = (primeiro_dia + timedelta(idx) for idx in range((ultimo_dia - primeiro_dia).days + 1))

            # Conte os dias úteis excluindo os feriados e registre os feriados
            res = sum(1 for day in dates if day.weekday() < 5 and day not in feriados_br)

            # Imprima o total de dias úteis no intervalo
            print(f"Total de dias úteis no mês {mes}/{ano}: {res}")

            # Obtenha os feriados do mês
            feriados_mes = [(date.strftime('%d/%m/%Y'), name) for date, name in feriados_br.items() if primeiro_dia.date() <= date <= ultimo_dia.date()]

            # Imprima os feriados do mês com a data
            print("Feriados do mês:")
            for data, feriado in feriados_mes:
                print(f"{feriado} - {data}")
            print()

    else:
        print("Ano inválido. Digite um número válido.")

elif escolha.upper() == 'M':
    # Código para calcular os dias úteis de um mês
    feriados_br = holidays.Brazil()  # Defina os feriados nacionais do Brasil

    ano = input("Digite o ano (exemplo: 2024): ")
    if ano.isdigit():  # Verifica se é um número
        ano = int(ano)

        mes = int(input("Digite o mês (exemplo: 1 para janeiro): "))
        if 1 <= mes <= 12:
            # Determine o primeiro dia e último dia do mês
            primeiro_dia = datetime(ano, mes, 1)
            ultimo_dia = datetime(ano, mes % 12 + 1, 1) if mes < 12 else datetime(ano + 1, 1, 1)
            ultimo_dia -= timedelta(days=1)
            
            # Converta as datas para objetos datetime
            primeiro_dia = datetime.combine(primeiro_dia, datetime.min.time())
            ultimo_dia = datetime.combine(ultimo_dia, datetime.max.time())

            # Gere as datas para o intervalo
            dates = (primeiro_dia + timedelta(idx) for idx in range((ultimo_dia - primeiro_dia).days + 1))

            # Conte os dias úteis excluindo os feriados e registre os feriados
            res = sum(1 for day in dates if day.weekday() < 5 and day not in feriados_br)

            # Imprima o total de dias úteis no intervalo
            print("Total de dias úteis no mês : " + str(res))

            # Obtenha os feriados do mês
            feriados_mes = [(date.strftime('%d/%m/%Y'), name) for date, name in feriados_br.items() if primeiro_dia.date() <= date <= ultimo_dia.date()]

            # Imprima os feriados do mês com a data
            print("Feriados do mês:")
            for data, feriado in feriados_mes:
                print(f"{feriado} - {data}")
        else:
            print("Mês inválido. Digite um número de 1 a 12.")
    else:
        print("Ano inválido. Digite um número válido.")

else:
    print("Escolha inválida.")
