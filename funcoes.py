
def somar():
    print('Esta funcao vai somar')


def muti():
    print('Esta funcao vai multiplicar')


def find_index(to_find, itens):
    for w, valor in enumerate(to_find):
        if valor == itens:
            return w
    return 'fora'


