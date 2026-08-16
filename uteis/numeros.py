"""
Funções básicas para trabalhar com números.
"""


def eh_par(numero):
    """Retorna True se o número for par."""
    return numero % 2 == 0


def maior_valor(*valores):
    """Retorna o maior valor entre os informados."""
    return max(valores)


def menor_valor(*valores):
    """Retorna o menor valor entre os informados."""
    return min(valores)


def media(*valores):
    """Calcula a média aritmética dos valores."""
    return sum(valores) / len(valores)


def eh_primo(numero):
    """Retorna True se o número for primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


if __name__ == '__main__':
    print('5 é par?', eh_par(5))
    print('Maior valor:', maior_valor(4, 9, 2, 7))
    print('Menor valor:', menor_valor(4, 9, 2, 7))
    print('Média:', media(4, 9, 2, 7))
    print('7 é primo?', eh_primo(7))
