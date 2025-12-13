import sys

class RecursiveDescentParser:
    def __init__(self, input_string):
        self.source = input_string
        self.pos = 0
        self.length = len(input_string)
        self.errors = []

    def peek(self):
        """Retorna o caractere atual sem consumir, ignorando espaços fora de strings."""
        self._skip_whitespace()
        if self.pos >= self.length:
            return None
        return self.source[self.pos]

    def consume_char(self):
        """Retorna o caractere atual e avança o cursor (sem pular espaços automaticamente)."""
        if self.pos >= self.length:
            return None
        char = self.source[self.pos]
        self.pos += 1
        return char

    def match(self, char):
        """Verifica se o próximo caractere é o esperado e o consome."""
        if self.peek() == char:
            self.pos += 1
            return True
        return False

    def _skip_whitespace(self):
        """Pula espaços em branco (exceto dentro de tokens que tratam seus próprios chars)."""
        while self.pos < self.length and self.source[self.pos] in ' \t\n\r':
            self.pos += 1

    def error(self, message):
        raise Exception(f"Erro de Sintaxe na posição {self.pos}: {message}")

    def parse(self):
        """Ponto de entrada."""
        try:
            self.inicial()
            if self.peek() is not None:
                self.error("Entrada contém caracteres após o fim da análise.")
            return "Cadeia Aceita"
        except Exception as e:
            return f"Erro: {str(e)}"

    def inicial(self):
        """INICIAL -> VAR [ INDEX ]"""
        # 1. VAR
        self.var()
        
        # 2. [
        if not self.match('['):
            self.error("Esperado '[' após variável.")
            
        # 3. INDEX
        self.index()
        
        # 4. ]
        if not self.match(']'):
            self.error("Esperado ']' final.")

    def var(self):
        """VAR -> LETRA VAR | LETRA"""

        char = self.peek()
        if not char or not char.isalpha():
            self.error("Esperado uma VAR (começando com letra).")
    
        while self.pos < self.length:
            if self.source[self.pos].isalpha():
                self.pos += 1
            else:
                break

    def index(self):
        """
        INDEX -> NUM | STR | SLICE_NUM | SLICE_STR | INICIAL | INICIAL OP VALOR
        A estratégia aqui é Lookahead para decidir o caminho.
        """
        char = self.peek()
        
        if char is None:
            self.error("Index vazio inesperado.")

        # Caso 1: String ou Slice de String
        if char == '"' or char == "'":
            self.string_literal()
            # Verifica se é SLICE_STR
            if self.peek() == ':':
                self.match(':')
                # O segundo argumento do slice é opcional
                next_char = self.peek()
                if next_char == '"' or next_char == "'":
                    self.string_literal()
            return

        # Caso 2: Número ou Slice Numérico
        if char.isdigit() or char == '-':
            self.num()
            # Verifica se é SLICE_NUM
            if self.peek() == ':':
                self.match(':')
                # O segundo argumento do slice é opcional
                next_char = self.peek()
                if next_char and (next_char.isdigit() or next_char == '-'):
                    self.num()
            return

        # Caso 3: Slice começando com vazio
        if char == ':':
            self.match(':')
            next_char = self.peek()
            if next_char == '"' or next_char == "'":
                self.string_literal()
            elif next_char and (next_char.isdigit() or next_char == '-'):
                self.num()
            return

        # Caso 4: INICIAL
        if char.isalpha():
            self.inicial()
            
            next_char = self.peek()
            if next_char in ['=', '!', '<', '>']:
                self.op()
                self.valor()
            return

        self.error(f"Caractere inválido no INDEX: '{char}'")

    def num(self):
        """NUM -> -DIGITOS | DIGITOS"""
        if self.source[self.pos] == '-':
            self.pos += 1
        
        if not (self.pos < self.length and self.source[self.pos].isdigit()):
            self.error("Esperado dígitos para formar um número.")
            
        while self.pos < self.length and self.source[self.pos].isdigit():
            self.pos += 1

    def string_literal(self):
        """STR -> '...' | "..." """
        quote_type = self.peek()
        if quote_type not in ["'", '"']:
            self.error("Esperado início de string (' ou \").")
        
        self.pos += 1
        
        found_close = False
        while self.pos < self.length:
            char = self.source[self.pos]
            self.pos += 1
            if char == quote_type:
                found_close = True
                break
        
        if not found_close:
            self.error("String não foi fechada.")

    def op(self):
        """OP -> == | != | < | <= | > | >= """
        # Lê o operador. Pode ter 1 ou 2 caracteres.
        c1 = self.consume_char()
        if c1 not in ['<', '>', '=', '!']:
             self.error("Operador inválido.")
             
        # Verifica se o próximo é '='
        if self.pos < self.length and self.source[self.pos] == '=':
            self.pos += 1

    def valor(self):
        """VALOR -> NUM | STR | VAR"""
        char = self.peek()
        if char is None:
            self.error("Esperado VALOR.")

        if char.isdigit() or char == '-':
            self.num()
        elif char == '"' or char == "'":
            self.string_literal()
        elif char.isalpha():
            self.var()
        else:
            self.error("VALOR inválido (deve ser NUM, STR ou VAR).")

# --- Testes ---

test_cases = [
    "x[150]",            # Exemplo 1
    "y[\"Data\"]",       # Exemplo 2
    "Z[-1:]",            # Exemplo 3
    "x[ : 'Nome']",      # Exemplo 4
    "A[B[1]]",           # Exemplo 5
    "y[x[9]>5]"          # Exemplo 6
]

print(f"{'CADEIA DE ENTRADA':<20} | {'RESULTADO'}")
print("-" * 40)

for chain in test_cases:
    parser = RecursiveDescentParser(chain)
    result = parser.parse()
    print(f"{chain:<20} | {result}")