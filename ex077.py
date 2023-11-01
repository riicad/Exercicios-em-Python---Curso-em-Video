palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in range(0, len(i)):
        if i[letra] in 'a e i o u':
            print(i[letra], end=' ')
