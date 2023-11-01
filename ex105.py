def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: Uma ou mais notas dos alunos. (aceita vários valores.)
    :param sit: Valor opcional, indicando se deve ou não indicar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    -- ⛱.
    """
    # Cria um dicíonario e analise os valores
    dicionario = {'Quantidade de Notas': len(n),
                  'Maior': max(n),
                  'Menor': min(n),
                  'Média': sum(n)/len(n)}
    # Identifica se o usúario quer ou a situação, e análisa ela de acordo com a média.
    if sit:
        if dicionario["Média"] >= 7:
            dicionario["Situação"] = 'BOA'

        elif dicionario["Média"] < 5:
            dicionario["Situação"] = 'RUIM'

        else:
            dicionario["Situação"] = 'RAZOÁVEL'
    # retorna o dicionario
    return dicionario


# programa principal
resp = notas(9.5, 10, 6.5, 5, 10, 4, sit=True)
print(resp)
