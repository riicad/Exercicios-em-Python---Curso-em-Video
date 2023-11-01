def voto(a=0):
    from datetime import date
    idade = date.today().year - a

    if 65 >= idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'

    else:
        return f'Com {idade} anos: VOTO OPCIONAL!'


# programa principal
adn = int(input('Ano de nascimento: '))
print(voto(adn))
