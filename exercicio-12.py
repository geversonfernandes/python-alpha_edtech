class Viagem:
    origem: str
    destino: str


viagem1 = Viagem()
viagem1.origem = input('Digite a origem: ')
viagem1.destino = input('Digite o destino: ')

viagem2 = Viagem()
viagem2.origem = input('Digite a origem: ')
viagem2.destino = input('Digite o destino: ')

if viagem1.destino == viagem2.origem:
    viagem3 = Viagem()
    viagem3.origem = viagem1.origem
    viagem3.destino = viagem2.destino
    print('Viagem 3 concluída')
else:
    print('Não foi possível concluir a viagem')
