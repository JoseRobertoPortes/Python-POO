"""
Funções básicas para trabalhar com dinheiro em Python.
Usa o módulo locale para formatar valores no padrão R$ (Real Brasileiro).
"""

import locale

# Configura o locale para o padrão brasileiro.
# Tenta alguns nomes comuns, pois o nome varia entre Windows/Linux/Mac.
_LOCALES_PT_BR = ('pt_BR.UTF-8', 'pt_BR.utf8',
                  'pt_BR', 'Portuguese_Brazil.1252')

_locale_ok = False
for _loc in _LOCALES_PT_BR:
    try:
        locale.setlocale(locale.LC_ALL, _loc)
        _locale_ok = True
        break
    except locale.Error:
        continue


def formatar_moeda(valor):
    """Formata um número como moeda (R$ 1.234,56).

    Se o locale pt_BR não estiver instalado no sistema, cai num
    formato manual equivalente, para a função nunca quebrar.
    """
    if _locale_ok:
        return locale.currency(valor, grouping=True, symbol=True)

    # Fallback manual (sem depender do locale.currency do sistema)
    texto = f'{valor:,.2f}'
    texto = texto.replace(',', '#').replace('.', ',').replace('#', '.')
    return f'R$ {texto}'


def somar_valores(*valores):
    """Soma vários valores e retorna já formatado em moeda."""
    total = sum(valores)
    return formatar_moeda(total)


def calcular_desconto(valor, percentual):
    """Calcula o valor com desconto aplicado."""
    desconto = valor * (percentual / 100)
    valor_final = valor - desconto
    return formatar_moeda(valor_final)


def calcular_aumento(valor, percentual):
    """Calcula o valor com aumento aplicado."""
    aumento = valor * (percentual / 100)
    valor_final = valor + aumento
    return formatar_moeda(valor_final)


def dividir_valor(valor, partes):
    """Divide um valor em N partes iguais."""
    if partes <= 0:
        raise ValueError('O número de partes deve ser maior que zero.')
    parte = valor / partes
    return formatar_moeda(parte)


def converter_moeda(valor, cotacao):
    """Converte um valor usando uma cotação (ex: dólar, euro)."""
    convertido = valor * cotacao
    return formatar_moeda(convertido)


if __name__ == '__main__':
    # Exemplos de uso
    print('Valor formatado:', formatar_moeda(1500.5))
    print('Soma:', somar_valores(100, 250.75, 30))
    print('Com 10% de desconto:', calcular_desconto(200, 10))
    print('Com 15% de aumento:', calcular_aumento(200, 15))
    print('Dividido em 3 partes:', dividir_valor(300, 3))
    print('Convertido (cotação 5.20):', converter_moeda(100, 5.20))
