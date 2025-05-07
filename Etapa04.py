# Passo 1: Importar o módulo math.
import math
 
def adicionar(n1, n2):
    """Retorna a soma de dois números."""
    return n1 + n2
 
def subtrair(n1, n2):
    """Retorna a diferença entre dois números."""
    return n1 - n2
 
def multiplicar(n1, n2):
    """Retorna o produto de dois números."""
    return n1 * n2
 
def dividir(n1, n2):
    """Retorna o quociente da divisão de dois números."""
    return n1 / n2
 
# Passo 2: Implementar funções para cálculos de potenciação, radiciação, trigonometria e logaritmos.
def potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return math.pow(base, expoente)
 
def radiciacao(numero, raiz):
    """Retorna a raiz de um número."""
    if numero < 0 and raiz % 2 == 0:
        raise ValueError("Raiz par de número negativo não é real.")
    return math.pow(numero, 1/raiz)

def seno(angulo_graus):
    """Retorna o seno de um ângulo em graus."""
    return math.sin(math.radians(angulo_graus))