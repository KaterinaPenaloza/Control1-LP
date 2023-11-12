import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import TerminalNode
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor

# Función para imprimir un árbol sintáctico abstracto (AST) de manera más legible
from antlr4.tree.Tree import TerminalNodeImpl

def print_ast(node, indent=0):
    if isinstance(node, TerminalNodeImpl):
        # Imprimir solo el texto de los nodos terminales
        print('  ' * indent + str(node.getText()))
    else:
        print('  ' * indent + str(type(node).__name__))
        for child in node.getChildren():
            print_ast(child, indent + 1)

if __name__ == '__main__':
    # Maneja los argumentos dados, ya sea desde un archivo o desde la entrada estándar
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    # Definiciones de los archivos (lexer, los tokens a partir del analizador léxico y el parser)
    lexer = gramaticaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gramaticaParser(token_stream)

    # Se realiza el análisis sintáctico con el parser y se obtiene el AST
    tree = parser.prog()

    # Imprime el árbol sintáctico abstracto (AST)
    print("Abstract Syntax Tree (AST):")
    print_ast(tree)

    # Se realiza la visita de los nodos para la ejecución
    visitor = gramaticaVisitor()
    visitor.visit(tree)

    print("\nResultado de la ejecución:")
