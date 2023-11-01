Primeiro = int(input('Primeiro número: '))
Segundo = int(input('Segundo número: '))
Terceiro = int(input('Terceiro número: '))
N1 = Primeiro
N2 = Segundo
N3 = Terceiro
if Primeiro < Segundo < Terceiro:
    print('Menor número: {}'.format(N1))
    print('Maior número: {}'.format(N3))
else:
    if Terceiro < Segundo < Primeiro:
        print('Menor número: {}'.format(N3))
        print('Maior número: {}'.format(N1))
    else:
        if Primeiro < Terceiro < Segundo:
            print('Menor número: {}'.format(N1))
            print('Maior número: {}'.format(N2))
        else:
            if Terceiro < Primeiro < Segundo:
                print('Menor número: {}'.format(N3))
                print('Menor número: {}'.format(N2))
            else:
                if Segundo < Primeiro < Terceiro:
                    print('Menor número: {}'.format(N2))
                    print('Maior número: {}'.format(N3))
                else:
                    print('Menor número: {}'.format(N2))
                    print('Maior número: {}'.format(N1))
