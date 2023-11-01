from ex115 import menu
from time import sleep

cores = {'branco': '\033[m',
         'vermelho': '\033[1;31m'}

while True:
    # menu de ações para o usuário
    op = menu.principal(['Pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])

    if op == 1:
        # mostra os dados cadastradados ao usuário
        menu.pessoas_cadastradas()

    elif op == 2:
        # cadastra um novo usuário
        menu.cadastrar()

    elif op == 3:
        # finaliza o sistema
        menu.titulo('Saindo do sistema... Até logo!')
        break

    else:
        # erro caso o usuário digite um valor ínvalido
        print(f'{cores["vermelho"]}ERRO! Por favor, digite uma opção válida.{cores["branco"]}')

    sleep(2)
