# Python POO

Repositório de estudos em Python orientado a objetos: exercícios, desafios e exemplos práticos aplicando os principais conceitos de POO (encapsulamento, herança, polimorfismo, classes abstratas, properties). *(work in progress)*

## Estrutura

- **desafios/**: desafios de POO, um por pasta, cada um com sua análise de requisitos e implementação
- **exercicios/**: resoluções de exercícios menores, em ordem crescente de complexidade
- **rich/**: exemplos de uso da biblioteca [Rich](https://github.com/Textualize/rich) para saída formatada no terminal
- **uteis/**: funções utilitárias reaproveitadas entre os exercícios (formatação de dinheiro, números etc.)

## Índice de desafios

| Desafio | Tema |
|---|---|
| 016 | Classe `Funcionario` com atributos padrão |
| 017 | Classe `Produto` com formatação monetária (locale) |
| 018 | Classe `Churrasco` com cálculo de quantidades |
| 019 | Classe `Livro` simulando leitura página a página |
| 020 | Classe `Jogador` com lista de jogos favoritos |
| 021 | Classe `Caneta` com estado (tampada/destampada) |
| 022 | Classe `ControleRemoto` com limites de canal/volume |
| 023 | Polígonos com classe abstrata (`Poligono`, `Circulo`, `Quadrado`) |
| 024 | Bebidas quentes com herança e método template (`BebidaQuente`, `Cha`, `Cafe`) |
| 025 | Cálculo de frete por tipo de transporte, com tabela via Rich |
| 026 | Funcionários horistas e mensalistas com cálculo de salário |
| 027 | Sistema de personagens de RPG com ataques |
| 028 | Termostato com `@property` e limites de temperatura |
| 029 | Diário protegido por senha (encapsulamento) |
| 030 | Credenciais com hash de senha (SHA-256) |
| 031 | Classe `Retangulo` com validação de medidas |
| 032 | Conta bancária com saldo, saques e depósitos |
| 033 | Hierarquia `Pessoa` → `Aluno`, com cursos disponíveis |

## Como executar

A execução depende do arquivo específico que você quiser testar. Em geral:

```bash
python desafios/desafio024/__main__.py
```

## Tecnologias

- Python
- Rich

## Conceitos praticados

- Encapsulamento (`@property` / atributos privados)
- Herança e classes abstratas (`ABC`, `@abstractmethod`)
- Polimorfismo
- Tratamento de exceções personalizadas
- Formatação de saída com Rich
