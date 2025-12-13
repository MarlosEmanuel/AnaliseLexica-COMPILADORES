# AnaliseSintatica-COMPILADORES

Trabalho referente à disciplina de Compiladores. Este projeto implementa um **Analisador Sintático Descendente Recursivo** utilizando **Python** para validar sentenças baseadas em uma Gramática Livre de Contexto (GLC) específica para acesso a arrays e fatiamento (slicing).

## 📋 Descrição do Problema

O objetivo é reconhecer cadeias de caracteres que representem estruturas de indexação de variáveis, respeitando as regras de produção da gramática. O analisador valida estruturas como:

  * **Variáveis:** Sequências de letras (ex: `x`, `Var`, `Data`).
  * **Indexação:** Uso obrigatório de colchetes `[...]`.
  * **Tipos de Índice:**
      * Números inteiros (ex: `x[150]`, `Z[-1]`).
      * Strings com aspas simples ou duplas (ex: `y["Data"]`).
      * **Slicing (Fatiamento):** Uso de dois pontos para intervalos (ex: `Z[-1:]`, `x[:'Nome']`).
  * **Recursividade:** Índices que contêm outras indexações (ex: `A[B[1]]`).
  * **Expressões Relacionais:** Comparações dentro do índice (ex: `y[x[9]>5]`).

## 🚀 Como Executar

Este projeto foi desenvolvido para ser executado via linha de comando (terminal). É necessário ter o **Python 3** instalado.

### Passo 1: Clone ou baixe o repositório

Certifique-se de estar na pasta onde o arquivo do script está salvo (ex: `parser.py`).

### Passo 2: Configurando os testes

O código já inclui uma lista de casos de teste pré-definidos no final do arquivo (variável `test_cases`). Caso queira testar novas cadeias, edite a lista diretamente no código:

```python
test_cases = [
    "x[150]",
    "y[\"Data\"]",
    "SUA_NOVA_CADEIA_AQUI"
]
```

### Passo 3: Executando o analisador

Utilize o comando abaixo para rodar o script e processar a lista de testes.

```bash
# Linux / macOS
$ python3 parser.py

# Windows (CMD ou PowerShell)
> python parser.py
```

## 📊 Exemplo de Saída

Ao executar o programa, você verá um relatório indicando se cada cadeia foi aceita ou se houve erro de sintaxe:

```text
CADEIA DE ENTRADA    | RESULTADO
----------------------------------------
x[150]               | Cadeia Aceita
y["Data"]            | Cadeia Aceita
Z[-1:]               | Cadeia Aceita
x[ : 'Nome']         | Cadeia Aceita
A[B[1]]              | Cadeia Aceita
y[x[9]>5]            | Cadeia Aceita
```

## 🛠️ Tecnologias Utilizadas

  * **Python 3**: Linguagem base.
  * **Paradigma**: Análise Descendente Recursiva (Top-Down Parsing).
  * **Lookahead**: Verificação de tokens futuros para decisão de fluxo.