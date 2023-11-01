from time import sleep


def maior(*num):
    print('Analisando os valores passados...')

    for n in num:
        sleep(0.6)
        print(n, end=' ')

    if len(num) == 0:
        m = 0

    else:
        for i in range(0, len(num)):
            if i == 0:
                m = num[i]

            else:
                if num[i] > m:
                    m = num[i]

    print(f'Ao todo foram informados {len(num)} valores.')
    print(f'O maior valor foi {m}.')
    print('-=' * 20)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
