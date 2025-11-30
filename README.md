# AnaliseLexica-COMPILADORES

Trabalho referente a unidade 2 da Disciplina de Compiladores. Este projeto implementa um analisador léxico simples utilizando **Python** e **Expressões Regulares (Regex)** para validar formatos de moeda (valores monetários).

## 📋 Descrição do Problema

O objetivo é reconhecer cadeias de caracteres que representem valores monetários válidos, respeitando as seguintes regras léxicas:

* **Símbolo:** Aceita `$` ou siglas de moedas (ex: `R$`, `US$`).
* **Formato Numérico:**
    * Aceita separador de milhar com ponto (`.`).
    * Obriga o uso de vírgula (`,`) para decimais (mínimo 2 casas).
    * Não aceita zeros à esquerda não significativos (ex: `05,00` é inválido).
* **Sinais:**
    * Positivos: `R$10,00`
    * Negativos com sinal: `-$10,00`
    * Negativos contábeis (entre parênteses): `(R$10,00)`

## 🚀 Como Executar

Este projeto foi desenvolvido para ser executado via linha de comando (terminal). É necessário ter o **Python 3** instalado.

### Passo 1: Clone ou baixe o repositório
Certifique-se de estar na pasta onde o arquivo do script está salvo (ex: `app.py`).

### Passo 2: Executando o teste
Utilize o comando abaixo, passando a string que deseja testar como argumento.

**⚠️ Importante:**
1.  Como terminais Linux/Mac e PowerShell interpretam o símbolo `$` como variável, use **aspas simples** (`'...'`).
2.  No Windows, o comando padrão costuma ser apenas `python`, enquanto no Linux/Mac é `python3`.

```bash
# Linux / macOS
$ python3 app.py 'R$1.500,00'

# Windows (CMD ou PowerShell)
> python app.py 'R$1.500,00'
