import re
import sys

SIMBOLO = r"(\$|[a-zA-Z]+\$?)"
DIGITO_INICIAL = r"(0|[1-9][0-9]{0,2})" 
MILHAR = r"(\.[0-9]{3})*"
INTEIRO = f"{DIGITO_INICIAL}{MILHAR}"
FRACAO = r"(,[0-9]{2,})"
NUM_POSITIVO = f"{INTEIRO}{FRACAO}"
NUM_NEGATIVO_MENOS = f"-{NUM_POSITIVO}"
NUM_NEGATIVO_PARENTESIS = f"\\({NUM_POSITIVO}\\)"

NUM_COMPLETO = f"(?:{NUM_POSITIVO}|{NUM_NEGATIVO_MENOS}|{NUM_NEGATIVO_PARENTESIS})"

MOEDA = f"{SIMBOLO}{NUM_COMPLETO}"

def validar(palavra):
    return bool(re.fullmatch(MOEDA, palavra))

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        resultado = validar(entrada)
        print(f"Entrada: '{entrada}' -> Válido? {resultado}")
    else:
        print("Erro: Você precisa fornecer uma palavra.")
        print("Exemplo de uso: python3 seu_arquivo.py 'R$10,00'")import re
import sys

SIMBOLO = r"(\$|[a-zA-Z]+\$?)"
DIGITO_INICIAL = r"(0|[1-9][0-9]{0,2})" 
MILHAR = r"(\.[0-9]{3})*"
INTEIRO = f"{DIGITO_INICIAL}{MILHAR}"
FRACAO = r"(,[0-9]{2,})"
NUM_POSITIVO = f"{INTEIRO}{FRACAO}"
NUM_NEGATIVO_MENOS = f"-{NUM_POSITIVO}"
NUM_NEGATIVO_PARENTESIS = f"\\({NUM_POSITIVO}\\)"

NUM_COMPLETO = f"(?:{NUM_POSITIVO}|{NUM_NEGATIVO_MENOS}|{NUM_NEGATIVO_PARENTESIS})"

MOEDA = f"{SIMBOLO}{NUM_COMPLETO}"

def validar(palavra):
    return bool(re.fullmatch(MOEDA, palavra))

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        resultado = validar(entrada)
        print(f"Entrada: '{entrada}' -> Válido? {resultado}")
    else:
        print("Erro: Você precisa fornecer uma palavra.")
        print("Exemplo de uso: python3 seu_arquivo.py 'R$10,00'")
