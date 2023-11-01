from time import sleep

cores = {'verde': '\033[7;32m',
         'azul': '\033[7;36m',
         'cinza': '\033[0;37m',
         'branco': '\033[7;38m',
         'vermelho': '\033[7;31m'}


def titulo(cor="branco", msg=''):
    """
    -> Função cria um titulo da cor que o usúario escolher.
    :param cor: Valor opcinal, deixa o titulo da cor que o usúario escolher.
    lista de cores: verde, azul, cinza, branco, vermelho. Ex: ('verde', 'Título')
    :param msg: Texto/Titúlo informado pelo usúario.
    -- ⛱.
    """
    cores = {'verde': '\033[7;32m',
             'azul': '\033[7;36m',
             'cinza': '\033[0;37m',
             'branco': '\033[7;38m',
             'vermelho': '\033[7;31m'}

    print(f'{cores[f"{cor}"]}~' * (len(msg) + 4))
    print(f'  {msg} ')
    print('~' * (len(msg) + 4))


# programa principal
while True:
    titulo('verde', 'SISTEMA DE AJUDA PyHELP')

    quest = str(input(f'{cores["cinza"]}Função ou Biblioteca > '))
    if quest.lower() != 'fim':

        titulo("azul", f"Acessando o manual do comando '{quest}'")

        sleep(1)
        print(f'{cores["branco"]}')
        help(quest)

    else:
        break

titulo('vermelho', 'ATÉ LOGO!')
