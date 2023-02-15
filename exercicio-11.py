numero = input('Digite um número: ')

try:
    numero = int(numero)
    divisao = 1/numero
except:
    if type(numero) == str:
        raise Exception('Você digitou texto')
    elif numero == 0:
        raise Exception('Você digitou zero')
    else:
        raise Exception('Erro genérico')
else:
    print(divisao)
finally:
    print('Meu nome é Geverson Araujo')
