import this


def exercicio01():
    A = 10
    B = 20
    msg = 'antes da troca A = {}, B = {}'.format(A,B)
    aux = A
    A = B
    B = aux
    msg = msg +'\nDepois da troca: A= {}, B = {}'.format(A,B)
    return msg

def exercicio02():
    print('digite o numero que voce deseja saber o antecessor')
    this.num3 = int(input())#entrada de dados
    print('o antecessor é {}'.format(this.num3 - 1))
    msgs = 'obrigado'
    return msgs

def exercicio03():
    print('digite o valor da base:')
    this.base = float(input())
    print('digite o valor da altura:')
    this.altura = float(input())

    #validaçao:
    if this.base < 0:
        return 'seu numero não é positivo!!!'
    if this.altura < 0:
        return 'seu numero não é positivo!!!'
    else:
        print('o valor da area do seu retangulozinho é de {}'.format(this.base*this.altura))
        msgs = 'obrigado'
        return msgs

def exercicio04():
    print('escreva sua idade em anos, meses e dias.')
    print('anos:')
    this.ano = int(input())
    print('meses:')
    this.mes = int(input())
    print('dias:')
    this.dia = int(input())
    print('sua idade em dias é {}'.format(this.ano * 365 + this.mes * 30 + this.dia))
    msgs = 'obrigado'
    return msgs

def exercicio05():
    print('total de votos válidos:')
    this.valido = int(input())
    print('total de votos em branco:')
    this.branco = int(input())
    print('total de votos nulos:')
    this.nulo = int(input())
    total = this.valido + this.nulo + this.branco
    totalV = this.valido / total
    totalB = this.branco / total
    totalN = this.nulo / total
    print('total de eleitores: {}'.format(total))
    print('percentual de votos válidos: {}%'.format(totalV * 100))
    print('percentual de votos em branco: {}%'.format(totalB * 100))
    print('percentual de votos nulos: {}%'.format(totalN * 100))
    msgs = 'obrigado'
    return msgs

def exercicio06():
    print('digite seu salário mensal atual:')
    salario = float(input())
    print('digite o percentual do reajuste:')
    print('favor nao digitar %')
    reajuste = float(input())
    salarioR = reajuste / 100 * salario
    print('seu salário com o reajuste é de R$ {}'.format(salarioR + salario))
    msgs = 'obrigado'
    return msgs

def exercicio07():
    print('digite o valor do custo de fabrica do carro:')
    fabrica = float(input())
    valor = fabrica + fabrica * 0.28 + fabrica * 0.45
    print('o custo final ao conasummidor é de R$ {}'.format(valor))
    msgs = 'obrigado'
    return msgs

def exercicio08():
    print('digite a priemieira nota:')
    nota1 = float(input())
    print('digite a segunda nota:')
    nota2 = float(input())
    print('digite a terceira nota:')
    nota3 = float(input())
    media = (nota1 + nota2 + nota3) / 3
    print('a media entre as três notas é de {}'.format(media))
    msgs = 'obrigado'
    return msgs

def exercicio09():
    print('quantidade de maçãs compradas:')
    maca = int(input())
    if maca <= 11:
        valor = 1.30
    else:
        valor = 1
    print('valor total: R$ {}'.format(maca * valor))
    msgs = 'obrigado'
    return msgs

def exercicio10():
    valor0 = 0
    print('valor 1')
    valor1 = bool(input())
    print('valor 2')
    valor2 = bool(input())
    print('valor 3')
    valor3 = bool(input())
    print('valor 4')
    valor4 = bool(input())
    print('valor 5')
    valor5 = bool(input())
    print('valor 6')
    valor6 = bool(input())
    print('valor 7')
    valor7 = bool(input())
    print('valor 8')
    valor8 = bool(input())
    print('valor 9')
    valor9 = bool(input())
    print('valor 10')
    valor10 = bool(input())

def exercicio12():

    debt = float
    credit = float

    print('digite seu SALDO:')
    sald = float(input())

    print('digite seu DEBITO:')
    debt = float(input())

    print('digite seu CREDITO:')
    credit = float(input())

    resp = sald - debt + credit

    print('seu saldo atual é {}'.format(resp));

    if resp >= 0:
        print('parabens seu saldo é positivo :)')
    elif resp < 0:
        print('vishhh seu saldo ta negativo :(');

    msgs = 'obrigado'
    return msgs

def exercicio13():
    print('digite um valor de 1 a 10:')
    val = int(input())

    if val < 1:
        print('o valor tem que estar entre 1 e 10')

    elif val > 10:
        print('o valor tem que estar entre 1 e 10')

    elif val == 1:
        print('1x0 = 0')
        print('1x1 = 1')
        print('1x2 = 2')
        print('1x3 = 3')
        print('1x4 = 4')
        print('1x5 = 5')
        print('1x6 = 6')
        print('1x7 = 7')
        print('1x8 = 8')
        print('1x9 = 9')
        print('1x10 = 10')
    elif val == 2:
        print('2x0 = 0')
        print('2x1 = 2')
        print('2x2 = 4')
        print('2x3 = 6')
        print('2x4 = 8')
        print('2x5 = 10')
        print('2x6 = 12')
        print('2x7 = 14')
        print('2x8 = 16')
        print('2x9 = 18')
        print('2x10 = 20')
    elif val == 3:
        print('3x0 = 0')
        print('3x1 = 3')
        print('3x2 = 6')
        print('3x3 = 9')
        print('3x4 = 10')
        print('3x5 = 15')
        print('3x6 = 18')
        print('3x7 = 21')
        print('3x8 = 24')
        print('3x9 = 27')
        print('3x10 = 30')
    elif val == 4:
        print('4x0 = 0')
        print('4x1 = 4')
        print('4x2 = 8')
        print('4x3 = 12')
        print('4x4 = 16')
        print('4x5 = 20')
        print('4x6 = 24')
        print('4x7 = 28')
        print('4x8 = 32')
        print('4x9 = 36')
        print('4x10 = 40')
    elif val == 5:
        print('5x0 = 0')
        print('5x1 = 5')
        print('5x2 = 10')
        print('5x3 = 15')
        print('5x4 = 20')
        print('5x5 = 25')
        print('5x6 = 30')
        print('5x7 = 35')
        print('5x8 = 40')
        print('5x9 = 45')
        print('5x10 = 50')
    elif val == 6:
        print('6x0 = 0')
        print('6x1 = 6')
        print('6x2 = 12')
        print('6x3 = 18')
        print('6x4 = 24')
        print('6x5 = 30')
        print('6x6 = 36')
        print('6x7 = 42')
        print('6x8 = 48')
        print('6x9 = 54')
        print('6x10 = 60')
    elif val == 7:
        print('7x0 = 0')
        print('7x1 = 7')
        print('7x2 = 14')
        print('7x3 = 21')
        print('7x4 = 28')
        print('7x5 = 35')
        print('7x6 = 42')
        print('7x7 = 49')
        print('7x8 = 56')
        print('7x9 = 63')
        print('7x10 = 70')
    elif val == 8:
        print('8x0 = 0')
        print('8x1 = 8')
        print('8x2 = 16')
        print('8x3 = 24')
        print('8x4 = 32')
        print('8x5 = 40')
        print('8x6 = 48')
        print('8x7 = 56')
        print('8x8 = 64')
        print('8x9 = 72')
        print('8x10 = 80')
    elif val == 9:
        print('9x0 = 0')
        print('9x1 = 9')
        print('9x2 = 18')
        print('9x3 = 27')
        print('9x4 = 36')
        print('9x5 = 45')
        print('9x6 = 54')
        print('9x7 = 63')
        print('9x8 = 72')
        print('9x9 = 81')
        print('9x10 = 90')
    elif val == 10:
        print('10x0 = 0')
        print('10x1 = 10')
        print('10x2 = 20')
        print('10x3 = 30')
        print('10x4 = 40')
        print('10x5 = 50')
        print('10x6 = 60')
        print('10x7 = 70')
        print('10x8 = 80')
        print('10x9 = 90')
        print('10x10 = 100');

    msgs = 'obrigado'
    return msgs


