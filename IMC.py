print('--------------------------------')
print('CÓDIGO PARA CALCULAR O IMC')
print('--------------------------------')
nome = (input ("Digite o seu primeiro nome: "))
altura_virgula = float(input ("Digite a sua altura em metros: "))
peso= float(input("Digite o seu peso em quilos: "))
#variaveis que recebem um valor e input para que o valor seja customizável
#float nos valores que serão futuramente utilizados em
#operações em que se usem números com diversas decimais
varIMC = ((peso)/(altura_virgula*altura_virgula))
#imc = peso/altura x altura

linha_1= f'{nome} tem {altura_virgula:.2f} de altura'
linha_2= f'Pesa {peso} quilos e seu IMC é {varIMC:.2f}'
print(linha_1)
print(linha_2)
#fstring =f'{var}
#fstring insere a possibilidade de usar variaveis executaveis em uma string
#controle numero de decimais da variavel = :.varnumf
#varf = f'{var} etc {var:.xf} etc {var} etc'
#print(varf)
if varIMC >24.9:
    print('O seu imc está acima do ideal')
#se o IMC for maior ou igual a 25 o peso está acima do ideal
elif varIMC<18.5:
    print('O seu IMC está abaixo do ideal')
#se o imc for menor ou igual a 18 o peso está abaixo do ideal
else:
    print('O seu IMC está ideal')
#se não for nenhum dos dois casos anteriores, o imc está correto