# Funções Básicas

Pasta com funções utilitárias básicas para programação em Python.

## Arquivos

- **dinheiro.py** — funções focadas em dinheiro, usando `locale.currency` para
  formatar valores em Real (R$). Inclui formatação, soma, desconto, aumento,
  divisão de valores e conversão de moeda. Se o locale `pt_BR` não estiver
  instalado no sistema, a função cai automaticamente num formato manual
  equivalente (não quebra o programa).
- **numeros.py** — funções básicas de números (par/ímpar, maior, menor,
  média, número primo).

## Como usar

Importe as funções no seu script:

```python
from dinheiro import formatar_moeda, calcular_desconto
from numeros import media, eh_par

print(formatar_moeda(1500.5))
print(calcular_desconto(200, 10))
```

## Sobre o locale.currency

O `locale.currency` depende do locale `pt_BR` estar instalado no sistema
operacional. Em alguns Linux, é preciso gerar o locale antes:

```bash
sudo apt-get install locales
sudo locale-gen pt_BR.UTF-8
sudo update-locale
```

No Windows, normalmente já funciona com `'Portuguese_Brazil.1252'`.
